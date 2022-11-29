# redis-cache (Redis on SAP BTP, hyperscaler option)

The Redis service on SAP BTP provides a way to directly consume the Redis cache service provided by the Infrastructure providers such as AWS and Azure.

## Service plan availability in regions

| Region | free | premium | standard |
|--------|------|---------|----------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ |
|  **ch20** | | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ |
|  **eu30** | | ✅ | ✅ |
|  **in30** | | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ |
|  **us30** | | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-BSB-REDIS

### Discovery Center

- [SAP Discovery Center - Redis, hyperscaler option](https://discovery-center.cloud.sap/serviceCatalog/redis-hyperscaler-option)

### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Redis&from=2019-05-01)
- [Feature Scope Description](https://help.sap.com/doc/796c683493bb4233906acd22d3c68110/)
- [What is Redis, Hyperscaler Option?](https://help.sap.com/docs/BTP/082005ec29494234a42af221bc963a67/71399a37ccba45c5b41d35f5ba9490dc.html)
- [Initial Setup](https://help.sap.com/docs/BTP/082005ec29494234a42af221bc963a67/a0a4e36f97694766a574dcb81c6ddf5e.html)
- [Documentation](https://help.sap.com/viewer/ad8f6ea81b714bbb9bf995dd2c2b424e/Cloud/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/Redis/Cloud/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Redis%20on%20SAP%20BTP%2C%20hyperscaler%20option)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Redis%20on%20SAP%20BTP%2C%20hyperscaler%20option)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Redis on SAP BTP, hyperscaler option** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **redis-cache** by configuring your `usecase.json` file.

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "redis-cache",
      "plan": "free",
      "parameters" : {
        "engine_version": "4.0",
        "eviction_policy": "noeviction"
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
      "name": "redis-cache",
      "plan": "premium",
      "parameters" : {
        "memory": 8,
        "engine_version": "4.0",
        "eviction_policy": "noeviction",
        "shard_count": 1,
        "node_count": 3,
        "multi_az": true,
        "maintenance_window": null,
        "notify_keyspace_events": "",
        "cluster_mode": true
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
      "name": "redis-cache",
      "plan": "standard",
      "parameters" : {
        "memory": 2,
        "engine_version": "4.0",
        "eviction_policy": "noeviction",
        "shard_count": 1,
        "node_count": 3,
        "multi_az": true,
        "maintenance_window": null,
        "notify_keyspace_events": "",
        "cluster_mode": true
      }
    }
  ]
}
```
