# redis (Redis on SAP BTP)

Redis on SAP BTP offers an in-memory data structure store that you can use as a cache, database, or message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets, and so on.

## Service plan availability in regions

| Region | large | medium | small | xsmall |
|--------|-------|--------|-------|--------|
|  **ap10** | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | | ✅ | ✅ | ✅ |
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

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Redis&from=2019-05-01)
- [Feature Scope Description](https://help.sap.com/doc/796c683493bb4233906acd22d3c68110/)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/971730b26c93492e980a03c4619f9916.html)
- [What is Redis Service](https://help.sap.com/docs/BTP/d6429ae8d9384822939bf809078d8ff2/8a204294693c4c78a2345eb1a42104da.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/Redis/Cloud/en-US)

### External

- [External](http://redis.io/community)
- [Redis Official Website](https://redis.io/)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/data-storage/redis.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Redis%20on%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Redis%20on%20SAP%20BTP)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Redis on SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **redis** by configuring your `usecase.json` file.

### Using the service plan **large**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "redis",
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
      "name": "redis",
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
      "name": "redis",
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
      "name": "redis",
      "plan": "xsmall"
    }
  ]
}
```
