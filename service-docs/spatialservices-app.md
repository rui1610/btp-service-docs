# spatialservices-app (SAP HANA spatial services)

HANA Spatial Services

## Service plan availability in regions

| Region | professional | starter |
|--------|--------------|---------|
|  **eu10** | ✅ | ✅ |

## Additional details
### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20HANA%20spatial%20services)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20HANA%20spatial%20services)

## Sample configuration of **SAP HANA spatial services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **spatialservices-app** by configuring your `usecase.json` file.

### Using the service plan **professional** (HANA Spatial Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "spatialservices-app",
      "plan": "professional"
    }
  ]
}
```

### Using the service plan **starter** (HANA Spatial Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "spatialservices-app",
      "plan": "starter"
    }
  ]
}
```
