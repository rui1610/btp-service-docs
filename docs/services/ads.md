# ads (SAP Forms service by Adobe)

SAP Forms service by Adobe lets you generate print and interactive forms using Adobe Document Services (ADS). Call the service from your application using a REST API for rendering documents and for managing form templates in the template store. Configure ADS and access the template store via service-offered UIs. To use Forms service by Adobe, you must subscribe to the application (ads-configui) and set entitlements to both, the ADS (ads) and the REST API template store (adsrestapi) service. In the Service Marketplace, find all two tiles easily by entering 'adobe' into the search field.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- BC-SRV-FP-CF

### API Hub

- [Overview | SAP Forms Service by Adobe | SAP API Business Hub](https://api.sap.com/package/SAPFormsServicebyAdobe/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/protected/index.html#/serviceCatalog/forms-service-by-adobe)
- [SAP Discovery Center - Forms Service by Adobe](https://discovery-center.cloud.sap/serviceCatalog/forms-service-by-adobe)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/71ef297f952146e3a0d93588e801dea2/)
- [Documentation](https://help.sap.com/docs/CP_FORMS_BY_ADOBE/dcbea777ceb3411cb10500a1a392273e/8a668ee41fea4cf39c6bd6d21bff6a6e.html)
- [What is SAP Forms Service by Adobe](https://help.sap.com/viewer/dcbea777ceb3411cb10500a1a392273e/Cloud/en-US)
- [Initial Setup](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/0cd988a24b3240ab871bae62a6bb377f.html)
- [Configuration Tool](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/5e7f0a84b70349309094ebaf26cb3bfb.html)
- [Use Case](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/6320b2af29de47c9800f658b9f3f3a52.html)
- [API Documentation](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/661c02ef20d54bfeb309d42608baeaca.html)
- [Architecture](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/8f003de6886344428e28707b17cc8248.html)
- [Migration from On-Premise ADS or Neo Subaccount](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/9acaec4e6a7841ff9960f4b229320eb5.html)
- [Help Portal Product Page](https://help.sap.com/docs/CP_FORMS_BY_ADOBE)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Forms%20service%20by%20Adobe)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Forms%20service%20by%20Adobe)

### Support

- [Supportability and Troubleshooting](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/c066c9c309444391819debf01b9dd8fa.html)

### Tutorial

- [Development Guide](https://help.sap.com/docs/BTP/dcbea777ceb3411cb10500a1a392273e/c765f8ca186d47369b199032ccb83523.html)

## Sample configuration of **SAP Forms service by Adobe** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ads** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ads",
      "plan": "standard"
    }
  ]
}
```
