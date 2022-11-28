# tnt-onboard-dataenrichment-dcp (SAP Data Enrichment service)

Provides Business Partner data from third-party data providers

## Service plan availability in regions

| Region | saas-application |
|--------|------------------|
|  **ap11** | ✅ |
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/viewer/product/Cloud_Platform_Data_Enrichment/latest/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Data%20Enrichment%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Data%20Enrichment%20service)

## Sample configuration of **SAP Data Enrichment service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **tnt-onboard-dataenrichment-dcp** by configuring your `usecase.json` file.

### Using the service plan **saas-application** (Data Enrichment)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "tnt-onboard-dataenrichment-dcp",
      "plan": "saas-application"
    }
  ]
}
```
