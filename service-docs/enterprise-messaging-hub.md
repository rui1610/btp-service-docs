# enterprise-messaging-hub (SAP Event Mesh)

The SAP Event Mesh service decouples communication and allows for event-driven business processes.

## Service plan availability in regions

| Region | standard |
|--------|----------|
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
### Documentation

- [Documentation](https://help.sap.com/docs/SAP_ENTERPRISE_MESSAGING)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Event%20Mesh)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Event%20Mesh)

## Sample configuration of **SAP Event Mesh** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **enterprise-messaging-hub** by configuring your `usecase.json` file.

### Using the service plan **standard** (Event Mesh Hub)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "enterprise-messaging-hub",
      "plan": "standard"
    }
  ]
}
```
