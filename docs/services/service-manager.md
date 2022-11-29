# service-manager (Service Manager)

SAP Service Manager service allows you to consume platform services in any connected runtime environment, track service instances creation, and share services and service instances between different environments.

## Service plan availability in regions

| Region | container | service-operator-access | subaccount-admin | subaccount-audit |
|--------|-----------|-------------------------|------------------|------------------|
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
### Blog

- [Experience the New Way of Consuming and Managing Services on SAP BTP](https://blogs.sap.com/2020/09/14/experience-the-new-way-of-consuming-and-managing-services-on-sap-cloud-platform/)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/service-manager)
- [SAP Discovery Center - Service Manager](https://discovery-center.cloud.sap/serviceCatalog/service-manager)

### Documentation

- [API Documentation](https://api.sap.com/api/APIServiceManagment/resource)
- [Feature Scope Description](https://help.sap.com/doc/f9809732e25740c3abd6158a57b8144e/)
- [Documentation](https://help.sap.com/docs/BTP/09cc82baadc542a688176dce601398de/0ccebd7cec24411dacd5ad17799534e0.html)
- [Documentation](https://help.sap.com/docs/BTP/09cc82baadc542a688176dce601398de/1ca5bbeac19340ce959e82b51b2fde1e.html)
- [What is SAP Service Manager](https://help.sap.com/docs/BTP/09cc82baadc542a688176dce601398de/3a27b85a47fc4dff99184dd5bf181e14.html)
- [What's New](https://help.sap.com/docs/BTP/09cc82baadc542a688176dce601398de/c9d5c050a067476f896a631e7414e2c9.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/f13b6c63eef341bc8b7d25b352401c92.html)
- [SAP Service Manager Product Page](https://help.sap.com/docs/SERVICEMANAGEMENT)

### External

- [External](https://discovery-center.cloud.sap/serviceCatalog/service-management)
- [External](https://operatorhub.io/operator/sap-btp-operator)

## Sample configuration of **Service Manager** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **service-manager** by configuring your `usecase.json` file.

### Using the service plan **container**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-manager",
      "plan": "container"
    }
  ]
}
```

### Using the service plan **service-operator-access**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-manager",
      "plan": "service-operator-access"
    }
  ]
}
```

### Using the service plan **subaccount-admin**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-manager",
      "plan": "subaccount-admin"
    }
  ]
}
```

### Using the service plan **subaccount-audit**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-manager",
      "plan": "subaccount-audit"
    }
  ]
}
```
