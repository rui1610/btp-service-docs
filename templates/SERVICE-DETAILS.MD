{% macro printProperty(property, key) -%}
{% if property[key].get("default") is defined -%}"{{ key }}": {{ property[key].get("default") | tojson }}{% endif %}
{%- endmacro -%}
{% macro addSchemaParametersIfExists(plan) -%}
{% if plan.schemas is defined and plan.schemas.service_instance is defined and plan.schemas.service_instance.create is defined and plan.schemas.service_instance.create.parameters is defined and plan.schemas.service_instance.create.parameters.properties is defined -%},
      "parameters" : {
        {% for key in plan.schemas.service_instance.create.parameters.properties %}{{ printProperty(plan.schemas.service_instance.create.parameters.properties, key) }}{% if not loop.last %},
        {% endif %}{% endfor %}
      }
{%- endif -%}
{%- endmacro -%}
{% macro addRequiredFieldIfSchemaExists(plan) -%}
{% if plan.schemas is defined and plan.schemas.service_instance is defined and plan.schemas.service_instance.create is defined and plan.schemas.service_instance.create.parameters is defined -%}
, "required" : ["parameters"]
{% endif %}
{%- endmacro -%}
{% macro addDatacenter(plan) -%}
{% if plan.dataCenters is defined and plan.dataCenters is not none -%}
{%- for datacenter in plan.dataCenters %} {{ datacenter.region }} - {{ datacenter.displayName }} {% if not loop.last %}<br>{% endif %} {%- endfor -%}
{% endif %}
{%- endmacro -%}
{% macro hasCommercialIds(service) -%}
{% set ns = namespace(found=false) %}
{%- for plan in service.servicePlans -%}
  {%- if plan.dataCenters is defined and plan.dataCenters is not none -%}
    {%- for datacenter in plan.dataCenters -%}
      {%- if datacenter.materialNumberMappings is defined and datacenter.materialNumberMappings is not none and datacenter.materialNumberMappings|length > 0 -%}{% set ns.found = true %}
      {%- endif -%}
    {%- endfor -%}
  {%- endif -%}
{%- endfor -%}
{{ ns.found }}
{%- endmacro -%}
# {{ service.name }} ({{ service.displayName }})

{{ service.description }}
{%- if service.alternativeDescriptions is defined %}
{%- for otherDescriptions in service.alternativeDescriptions -%}
{%- if otherDescriptions.source is defined and otherDescriptions.source == "slmAsset" and otherDescriptions.type is defined and otherDescriptions.type == "largeDescription" %}

{{ otherDescriptions.value }}{%- endif -%}
{%- endfor %}
{%- endif %}

## Service plan availability in regions

| Region |{%- for plan in service.servicePlans %} {{ plan.name }} |{%- endfor %}
|--------|{%- for plan in service.servicePlans %}{{ '-' * (plan.name|length + 2) }}|{%- endfor %}
{%- for plansInRegion in plansInRegions %}
|  **{{ plansInRegion.region }}** |
  {%- for plan in service.servicePlans -%}
    {%- set ns = namespace(found=false) -%}
    {%- for planInRegion in plansInRegion.plans -%}
      {%- if planInRegion.name == plan.name -%}{% set ns.found = true %}{%- endif -%}
    {%- endfor -%}
    {%- if ns.found == true %} ✅ |{% else %} |{% endif -%}
  {%- endfor %}
{%- endfor %}

{%- if hasCommercialIds(service) == "True" %}

## Commercial IDs
{%- set materialNumbers = [] %}

| Material ID| Plan name | Metric | Charging period |
|-----------|-------------|--------|-----------------|
{%- for plan in service.servicePlans -%}
  {%- if plan.dataCenters is defined and plan.dataCenters is not none -%}
    {%- for datacenter in plan.dataCenters -%}
      {%- if datacenter.materialNumberMappings is defined and datacenter.materialNumberMappings is not none -%}
        {%- for materialNumberMapping in datacenter.materialNumberMappings -%}
          {%- if materialNumberMapping.materialNumber not in materialNumbers -%}{%- set materialNumbers = materialNumbers.append(materialNumberMapping.materialNumber) %}
| {{ materialNumberMapping.type }} {{ materialNumberMapping.materialNumber }} | {{ plan.name }} | {{ materialNumberMapping.metricId }} | {{ materialNumberMapping.chargingPeriod | lower }} |
          {%- endif -%}
        {%- endfor -%}
      {%- endif -%}
    {%- endfor -%}
  {%- endif -%}
{%- endfor -%}
{%- endif %}

## Additional details
{%- if service.supportComponents is defined and service.supportComponents|length > 0 %}

### Support components

{% for supportComponent in service.supportComponents -%}
- {{ supportComponent.value }}
{% endfor -%}
{%- endif -%}
{%- if service.links is defined and service.links is not none %}

{%- for link in service.links | groupby('classification') %}
### {{ link.grouper }}

{% for thislink in link.list -%}
- [{{ thislink.text }}]({{ thislink.value }})
{% endfor -%}
{% endfor -%}
{% endif %}
## Sample configuration of **{{ service.displayName }}** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **{{ service.name }}** by configuring your `usecase.json` file.
{% for plan in service.servicePlans %}
### Using the service plan **{{ plan.name }}**{% if plan.name != plan.displayName %} ({{ plan.displayName }}){% endif %}

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "{{ category.name }}",
      "name": "{{ service.name }}",
      "plan": "{{ plan.name }}"{{ addSchemaParametersIfExists(plan) }}
    }
  ]
}
```
{% endfor %}
