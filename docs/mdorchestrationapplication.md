# MDOrchestrationApplication (SAP Master Data Orchestration)

Master data application for existing customers of SAP Master Data service for business partners and SAP Master Data service for products. New customers should use the Master Data Integration (Orchestration) tile. SAP Master Data Orchestration should only be used in combination with the SAP Master Data Integration service.

## Service plan availability in regions

| Region | saas-application |
|--------|------------------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/viewer/product/DRAFT/SAP_CLOUD_PLATFORM_MASTER_DATA_INTEGRATION/CLOUD/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Master%20Data%20Orchestration)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Master%20Data%20Orchestration)

## Sample configuration of **SAP Master Data Orchestration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **MDOrchestrationApplication** by configuring your `usecase.json` file.

### Using the service plan **saas-application** (Master data application that allows master data replication according to predetermined master data distribution models)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "MDOrchestrationApplication",
      "plan": "saas-application"
    }
  ]
}
```
