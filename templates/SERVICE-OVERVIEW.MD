# Services in a PAYG Account

This lists shows all SAP BTP services that are available in an [SAP BTP pay-as-you-go account](https://www.sap.com/products/business-technology-platform/trial.html).

{% for category in services %}
## All services of category {{ category.name }}

Services are listed and sorted by their technical name. The display name is added in parentheses. Click on the link for a service to get service-specific details.
{% for service in category.list %}
- [{{ service.normalized_id }}](services/{{ service.normalized_id }}.md) ({{ service.displayName }})
{%- endfor %}
{% endfor %}
