# wums-partner-api-beta (Workspace Utilization)

The Workspace Utilization Management service lets you write sensor measurements to the Workspace Utilization Management API. Sensor platform providers use this API to integrate with the Workspace Utilization Management solution of SAP Cloud for Real Estate.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/SAP_CLOUD_FOR_REAL_ESTATE)

## Sample configuration of **Workspace Utilization** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **wums-partner-api-beta** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "wums-partner-api-beta",
      "plan": "default"
    }
  ]
}
```
