# postgresql-db (PostgreSQL on SAP BTP, hyperscaler option)

The PostgreSQL service on SAP BTP provides a way to directly consume the PostgreSQL service provided by the infrastructure providers such as AWS and Azure.

## Service plan availability in regions

| Region | free | premium | standard | storage | storage_ha |
|--------|------|---------|----------|---------|------------|
|  **ap10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap20** | | ✅ | | ✅ | ✅ |
|  **ap21** | | ✅ | | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | | ✅ | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu20** | | ✅ | ✅ | ✅ | ✅ |
|  **eu30** | | ✅ | ✅ | ✅ | ✅ |
|  **in30** | | ✅ | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **jp20** | | ✅ | | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us20** | | ✅ | | ✅ | ✅ |
|  **us21** | | ✅ | | ✅ | ✅ |
|  **us30** | | ✅ | ✅ | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-BSB-POSTGRESQL

### Discovery Center

- [SAP Discovery Center - PostgreSQL, hyperscaler option](https://discovery-center.cloud.sap/serviceCatalog/postgresql-hyperscaler-option)

### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=PostgreSQL&from=2019-01-01)
- [Feature Scope Description](https://help.sap.com/doc/937fff80a94e413681298439b201e5f7/)
- [What is PostgreSQL, hyperscaler option?](https://help.sap.com/viewer/b3fe3621fa4a4ed28d7bbe3d6d88f036/Cloud/en-US)
- [Sizing](https://help.sap.com/docs/BTP/b3fe3621fa4a4ed28d7bbe3d6d88f036/2d999a8d2889419b8a001502351241f2.html)
- [Initial Setup](https://help.sap.com/docs/BTP/b3fe3621fa4a4ed28d7bbe3d6d88f036/410f5d9fe86f4a91a0d4c9ab76b04373.html)
- [Find the Right Guide](https://help.sap.com/viewer/b485ef99ff9e4e778e192037316fd20e/2101/en-US/b00d2e76ea5b43ba9b626711d86d33a1.html)
- [Documentation](https://help.sap.com/docs/BTP/c92112ee69784c3383a0fb8361156a6f/b045b64925a544689dd839266a23c89b.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/PostgreSQL/Cloud/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=PostgreSQL%20on%20SAP%20BTP%2C%20hyperscaler%20option)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=PostgreSQL%20on%20SAP%20BTP%2C%20hyperscaler%20option)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **PostgreSQL on SAP BTP, hyperscaler option** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **postgresql-db** by configuring your `usecase.json` file.

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql-db",
      "plan": "free",
      "parameters" : {
        "engine_version": "12",
        "locale": "en_US"
      }
    }
  ]
}
```

### Using the service plan **premium**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql-db",
      "plan": "premium",
      "parameters" : {
        "audit_log_level": ["ROLE", "DDL"],
        "memory": 8,
        "storage": 5,
        "engine_version": "12",
        "multi_az": true,
        "locale": "en_US",
        "maintenance_window": null
      }
    }
  ]
}
```

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql-db",
      "plan": "standard",
      "parameters" : {
        "audit_log_level": ["ROLE", "DDL"],
        "memory": 2,
        "storage": 5,
        "engine_version": "12",
        "multi_az": true,
        "locale": "en_US",
        "maintenance_window": null
      }
    }
  ]
}
```

### Using the service plan **storage**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql-db",
      "plan": "storage"
    }
  ]
}
```

### Using the service plan **storage_ha**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql-db",
      "plan": "storage_ha"
    }
  ]
}
```
