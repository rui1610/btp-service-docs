# apimanagement-devportal (API Management, developer portal)

API Management, developer portal service simplifies sharing managed APIs and enables collaborations with customers, partners, and developers, providing a common platform for application developers to consume APIs. It offers capabilities for onboarding application developers, exploring and testing APIs, and creating and subscribing to applications.This service provides the plan which allows you to access APIs in the developer portal.

## Service plan availability in regions

| Region | devportal-apiaccess |
|--------|---------------------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
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
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/e765066197904519a730c3bca40f28b0.html)
- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_PLATFORM_API_MANAGEMENT)
- [Documentation](https://www.sap.com/india/products/api-management.html#support)

### SAP Community

- [SAP Community](https://help.hana.ondemand.com/apim_od/frameset.htm)

## Sample configuration of **API Management, developer portal** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **apimanagement-devportal** by configuring your `usecase.json` file.

### Using the service plan **devportal-apiaccess**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "apimanagement-devportal",
      "plan": "devportal-apiaccess"
    }
  ]
}
```
