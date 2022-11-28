# mdo-one-mds-master (Master Data Integration (Orchestration))

Master data application that allows master data replication according to predetermined master data distribution models. SAP Master Data Orchestration can only be used in combination with the SAP Master Data Integration service.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **us10** | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/master-data-integration)

### Documentation

- [Documentation](https://help.sap.com/viewer/product/DRAFT/SAP_CLOUD_PLATFORM_MASTER_DATA_INTEGRATION/CLOUD/en-US)

## Sample configuration of **Master Data Integration (Orchestration)** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mdo-one-mds-master** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "mdo-one-mds-master",
      "plan": "standard"
    }
  ]
}
```
