# privatelink (SAP Private Link service)

SAP Private Link service establishes a private connection between selected SAP BTP services and selected services in your own IaaS provider accounts.

## Service plan availability in regions

| Region | beta | standard |
|--------|------|----------|
|  **ap20** | | ✅ |
|  **ap21** | | ✅ |
|  **eu10** | ✅ | |
|  **eu20** | | ✅ |
|  **jp20** | | ✅ |
|  **us10** | ✅ | |
|  **us20** | | ✅ |
|  **us21** | | ✅ |

## Additional details

### Support components

- BC-CP-PRIVATELINK

### Discovery Center

- [SAP Discovery Center - Private Link Service](https://discovery-center.cloud.sap/serviceCatalog/private-link-service)

### Documentation

- [Help Portal Product Page](https://help.sap.com/products/PRIVATE_LINK)
- [What is SAP Private Link Service?](https://help.sap.com/products/PRIVATE_LINK/42acd88cb4134ba2a7d3e0e62c9fe6cf/3eb3bc7aa5db4b5da9dcdbf8ee478e52.html)
- [What's New](https://help.sap.com/products/PRIVATE_LINK/42acd88cb4134ba2a7d3e0e62c9fe6cf/61fa6a04b3a645e28dde020cc319a6df.html)
- [Initial Setup](https://help.sap.com/products/PRIVATE_LINK/42acd88cb4134ba2a7d3e0e62c9fe6cf/f2dce1d43acb4771beee7304b464041e.html)
- [Documentation](https://help.sap.com/viewer/product/PRIVATE_LINK/CLOUD/en-US)
- [Documentation](https://support.sap.com/en/index.html)

### Onboarding

- [Tutorial: Onboarding](https://developers.sap.com/tutorials/private-link-onboarding.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Private%20Link%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Private%20Link%20service)

### Tutorial

- [Tutorial: Connect SAP Private Link Service to Microsoft Azure Private Link Service](https://developers.sap.com/tutorials/private-link-microsoft-azure.html)

## Sample configuration of **SAP Private Link service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **privatelink** by configuring your `usecase.json` file.

### Using the service plan **beta**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "privatelink",
      "plan": "beta",
      "parameters" : {
        "desiredAZs": 3,
        "policyDocument": null,
        "serviceName": null
      }
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
      "name": "privatelink",
      "plan": "standard",
      "parameters" : {
        "cosmosDb": null,
        "requestMessage": null,
        "resourceId": null,
        "subResource": null
      }
    }
  ]
}
```
