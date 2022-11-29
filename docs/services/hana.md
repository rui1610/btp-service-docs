# hana (SAP HANA Schemas & HDI Containers)

Use the SAP HANA schemas & HDI containers service to create service instances on SAP HANA databases and bind them to cloud applications. To create schemas and HDI containers, an SAP HANA database must be available in your space. The SAP HANA schemas & HDI containers service is part of the SAP HANA service.

## Service plan availability in regions

| Region | hdi-shared | sbss | schema | securestore |
|--------|------------|------|--------|-------------|
|  **ap10** | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ | ✅ |
|  **in30** | ✅ | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)
- [Documentation](https://help.sap.com/docs/BTP/a36ee1aa073e4e8e840573fb30a72d95/1e9a6cb47e1b44f990a917b4bf8c2e19.html)
- [Documentation](https://help.sap.com/viewer/product/HANA_CLOUD/cloud/en-US)

## Sample configuration of **SAP HANA Schemas & HDI Containers** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hana** by configuring your `usecase.json` file.

### Using the service plan **hdi-shared**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana",
      "plan": "hdi-shared"
    }
  ]
}
```

### Using the service plan **sbss**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana",
      "plan": "sbss"
    }
  ]
}
```

### Using the service plan **schema**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana",
      "plan": "schema"
    }
  ]
}
```

### Using the service plan **securestore**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana",
      "plan": "securestore"
    }
  ]
}
```
