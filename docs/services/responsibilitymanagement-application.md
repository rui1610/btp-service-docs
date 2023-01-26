# responsibilitymanagement-application (Responsibility Management Service)

As we move toward an intelligent enterprise, intelligent systems need to determine agents who are responsible for business processes and objects, and automatically notify them. It is essential to define and manage these responsibilities for various contexts and retrieve responsible agents who can respond to tasks and activities.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **eu11** | ✅ |

## Additional details

### Support components

- CA-GTF-RM-SCP

### Documentation

- [Documentation](https://help.sap.com/viewer/product/RESPONSIBILITY_MANAGEMENT_SCP/SHIP/en-US)

## Sample configuration of **Responsibility Management Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **responsibilitymanagement-application** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "responsibilitymanagement-application",
      "plan": "standard"
    }
  ]
}
```
