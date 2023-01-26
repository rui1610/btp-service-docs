# procurement-service (Guided Buying)

Guided Buying allows you to integrate procurement solutions with SAP S/4HANA Cloud.

## Service plan availability in regions

| Region | apiaccess |
|--------|-----------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/GUIDED_BUYING)
- [Documentation](https://help.sap.com/docs/Guided%20Buying)

### Support

- [Support](https://help.sap.com/docs/GUIDED_BUYING/662c2bd15b5940cbaf249c814bedad91/8369e2f6dbbc44f8bfe72e69662db00c.html)

## Sample configuration of **Guided Buying** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **procurement-service** by configuring your `usecase.json` file.

### Using the service plan **apiaccess** (API Access)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "procurement-service",
      "plan": "apiaccess"
    }
  ]
}
```
