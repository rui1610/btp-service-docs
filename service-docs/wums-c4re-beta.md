# wums-c4re-beta (Workspace Utilization)

The Workspace Utilization Management application lets you assign sensors to workplaces and spaces. These sensors measure how your workspaces are used. The Workspace Utilization Management application integrates with SAP Cloud for Real Estate and SAP Analytics Cloud to analyze, manage, and optimize your workspaces.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_FOR_REAL_ESTATE/2/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Workspace%20Utilization)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Workspace%20Utilization)

## Sample configuration of **Workspace Utilization** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **wums-c4re-beta** by configuring your `usecase.json` file.

### Using the service plan **default** (SAP Cloud for Real Estate Workspace Utilization Management (BETA))

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "wums-c4re-beta",
      "plan": "default"
    }
  ]
}
```
