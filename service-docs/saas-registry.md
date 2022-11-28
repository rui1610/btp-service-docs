# saas-registry (SAP Software-as-a-Service Provisioning service)

Service for application providers to register multitenant applications and services.

## Service plan availability in regions

| Region | application |
|--------|-------------|
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
### Blog

- [Developing Multitenant Applications on SAP BTP](https://blogs.sap.com/2018/09/17/developing-multitenant-applications-on-sap-cloud-platform-cloud-foundry-environment/)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/saas-provisioning-service?service_plan=application&region=all)
- [SAP Discovery Center - SaaS Provisioning Service](https://discovery-center.cloud.sap/serviceCatalog/saas-provisioning-service)

### Documentation

- [What Is SaaS Provisioning?](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5e8a2b74e4f2442b8257c850ed912f48.html)
- [API Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/ed08c7dcb35d4082936c045e7d7b3ecd.html)

### External

- [Using SaaS Provisioning Service to develop a SaaS Multitenant Application on SAP BTP in the Cloud Foundry Environment-Hello World](https://github.com/SAP-samples/cloud-cf-multitenant-saas-provisioning-sample)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Software-as-a-Service%20Provisioning%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Software-as-a-Service%20Provisioning%20service)

## Sample configuration of **SAP Software-as-a-Service Provisioning service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **saas-registry** by configuring your `usecase.json` file.

### Using the service plan **application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "saas-registry",
      "plan": "application"
    }
  ]
}
```
