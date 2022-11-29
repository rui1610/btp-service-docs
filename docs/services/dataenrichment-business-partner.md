# dataenrichment-business-partner (Data Enrichment)

Industrializes the use of third-party data for enterprise applications, and makes it economical to find, procure and consume relevant datasets in timely fashion. Offers pre-built integrations with SAP S/4HANA Cloud and on-premise, and SAP Master Data Governance. Centrally links data from external data providers such as Dun & Bradstreet and CDQ into SAP enterprise applications, reducing overall TCO for data brokerage needs. Data Enrichment will be a one stop shop for multiple data augmentation needs.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **ap11** | ✅ |
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Blog

- [Industrialize Your Use of Third Party Data with SAP Data Enrichment service](https://blogs.sap.com/2019/10/22/industrialize-your-use-of-third-party-data-with-sap-s4hana-cloud-for-data-enrichment/)
- [Try out SAP Data Enrichment service for Free](https://blogs.sap.com/2019/12/26/try-out-sap-cloud-platform-data-enrichment-for-free/)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/data-enrichment)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/ffa27d7844f84f86b6af40b3f73a7ee6/latest/en-US/loiob0ae78ea148b445989d87f062fa39602_b0ae78ea148b445989d87f062fa39602.pdf)
- [API Documentation](https://help.sap.com/viewer/b2e912080b9c48b3a7066d59acc9f0d9/latest/en-US)
- [What is SAP Data Enrichment service?](https://help.sap.com/viewer/c97f1890387147679ab6a8cbf8276cf8/latest/en-US)
- [What's New](https://help.sap.com/viewer/dfcc98cbbcab4c109e17832fdad7bd3d/latest/en-US)
- [Initial Setup](https://help.sap.com/viewer/e6d9a574e3ae4c30b64a4b8246b3d7e6/latest/en-US)
- [Onboarding](https://help.sap.com/viewer/e6d9a574e3ae4c30b64a4b8246b3d7e6/latest/en-US/ea1bb6c3f1ba440aa5bf92ef2e64d958.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/Cloud_Platform_Data_Enrichment/latest/en-US)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Data Enrichment** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dataenrichment-business-partner** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "dataenrichment-business-partner",
      "plan": "default"
    }
  ]
}
```
