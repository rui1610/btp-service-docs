# data-privacy-integration-application (SAP Data Privacy Integration)

Data Privacy Integration (DPI) is a service that supports applications realize their data privacy functions i.e Business Purpose Management ( Ensure Data is processed in a compliant manner based on valid Business Purpose ), Data Deletion and Retrieval of personal data. Applications that are part of an end to end business process can integrate with DPI to provide a centralized management of data privacy.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap21** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Data Privacy Integration - Application Repository | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationApplicationRepository/overview)
- [Overview | SAP Data Privacy Integration - Business Context Management | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationBusinessContext/overview)
- [Overview | SAP Data Privacy Integration - Data Deletion | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationDeletion/overview)
- [Overview | SAP Data Privacy Integration - Information Retrieval | SAP API Business Hub](https://api.sap.com/package/DataPrivacyIntegrationInformation/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/data-privacy-integration)

### Documentation

- [Documentation](https://help.sap.com/docs/DATA_PRIVACY_INTEGRATION)
- [Documentation](https://help.sap.com/docs/DATA_PRIVACY_INTEGRATION/c829f95e3a3a43ddb958782fb3bf61e2/3538bed426ff405fb68296575f53def4.html)
- [Documentation](https://help.sap.com/docs/DATA_PRIVACY_INTEGRATION/c829f95e3a3a43ddb958782fb3bf61e2/91954b1f5fee4039893300762ff51040.html)
- [Documentation](https://help.sap.com/docs/BTP/c829f95e3a3a43ddb958782fb3bf61e2/9cd4d0166681448899a6df34cc60f57f.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Data%20Privacy%20Integration)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Data%20Privacy%20Integration)

### Support

- [Support](https://help.sap.com/viewer/313a456d8f6c47289945699fbf5ab0c6/DEV/en-US)

## Sample configuration of **SAP Data Privacy Integration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **data-privacy-integration-application** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "data-privacy-integration-application",
      "plan": "default"
    }
  ]
}
```
