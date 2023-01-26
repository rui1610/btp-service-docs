# extension-center (Extension Center)

Allows you to create, manage, configure extensions on SAP Business Technology Platform

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |

## Additional details

### Support components

- BC-CP-XF-SRT

### Blog

- [Blogs](https://blogs.sap.com/?s=serverless+runtime)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/serverless-runtime)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/5e8107bf49684962b897217040398007/)
- [What's New](https://help.sap.com/docs/BTP/bf7b2ff68518427c85b30ac3184ad215/61834baadfcc45a2b4bf6675b518e6f9.html)
- [What Is SAP BTP, Serverless Runtime](https://help.sap.com/docs/BTP/bf7b2ff68518427c85b30ac3184ad215/7b8cc2b0e8d141d6aa37c7dff4d70b82.html)
- [Initial Setup](https://help.sap.com/docs/BTP/bf7b2ff68518427c85b30ac3184ad215/80f67e476a8447378a72b3fcfbce8f3e.html)
- [Product Page](https://help.sap.com/docs/XF_SERVERLESS_RUNTIME)

### External

- [Overview](https://www.youtube.com/embed/hUx3Miq29XQ)

### Tool

- [Extension Center](https://help.sap.com/docs/BTP/bf7b2ff68518427c85b30ac3184ad215/6f6b050980384b18bb0a0bae5a9b2daa.html)
- [SAP Business Technology Platform Serverless Runtime CLI](https://help.sap.com/docs/BTP/bf7b2ff68518427c85b30ac3184ad215/8400ccd0efc94c3096a9468c1e5f63ce.html)

## Sample configuration of **Extension Center** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **extension-center** by configuring your `usecase.json` file.

### Using the service plan **standard** (Extension Center)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "extension-center",
      "plan": "standard"
    }
  ]
}
```
