# sapappgyver (SAP AppGyver)

Low-code / no-code tools from SAP that accelerate SAP business applications development.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details

### Support components

- CA-LCA

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/sap-appgyver)

### Documentation

- [Documentation](https://help.sap.com/viewer/6a5fc562f6e2402aa84b0416614a05fc/Dev/en-US)

### Tutorial

- [Tutorials and reference documentation](https://docs.appgyver.com)

## Sample configuration of **SAP AppGyver** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sapappgyver** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sapappgyver",
      "plan": "standard"
    }
  ]
}
```
