# feature-flags-dashboard (SAP Feature Flags service)

View and manage Feature Flags Service instances. Get information about flags status, usage and history. Also perform tasks, such as enabling, disabling, adding and removing flags.

## Service plan availability in regions

| Region | dashboard |
|--------|-----------|
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
### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Feature%20Flags%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Feature%20Flags%20service)

## Sample configuration of **SAP Feature Flags service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **feature-flags-dashboard** by configuring your `usecase.json` file.

### Using the service plan **dashboard** (Dashboard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "feature-flags-dashboard",
      "plan": "dashboard"
    }
  ]
}
```
