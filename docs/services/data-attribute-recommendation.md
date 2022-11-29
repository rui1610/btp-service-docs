# data-attribute-recommendation (Data Attribute Recommendation)

Data Attribute Recommendation uses free text, numbers and categories as input to classify entities such as products, stores and users into multiple classes and also to predict the value of missing numerical attributes in your data records. You can use Data Attribute Recommendation, for example, to classify incoming product information and predict the price of commodities based on their description.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **eu10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-DAR

### Discovery Center

- [SAP Discovery Center - Data Attribute Recommendation](https://discovery-center.cloud.sap/serviceCatalog/data-attribute-recommendation)

### Documentation

- [Documentation](https://help.sap.com/dar)
- [Feature Scope Description](https://help.sap.com/doc/a989e835b2ef407b9d104402e130da27/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [Help Portal Product Page](https://help.sap.com/docs/Data_Attribute_Recommendation)
- [Security](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/3cb3e86f07164272bf3c3dea2a55a2a5.html)
- [What's New](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/404e7e4be1814cebbd6957e7e413785d.html)
- [What Is Data Attribute Recommendation?](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/6fade604ebe6459983699b3b5d9e8e59.html)
- [API Documentation](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/b45cf9b24fd042d082c16191aa938c8d.html)
- [Concepts](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/cff2de73bc9c4625b35eb036439ae70a.html)
- [Initial Setup](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/e8d18fbd1c0445e4a39dd1b66d942962.html)

### External

- [SAP AI Business Services - Data Attribute Recommendation](https://www.youtube.com/embed/6IWV3pg2BK8)
- [Efficient and High-Quality Master Data Management with Data Attribute Recommendation](https://www.youtube.com/embed/83-bLATU74U)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Data%20Attribute%20Recommendation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Data%20Attribute%20Recommendation)
- [SAP Community Topic Page](https://community.sap.com/topics/data-attribute-recommendation)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/Data_Attribute_Recommendation/105bcfd88921418e8c29b24a7a402ec3/4fb850f57a7848cab74f180c129c0b86.html)
- [Support](https://help.sap.com/viewer/105bcfd88921418e8c29b24a7a402ec3/SHIP/en-US/4fb850f57a7848cab74f180c129c0b86.html)

### Tutorial

- [Use Machine Learning and the Invoice Object Recommendation Business Blueprint to Predict Invoice Financial Objects](https://developers.sap.com/group.cp-aibus-dar-predict-invoice.html)
- [Use Machine Learning and the Regression Model Template to Predict Data Records](https://developers.sap.com/group.cp-aibus-dar-regression-predict-data.html)
- [Classify Data Records with the SDK for Data Attribute Recommendation](https://developers.sap.com/group.cp-aibus-data-attribute-sdk.html)
- [Use Machine Learning to Classify Data Records](https://developers.sap.com/mission.cp-aibus-data-attribute.html)

## Sample configuration of **Data Attribute Recommendation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-attribute-recommendation** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-attribute-recommendation",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-attribute-recommendation",
      "plan": "standard"
    }
  ]
}
```
