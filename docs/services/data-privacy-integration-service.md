# data-privacy-integration-service (SAP Data Privacy Integration)

Data Privacy Integration (DPI) is a service that supports applications realize their data privacy functions i.e Business Purpose Management ( Ensure Data is processed in a compliant manner based on valid Business Purpose ), Data Deletion and Retrieval of personal data. Applications that are part of an end to end business process can integrate with DPI to provide a centralized management of data privacy.

## Service plan availability in regions

| Region | application | free |
|--------|-------------|------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap21** | | ✅ |
|  **br10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **jp20** | | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | | ✅ |

## Additional details

### Support components

- LOD-GDP-IL

### API Hub

- [Overview | SAP Data Privacy Integration - Application Repository | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationApplicationRepository/overview)
- [Overview | SAP Data Privacy Integration - Business Context Management | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationBusinessContext/overview)
- [Overview | SAP Data Privacy Integration - Data Deletion | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationDeletion/overview)
- [Overview | SAP Data Privacy Integration - Information Retrieval | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationInformation/overview)

### Blog

- [Blog Data Privacy Integration](https://blogs.sap.com/2020/09/16/manage-business-purpose-and-data-privacy-for-your-applications-using-sap-cloud-platform-data-privacy-integration/)

### Discovery Center

- [SAP Discovery Center - Data Privacy Integration](https://discovery-center.cloud.sap/serviceCatalog/data-privacy-integration)

### Documentation

- [API Documentation](https://api.sap.com/search?searchterm=DPI)
- [Feature Scope Description](https://help.sap.com/doc/070f9c7b0b14489c93d39e54798e5409/)
- [Documentation](https://help.sap.com/docs/DATA_PRIVACY_INTEGRATION)
- [Documentation](https://help.sap.com/docs/DATA_PRIVACY_INTEGRATION/c829f95e3a3a43ddb958782fb3bf61e2/3538bed426ff405fb68296575f53def4.html)
- [Documentation](https://help.sap.com/docs/DATA_PRIVACY_INTEGRATION/c829f95e3a3a43ddb958782fb3bf61e2/91954b1f5fee4039893300762ff51040.html)
- [What is Data Privacy Integration](https://help.sap.com/viewer/3916a64ef0594fa0b50b47708f4a5c41/Cloud/en-US)
- [Initial Setup](https://help.sap.com/docs/BTP/3916a64ef0594fa0b50b47708f4a5c41/83de644c472c47b7af42c226618a461f.html)
- [What's New](https://help.sap.com/viewer/57390899c7b140ad958a20b0ebbd461a/Cloud/en-US)
- [Documentation](https://help.sap.com/docs/BTP/c829f95e3a3a43ddb958782fb3bf61e2/9cd4d0166681448899a6df34cc60f57f.html)
- [End-User Information](https://help.sap.com/docs/BTP/c829f95e3a3a43ddb958782fb3bf61e2/a360cc35b40946139300990c4cdacad8.html)
- [Documentation](https://help.sap.com/viewer/product/DATA_PRIV_INTEGRATION_OD/SHIP/en-US)

### External

- [Data Privacy Integration Demo Video](https://www.youtube.com/embed/tms6_AEy2q8)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Data%20Privacy%20Integration)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Data%20Privacy%20Integration)

### Support

- [Support](https://help.sap.com/viewer/313a456d8f6c47289945699fbf5ab0c6/DEV/en-US)

## Sample configuration of **SAP Data Privacy Integration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-privacy-integration-service** by configuring your `usecase.json` file.

### Using the service plan **application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-privacy-integration-service",
      "plan": "application"
    }
  ]
}
```

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "data-privacy-integration-service",
      "plan": "free"
    }
  ]
}
```
