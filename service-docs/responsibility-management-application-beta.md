# responsibility-management-application-beta (SAP Responsibility Management service)

Provides APIs for DetermineAgents using responsibility rules or external APIs(bring your own code) and AgentDeterminationRequest.

## Service plan availability in regions

| Region | beta |
|--------|------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/viewer/product/DRAFT/RESPONSIBILITY_MANAGEMENT/1.0/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Responsibility%20Management%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Responsibility%20Management%20service)

## Sample configuration of **SAP Responsibility Management service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **responsibility-management-application-beta** by configuring your `usecase.json` file.

### Using the service plan **beta** (Beta)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "responsibility-management-application-beta",
      "plan": "beta"
    }
  ]
}
```
