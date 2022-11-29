# hana-tenant-db (SAP HANA Tenant Database)

SAP HANA Tenant Database

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap21** | ✅ |
|  **eu20** | ✅ |
|  **jp20** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)
- [Documentation](https://help.sap.com/docs/BTP/a36ee1aa073e4e8e840573fb30a72d95/1e9a6cb47e1b44f990a917b4bf8c2e19.html)

## Sample configuration of **SAP HANA Tenant Database** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hana-tenant-db** by configuring your `usecase.json` file.

### Using the service plan **standard** (SAP HANA Tenant Database)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-tenant-db",
      "plan": "standard"
    }
  ]
}
```
