# market-rates-ux (SAP Market Rates Management)

The Manage Market Rates application enables you to read and manage market data you have uploaded by using the data options available with the SAP Market Rates Management service

## Service plan availability in regions

| Region | mror | mrtr |
|--------|------|------|
|  **eu10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/market-rates-refinitiv)

### Documentation

- [Documentation](https://help.sap.com/docs/SAP_CP_BUS_REUSE_SERVICE_MRM_TR)

## Sample configuration of **SAP Market Rates Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **market-rates-ux** by configuring your `usecase.json` file.

### Using the service plan **mror** (SAP Market Rates Management)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "market-rates-ux",
      "plan": "mror"
    }
  ]
}
```

### Using the service plan **mrtr** (SAP Market Rates Management)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "market-rates-ux",
      "plan": "mrtr"
    }
  ]
}
```
