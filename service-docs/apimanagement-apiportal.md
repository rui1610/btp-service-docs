# apimanagement-apiportal (API Management, API portal)

API Management, API portal service drives innovation in modern business models. Based on APIs and digital assets, the service facilitates unified access from new channels and diverse user interfaces. This is possible by enabling developer communities to connect to your enterprise information and processes securely. Here, the access to backend services and complex landscapes are simplified with easy to consume APIs while protecting your systems from threats and overloaded access.

## Service plan availability in regions

| Region | apim-as-route-service | apiportal-apiaccess | on-premise-connectivity |
|--------|-----------------------|---------------------|-------------------------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ |
|  **in30** | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/e765066197904519a730c3bca40f28b0.html)
- [Documentation](https://help.sap.com/viewer/product/SAP_CLOUD_PLATFORM_API_MANAGEMENT)
- [Documentation](https://www.sap.com/india/products/api-management.html#support)

### SAP Community

- [SAP Community](https://help.hana.ondemand.com/apim_od/frameset.htm)

### Tool

- [API Portal](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/29c281b4a002404eba44e91c6fad0d34.html)

## Sample configuration of **API Management, API portal** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **apimanagement-apiportal** by configuring your `usecase.json` file.

### Using the service plan **apim-as-route-service**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "apimanagement-apiportal",
      "plan": "apim-as-route-service"
    }
  ]
}
```

### Using the service plan **apiportal-apiaccess**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "apimanagement-apiportal",
      "plan": "apiportal-apiaccess"
    }
  ]
}
```

### Using the service plan **on-premise-connectivity**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "apimanagement-apiportal",
      "plan": "on-premise-connectivity"
    }
  ]
}
```
