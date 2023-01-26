# build-workzone-standard (SAP Build Work Zone, standard edition)

Provides users with a central point of access to applications from different sources. Note: SAP Launchpad service was recently renamed to SAP Build Work Zone, standard edition.

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

- [Overview | SAP Build Work Zone and SAP Cloud Portal Service | SAP API Business Hub](https://api.sap.com/package/SAPCLOUDPLATFORMPORTAL/overview)

### Discovery Center

- [SAP Discovery Center - SAP Build Work Zone, standard edition](https://discovery-center.cloud.sap/serviceCatalog/sap-build-work-zone-standard-edition)

### Documentation

- [Fiori Design Guidelines](https://experience.sap.com/fiori-design-web/launchpad/)
- [SAP Fiori Deployment Options and System Landscape Recommendations](https://www.sap.com/documents/2018/02/f0148939-f27c-0010-82c7-eda71af511fa.html)
- [Feature Scope Description](https://help.sap.com/doc/eb57eb0ef530411093f071d5d7b20b0a/)
- [Documentation](https://help.sap.com/docs/WZ)
- [Help Portal Product Page](https://help.sap.com/docs/WZ_STD)
- [What's New](https://help.sap.com/docs/WZ_STD/8c8e1958338140699bd4811b37b82ece/2d993e39df354509bf9b4fe71c1a5bd0.html)
- [What is SAP Build Work Zone, standard edition](https://help.sap.com/docs/WZ_STD/8c8e1958338140699bd4811b37b82ece/9db48fa44f7e4c62a01bc74c82e74e07.html)
- [Initial Setup](https://help.sap.com/docs/WZ_STD/8c8e1958338140699bd4811b37b82ece/fd79b232967545569d1ae4d8f691016b.html)
- [Documentation](https://help.sap.com/viewer/8422cb487c2146999a2a7dab9cc85cf7/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/8c8e1958338140699bd4811b37b82ece/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/product/Portal_Service/1.0/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Build%20Work%20Zone%2C%20standard%20edition)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Build%20Work%20Zone%2C%20standard%20edition)

### Tutorial

- [Deliver Your First Business Site Using SAP Build Work Zone, standard edition](https://developers.sap.com/mission.launchpad-cf.html)

## Sample configuration of **SAP Build Work Zone, standard edition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **build-workzone-standard** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "build-workzone-standard",
      "plan": "standard"
    }
  ]
}
```
