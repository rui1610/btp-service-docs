# SAPWorkZone (SAP Build Work Zone, advanced edition)

Increase the productivity and engagement for your employees as well as interact with partners and customers in a multi-channel digital experience. Note: SAP Work Zone was recently renamed to SAP Build Work Zone, advanced edition.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |

## Additional details

### Support components

- EP-WZ-COR

### Documentation

- [Documentation](https://help.sap.com/docs/WZ)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Build%20Work%20Zone%2C%20advanced%20edition)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Build%20Work%20Zone%2C%20advanced%20edition)

## Sample configuration of **SAP Build Work Zone, advanced edition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **SAPWorkZone** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "SAPWorkZone",
      "plan": "standard"
    }
  ]
}
```
