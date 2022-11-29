# sdm (Document Management Service, Integration Option)

Leverage the APIs of SAP Document Management service and build your own document management layer to enable document management capabilities for your business applications. You can also embed the easy-to-use, UI5-based, reusable UI component of Document Management into your application for document management scenarios.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CF-SDM
- BC-CP-CF-SDM-INT

### API Hub

- [Overview | SAP Document Management Service, Integration Option | SAP API Business Hub](https://api.sap.com/package/SAPDocumentManagementServiceIntegrationOption/overview)
- [Overview | SAP Document Management Service, Integration Option - Content Management Interoperability Services | SAP API Business Hub](https://api.sap.com/package/SAPDocumentManagementServiceIntegrationOptionCMISAPI/overview)

### Discovery Center

- [SAP Discovery Center - Document Management Service, Integration Option](https://discovery-center.cloud.sap/serviceCatalog/document-management-service-integration-option)

### Documentation

- [API Documentation](https://api.sap.com/package/SAPDocumentManagementServiceIntegrationOption/rest)
- [Feature Scope Description](https://help.sap.com/doc/4551b91432244b9586798187207100a7/)
- [What is Document Management](https://help.sap.com/viewer/f6e70dd4bffa4b65965b43feed4c9429/Cloud/en-US)
- [Manage Document Management, integration](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/24382e5628cf4607816e1120e1db98f2.html)
- [Documentation](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/27e742e062924d72a9f1cb94a8c8346c.html)
- [Initial Setup](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/bc0f1ec7d5374b968e0b0de6db470c94.html)
- [What's New](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/c54fa8c2b5164dc2ae636e44fe92cacd.html)
- [Consume Document Management, repository](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/d30200e0993a457888db2786d4bb5cd9.html)
- [Documentation](https://help.sap.com/docs/DOCUMENT_MANAGEMENT)

### External

- [Know about Document Management in less than 3 minutes](https://www.youtube.com/embed/AwFlRaEmUvo)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

## Sample configuration of **Document Management Service, Integration Option** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sdm** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sdm",
      "plan": "free"
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
      "name": "sdm",
      "plan": "standard"
    }
  ]
}
```
