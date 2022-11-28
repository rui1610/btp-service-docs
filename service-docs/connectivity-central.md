# connectivity-central (Connectivity (for scale-out build-out))

Connectivity (for scale-out build-out)

## Service plan availability in regions

| Region | connectivity_proxy |
|--------|--------------------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/34010ace6ac84574a4ad02f5055d3597.html)
- [Documentation](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/e5580c5dbb5710149e53c6013301a9f2.html)

## Sample configuration of **Connectivity (for scale-out build-out)** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **connectivity-central** by configuring your `usecase.json` file.

### Using the service plan **connectivity_proxy** (Pair Connectivity Proxy with SAP CP Connectivity service for establishing secure connections to on-premise systems through SAP Cloud Connector)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "connectivity-central",
      "plan": "connectivity_proxy"
    }
  ]
}
```
