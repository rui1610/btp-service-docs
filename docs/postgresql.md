# postgresql (PostgreSQL on SAP BTP)

PostgreSQL on SAP BTP offers an object-relational database management system with many advanced features, such as user-defined types, table inheritance, foreign key referential integrity, Multiversion Concurrency Control (MVCC), and so on.

## Service plan availability in regions

| Region | large | medium | small | xsmall | xxsmall |
|--------|-------|--------|-------|--------|---------|
|  **ap10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **in30** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=PostgreSQL&from=2019-03-01)
- [Feature Scope Description](https://help.sap.com/doc/937fff80a94e413681298439b201e5f7/)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/314e0968334d45ab855924497759671b.html)
- [What is PostgreSQL?](https://help.sap.com/docs/BTP/6be7ed96ddeb4e158c2107c434142545/1cb29d5c1f714e71a79379c6b7482428.html)
- [FAQ](https://help.sap.com/docs/BTP/6be7ed96ddeb4e158c2107c434142545/6a5414a865cc48369bbc89da91133243.html)
- [Export Data from PostgreSQL Service Instance](https://help.sap.com/docs/BTP/6be7ed96ddeb4e158c2107c434142545/7547876937594510aa13cfaf693d07b1.html)
- [Initial Setup](https://help.sap.com/docs/BTP/6be7ed96ddeb4e158c2107c434142545/f6baac64701e49da9069c74c6359eba8.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/PostgreSQL/Cloud/en-US)

### External

- [PostgreSQL Official Website](https://www.postgresql.org/)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/data-storage/postgresql.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=PostgreSQL%20on%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=PostgreSQL%20on%20SAP%20BTP)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **PostgreSQL on SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **postgresql** by configuring your `usecase.json` file.

### Using the service plan **large**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql",
      "plan": "large"
    }
  ]
}
```

### Using the service plan **medium**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql",
      "plan": "medium"
    }
  ]
}
```

### Using the service plan **small**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql",
      "plan": "small"
    }
  ]
}
```

### Using the service plan **xsmall**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql",
      "plan": "xsmall"
    }
  ]
}
```

### Using the service plan **xxsmall**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "postgresql",
      "plan": "xxsmall"
    }
  ]
}
```
