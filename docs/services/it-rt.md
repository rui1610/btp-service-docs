# it-rt (Process Integration Runtime)

Provides access to SAP Business Technology Platform Integration runtime (integration flows) and APIs.

## Service plan availability in regions

| Region | api | integration-flow |
|--------|-----|------------------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **ch20** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/SAP_INTEGRATION_SUITE/51ab953548be4459bfe8539ecaeee98d/19af5e205fe14af6a4f8a9fd80d4dc92.html)
- [Documentation](https://help.sap.com/docs/SAP_INTEGRATION_SUITE/51ab953548be4459bfe8539ecaeee98d/6abc8746df294fe4ac5877e39683dee6.html)

### Support

- [Support](https://cloudintegration.hana.ondemand.com/PI/help)

### Tool

- [SAP Business Technology Platform Integration Web UI](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/9af2f05c7eb04457aee5906fd8553e00.html)

## Sample configuration of **Process Integration Runtime** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **it-rt** by configuring your `usecase.json` file.

### Using the service plan **api**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "it-rt",
      "plan": "api",
      "parameters" : {
        "roles": null,
        "grant-types": ["client_credentials"],
        "redirect-uris": []
      }
    }
  ]
}
```

### Using the service plan **integration-flow**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "it-rt",
      "plan": "integration-flow",
      "parameters" : {
        "roles": ["ESBMessaging.send"],
        "grant-types": ["client_credentials"],
        "redirect-uris": []
      }
    }
  ]
}
```
