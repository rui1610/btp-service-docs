# data-intelligence (SAP Data Intelligence Cloud)

SAP Data Intelligence is the all-in-one data orchestration solution to discover, refine, enriche and govern any type, variety, and volume of data across your entire distributed data landscape. Deliver on the promise of AI with enterprise scale, trust, and transparency driving significant new business value and insights.

## Service plan availability in regions

| Region | dedicated | enterprise | tenant |
|--------|-----------|------------|--------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ |

## Additional details

### Support components

- CA-DI

### API Hub

- [Overview | SAP Data Intelligence Cloud | SAP API Business Hub](https://api.sap.com/package/SAPDataIntelligenceCloud/overview)

### Discovery Center

- [SAP Discovery Center - SAP Data Intelligence](https://discovery-center.cloud.sap/serviceCatalog/sap-data-intelligence)

### Documentation

- [Documentation](https://help.sap.com/docs/BTP/ca509b7635484070a655738be408da63/1fd349c9b7a34bc58b55e5c7b871e92e.html)
- [Documentation](https://help.sap.com/docs/BTP/ca509b7635484070a655738be408da63/f0d7525dcea04c70b262521f2965ab1e.html)
- [SAP Data Hub Product Page on SAP Help Portal](https://help.sap.com/viewer/product/SAP_DATA_HUB/latest/en-US)
- [Documentation](https://help.sap.com/viewer/product/SAP_DATA_INTELLIGENCE/Cloud)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_DATA_INTELLIGENCE)
- [SAP Leonardo Machine Learning Foundation](https://help.sap.com/viewer/product/SAP_LEONARDO_MACHINE_LEARNING_FOUNDATION/latest/en-US)
- [Documentation](https://launchpad.support.sap.com/#/notes/2820555)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Data%20Intelligence%20Cloud)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Data%20Intelligence%20Cloud)

## Sample configuration of **SAP Data Intelligence Cloud** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-intelligence** by configuring your `usecase.json` file.

### Using the service plan **dedicated** (Dedicated)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-intelligence",
      "plan": "dedicated",
      "parameters" : {
        "adminUsername": null,
        "adminPassword": null,
        "minNodes": null,
        "maxNodes": null,
        "vpcCIDR": null,
        "hibernationSchedules": null
      }
    }
  ]
}
```

### Using the service plan **enterprise**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-intelligence",
      "plan": "enterprise",
      "parameters" : {
        "adminUsername": null,
        "adminPassword": null,
        "minNodes": null,
        "maxNodes": null,
        "vpcCIDR": null,
        "hibernationSchedules": null
      }
    }
  ]
}
```

### Using the service plan **tenant** (Tenant)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-intelligence",
      "plan": "tenant",
      "parameters" : {
        "clusterName": null,
        "tenantName": null,
        "adminUsername": null,
        "adminPassword": null,
        "resourceQuotas": null
      }
    }
  ]
}
```
