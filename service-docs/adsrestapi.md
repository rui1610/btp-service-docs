# adsrestapi (SAP Forms service by Adobe)

SAP Forms service by Adobe lets you generate print and interactive forms using Adobe Document Services (ADS). Call the service from your application using a REST API for rendering documents and for managing form templates in the template store. Configure ADS and access the template store via service-offered UIs. To use Forms service by Adobe, you must subscribe to the application (ads-configui) and set entitlements to both, the ADS (ads) and the REST API template store (adsrestapi) service. In the Service Marketplace, find all two tiles easily by entering 'adobe' into the search field.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Forms Service by Adobe | SAP API Business Hub](https://api.sap.com/package/SAPFormsServicebyAdobe/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/protected/index.html#/serviceCatalog/forms-service-by-adobe)

### Documentation

- [Documentation](https://help.sap.com/viewer/dcbea777ceb3411cb10500a1a392273e/Cloud/en-US)
- [Documentation](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/661c02ef20d54bfeb309d42608baeaca.html)
- [Documentation](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/8f003de6886344428e28707b17cc8248.html)
- [Documentation](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/9acaec4e6a7841ff9960f4b229320eb5.html)
- [Documentation](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/c765f8ca186d47369b199032ccb83523.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Forms%20service%20by%20Adobe)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Forms%20service%20by%20Adobe)

### Swagger

- [Swagger](https://adsrestapi-formsprocessing.cfapps.eu10.hana.ondemand.com/swagger-ui.html)
- [Swagger](https://adsrestapi-formsprocessing.cfapps.us10.hana.ondemand.com/swagger-ui.html)

## Sample configuration of **SAP Forms service by Adobe** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **adsrestapi** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "adsrestapi",
      "plan": "standard"
    }
  ]
}
```
