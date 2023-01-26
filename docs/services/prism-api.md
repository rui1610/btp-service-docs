# prism-api (procurement data warehouse API)

Provides access to procurement data warehouse API.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |

## Additional details

### Support components

- BNS-ARI-PRI

## Sample configuration of **procurement data warehouse API** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **prism-api** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "prism-api",
      "plan": "default"
    }
  ]
}
```
