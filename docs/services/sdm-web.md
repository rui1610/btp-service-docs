# sdm-web (Document Management Service, Application Option)

Benefit from the standalone, ready-to-use web application of SAP Document Management service that provides document management capabilities.

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
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **eu30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-CP-CF-SDM

### Discovery Center

- [SAP Discovery Center - Document Management Service, Application Option](https://discovery-center.cloud.sap/serviceCatalog/document-management-service-application-option)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/4551b91432244b9586798187207100a7/)
- [Onboarding](https://help.sap.com/docs/DOCUMENT_MANAGEMENT/f6e70dd4bffa4b65965b43feed4c9429/636e8820ed3d4887813ea2c2cae47e23.html)
- [Security Guide](https://help.sap.com/docs/DOCUMENT_MANAGEMENT/f6e70dd4bffa4b65965b43feed4c9429/bfbb1cd940f24302bdd9d8f82f660a14.html)
- [Consume Document Management, repository](https://help.sap.com/viewer/DRAFT/f6e70dd4bffa4b65965b43feed4c9429/Cloud/en-US/59e3cb769e4f4487a2417d59d65f8276.html)
- [What is Document Management](https://help.sap.com/viewer/f6e70dd4bffa4b65965b43feed4c9429/Cloud/en-US)
- [Manage Document Management, application](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/24382e5628cf4607816e1120e1db98f2.html)
- [Initial Setup](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/636e8820ed3d4887813ea2c2cae47e23.html)
- [What's New](https://help.sap.com/docs/BTP/f6e70dd4bffa4b65965b43feed4c9429/c54fa8c2b5164dc2ae636e44fe92cacd.html)
- [Documentation](https://help.sap.com/docs/DOCUMENT_MANAGEMENT)

### External

- [Know about Document Management in less than 3 mins](https://www.youtube.com/embed/AwFlRaEmUvo)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/DOCUMENT_MANAGEMENT/f6e70dd4bffa4b65965b43feed4c9429/8a33bf75776849cfa06feecb22aba9d6.html)

## Sample configuration of **Document Management Service, Application Option** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sdm-web** by configuring your `usecase.json` file.

### Using the service plan **standard** (Document Management, application option)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sdm-web",
      "plan": "standard"
    }
  ]
}
```
