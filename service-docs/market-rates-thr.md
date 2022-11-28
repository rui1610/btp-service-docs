# market-rates-thr (Market Rates, Refinitiv)

The Market Rates Management, Refinitiv data option is a reuse service that allows you to import daily and historical Exchange Rates & Interest Rates from Refinitiv.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- LOD-CBS-CS

### API Hub

- [Overview | SAP Market Rates Management, Refinitiv data option | SAP API Business Hub](https://api.sap.com/package/MarketRatesManagementAPI/overview)

### Discovery Center

- [SAP Discovery Center - Market Rates, Refinitiv](https://discovery-center.cloud.sap/serviceCatalog/market-rates-refinitiv)

### Documentation

- [API Documentation](https://api.sap.com/package/MarketRatesManagementAPI)
- [What is Refinitiv data option](https://help.sap.com/viewer/9da8c81f87e0480fac3975cdd3182418/LATEST/en-US)
- [Initial Setup](https://help.sap.com/viewer/9da8c81f87e0480fac3975cdd3182418/LATEST/en-US/5e759c605bfe4b6ba52a06bf23f6c15c.html)
- [Documentation](https://help.sap.com/docs/SAP_CP_BUS_REUSE_SERVICE_MRM_TR)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAP_CP_BUS_REUSE_SERVICE_MRM_TR/LATEST/en-US?task=discover_task)

### External

- [SAP Market Rates Management, Refinitiv Data Option](https://www.youtube.com/embed/h_0pIIPNhJY)

## Sample configuration of **Market Rates, Refinitiv** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **market-rates-thr** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "market-rates-thr",
      "plan": "default"
    }
  ]
}
```
