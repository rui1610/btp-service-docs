# data-analytics-osb (SAP Data Warehouse Cloud)

SAP Data Warehouse Cloud provides a single, fully-managed cloud environment to allow your organization to acquire, combine, prepare, and model data for consumption in analytics clients.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details
### API Hub

- [Overview | SAP Data Warehouse Cloud | SAP API Business Hub](https://api.sap.com/package/sapdatawarehousecloud/overview)

### Discovery Center

- [SAP Discovery Center - SAP Data Warehouse Cloud](https://discovery-center.cloud.sap/serviceCatalog/sap-data-warehouse-cloud)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/2e44fba46f674c179c0701d83526d67e/cloud/en-US/SAP_Data_Warehouse_Cloud_FSD.pdf)
- [Documentation](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD)
- [Documentation](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/c8a54ee704e94e15926551293243fd1d/7a453609c8694b029493e7d87e0de60a.html)
- [What's New](https://help.sap.com/viewer/5a2cf6cf78ee4f03bbd49714d79d8559/cloud/en-US)
- [Onboarding](https://help.sap.com/viewer/d4f3c5a0bb074d09ae9b42b2b9bd7a08/cloud/en-US)
- [What is SAP Data Warehouse Cloud](https://help.sap.com/viewer/d4f3c5a0bb074d09ae9b42b2b9bd7a08/cloud/en-US/5db9a099826c467e93ff0994fc185589.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAP_DATA_WAREHOUSE_CLOUD/cloud/en-US)

### External

- [What is SAP Data Warehouse Cloud?](https://www.youtube.com/embed/XdUFzWL-zFo)

### Learning

- [Learning Journey: SAP Data Warehouse Cloud](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/c4fcae2e2b7645109ab3315e8a7a6b10.html?IDs=show)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### Onboarding

- [Tutorial: Onboarding](https://www.sap.com/documents/2022/05/00d61914-287e-0010-bca6-c68f7e60039b.html)

### SAP Community

- [SAP Data Warehouse Cloud Community](https://community.sap.com/topics/data-warehouse-cloud)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Data%20Warehouse%20Cloud)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Data%20Warehouse%20Cloud)

### Support

- [Guidelines for SAP Data Warehouse Cloud Incidents](https://launchpad.support.sap.com/#/notes/2854764)

### Tutorial

- [Tutorials](https://developers.sap.com/tutorial-navigator.html?tag=software-product%3Atechnology-platform%2Fsap-data-warehouse-cloud%2Fsap-data-warehouse-cloud)
- [Experience SAP Data Warehouse Cloud](https://www.sap.com/products/data-warehouse-cloud.html)

## Sample configuration of **SAP Data Warehouse Cloud** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-analytics-osb** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-analytics-osb",
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
      "name": "data-analytics-osb",
      "plan": "standard"
    }
  ]
}
```
