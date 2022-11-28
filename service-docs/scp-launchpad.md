# scp-launchpad (Launchpad Service)

SAP Launchpad service provides users with a central point of access to applications from different sources. Note: this service is being renamed to SAP Build Work Zone, standard edition in January 2023.

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
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- EP-CPP-CF-LND

### API Hub

- [Overview | SAP Cloud Portal Service | SAP API Business Hub](https://api.sap.com/package/SAPCLOUDPLATFORMPORTAL/overview)

### Discovery Center

- [SAP Discovery Center - Launchpad Service](https://discovery-center.cloud.sap/serviceCatalog/launchpad-service)

### Documentation

- [Fiori Design Guidelines](https://experience.sap.com/fiori-design-web/launchpad/)
- [SAP Fiori Deployment Options and System Landscape Recommendations](https://www.sap.com/documents/2018/02/f0148939-f27c-0010-82c7-eda71af511fa.html)
- [Establish a central point of access with SAP Launchpad service](https://www.sap.com/documents/2020/09/1a5b0483-ad7d-0010-87a3-c30de2ffd8ff.html)
- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Launchpad)
- [Feature Scope Description](https://help.sap.com/doc/eb57eb0ef530411093f071d5d7b20b0a/)
- [Documentation](https://help.sap.com/viewer/8422cb487c2146999a2a7dab9cc85cf7/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/8c8e1958338140699bd4811b37b82ece/Cloud/en-US)
- [What is SAP Launchpad service](https://help.sap.com/docs/BTP/8c8e1958338140699bd4811b37b82ece/9db48fa44f7e4c62a01bc74c82e74e07.html)
- [Initial Setup](https://help.sap.com/docs/BTP/8c8e1958338140699bd4811b37b82ece/fd79b232967545569d1ae4d8f691016b.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/Launchpad_Service/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/product/Portal_Service/1.0/en-US)
- [Documentation](https://help.sap.com/docs/WZ)

### External

- [Introducing the SAP Launchpad Service](https://www.youtube.com/embed/5mClyrQVYLk)

### Tutorial

- [Trial Starter Scenario: Deliver Your First SAP Fiori Launchpad Site](https://developers.sap.com/mission.cp-starter-digitalexp-portal.html)

## Sample configuration of **Launchpad Service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **scp-launchpad** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "scp-launchpad",
      "plan": "standard"
    }
  ]
}
```
