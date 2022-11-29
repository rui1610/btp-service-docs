# MDMBusinessPartnerService (SAP Master Data service for business partners)

SAP Business Partner Service

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Master Data Service for Business Partners | SAP API Business Hub](https://api.sap.com/package/SCPMDBPServices/overview)

### Blog

- [Blog: SAP Master Data service for business partners Release 1.5](https://blogs.sap.com/2020/03/03/sap-cloud-platform-master-data-for-business-partners-release-1.5/)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/1ae4c02ef01f474099ea7e91ff74c27b/latest/en-US/loiof17c712f221a46caac6281d69810365e.pdf)
- [What's New](https://help.sap.com/viewer/3b787e14f62047b0ab9ebc3fa5772be9/latest/en-US)
- [What is SAP Master Data service for business partners](https://help.sap.com/viewer/f4bdb01b870142b784aa0668f7877f74/latest/en-US)
- [Documentation](https://help.sap.com/viewer/product/SAP_Cloud_Platform_Master_Data_for_Business_Partners/latest/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAP_Cloud_Platform_Master_Data_for_Business_Partners/latest/en-US?task=discover_task)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Master%20Data%20service%20for%20business%20partners)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Master%20Data%20service%20for%20business%20partners)

## Sample configuration of **SAP Master Data service for business partners** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **MDMBusinessPartnerService** by configuring your `usecase.json` file.

### Using the service plan **default** (SAP Cloud Platform Master Data Management for business partners)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "MDMBusinessPartnerService",
      "plan": "default"
    }
  ]
}
```
