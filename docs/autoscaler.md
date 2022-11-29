# autoscaler (Application Autoscaler)

The Application Autoscaler lets you automatically increase or decrease the number of application instances based on a policy you define.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **ch20** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **eu30** | ✅ |
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-CP-CF-AUTOSCALE

### API Hub

- [Overview | Application Autoscaler | SAP API Business Hub](https://api.sap.com/package/CFApplicationAutoscaler/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/application-autoscaler)
- [SAP Discovery Center - Application Autoscaler](https://discovery-center.cloud.sap/serviceCatalog/application-autoscaler)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/0a842f0cc688413d9e8dd8fb24e85232/)
- [What is Application Autoscaler](https://help.sap.com/viewer/7472b7d13d5d4862b2b06a730a2df086/Cloud/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/Application_Autoscaler/Cloud/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Application%20Autoscaler)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Application%20Autoscaler)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Application Autoscaler** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **autoscaler** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "autoscaler",
      "plan": "standard"
    }
  ]
}
```
