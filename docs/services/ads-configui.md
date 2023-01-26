# ads-configui (Forms Service by Adobe)

SAP Forms service by Adobe lets you generate print and interactive forms using Adobe Document Services (ADS). Call the service from your application using a REST API for rendering documents and for managing form templates in the template store. Configure ADS and access the template store via service-offered UIs. To use Forms service by Adobe, you must subscribe to the application (ads-configui) and set entitlements to both, the ADS (ads) and the REST API template store (adsrestapi) service. In the Service Marketplace, find all two tiles easily by entering 'adobe' into the search field.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- BC-SRV-FP-CF

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/protected/index.html#/serviceCatalog/forms-service-by-adobe)

### Documentation

- [Documentation](https://help.sap.com/docs/CP_FORMS_BY_ADOBE/dcbea777ceb3411cb10500a1a392273e/661c02ef20d54bfeb309d42608baeaca.html)

## Sample configuration of **Forms Service by Adobe** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ads-configui** by configuring your `usecase.json` file.

### Using the service plan **default** (Default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "ads-configui",
      "plan": "default"
    }
  ]
}
```
