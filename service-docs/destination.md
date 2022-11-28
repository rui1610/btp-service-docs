# destination (SAP Destination service)

The Destination service lets you retrieve the backend destination details you need to configure applications in the Cloud Foundry environment.

## Service plan availability in regions

| Region | lite |
|--------|------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **ch20** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **eu30** | ✅ |
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-CP-DEST

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/destination)
- [SAP Discovery Center - Destination](https://discovery-center.cloud.sap/serviceCatalog/destination)

### Documentation

- [Documentation](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/34010ace6ac84574a4ad02f5055d3597.html)
- [Documentation](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/e5580c5dbb5710149e53c6013301a9f2.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Destination%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Destination%20service)

## Sample configuration of **SAP Destination service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **destination** by configuring your `usecase.json` file.

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "destination",
      "plan": "lite"
    }
  ]
}
```
