# dqmmicroui (Data Quality Services UI)

Manage settings and field mappings using configurations. View number of transactions performed over a spefici time period.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details

### Support components

- EIM-DQM-SVS

### Documentation

- [Documentation](https://help.sap.com/docs/BTP/d95546360fea44988eb614718ff7e959/8bb7b22e6d4c40b5bfdaef86f59e2036.html)

### Legal

- [License Terms](https://www.sap.com/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?tag=agreements:product-use-support-terms/on-premise-software/software-use-rights/)

## Sample configuration of **Data Quality Services UI** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dqmmicroui** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "dqmmicroui",
      "plan": "standard"
    }
  ]
}
```
