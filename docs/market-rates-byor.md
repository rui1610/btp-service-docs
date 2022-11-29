# market-rates-byor (SAP Market Rates Management)

The Market Rates Management, Bring Your Own Rates data option allows you to upload and download your own market rates licensed from third party data providers

## Service plan availability in regions

| Region | default | free |
|--------|---------|------|
|  **eu10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- LOD-CBS-CS

### API Hub

- [Overview | SAP Market Rates Management, Bring Your Own Rates data option | SAP API Business Hub](https://api.sap.com/package/MarketRatesManagementBYORAPI/overview)

### Discovery Center

- [SAP Discovery Center - Market Rates, Bring Your Own Rates](https://discovery-center.cloud.sap/serviceCatalog/market-rates-bring-your-own-rates)

### Documentation

- [API Documentation](https://api.sap.com/package/MarketRatesManagementBYORAPI)
- [What is the Bring Your Own Rates data option](https://help.sap.com/viewer/64e0eccf2d424543be76606dd5e5e460/LATEST/en-US)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_CP_BUS_REUSE_SERVICE_MRM_APP)
- [Documentation](https://help.sap.com/viewer/product/SAP_CP_BUS_REUSE_SERVICE_MRM_APP/LATEST/en-US)

### External

- [SAP Market Rates Management, Bring Your Own Rates Data Option](https://www.youtube.com/embed/h_0pIIPNhJY)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Market%20Rates%20Management)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Market%20Rates%20Management)

## Sample configuration of **SAP Market Rates Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **market-rates-byor** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "market-rates-byor",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "market-rates-byor",
      "plan": "free"
    }
  ]
}
```
