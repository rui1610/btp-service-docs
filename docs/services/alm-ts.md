# alm-ts (SAP Cloud Transport Management)

SAP Cloud Transport Management service lets you manage software deliverables between accounts of different environments (such as Neo and Cloud Foundry), by transporting them across various runtimes. This includes application artifacts as well as their respective application-specific content.

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
|  **ch20** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-LCM-TMS

### API Hub

- [Overview | SAP Cloud Transport Management | SAP API Business Hub](https://api.sap.com/package/TmsForCloudPub/overview)

### Blog

- [Blog](https://blogs.sap.com/?s=transport+management+service)
- [Blogs about SAP Cloud Transport Management](https://blogs.sap.com/?s=cloud+transport+management)

### Discovery Center

- [SAP Discovery Center - Cloud Transport Management](https://discovery-center.cloud.sap/serviceCatalog/cloud-transport-management)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/b5430836c20d4bd8a975cb4d48b4e7a5/)
- [Security](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/51939a49db9749578b7e237139bfd08d.html)
- [SAP Cloud Transport Management](https://help.sap.com/viewer/7f7160ec0d8546c6b3eab72fb5ad6fd8/Cloud/en-US)
- [Initial Setup](https://help.sap.com/docs/BTP/7f7160ec0d8546c6b3eab72fb5ad6fd8/66fd7283c62f48adb23c56fb48c84a60.html)
- [What's New](https://help.sap.com/docs/BTP/7f7160ec0d8546c6b3eab72fb5ad6fd8/85b6ac3c2925448c86bcd04f0da6678e.html)
- [Transport Management](https://help.sap.com/docs/BTP/7f7160ec0d8546c6b3eab72fb5ad6fd8/9ac7880eddb14eeda89b800295bcf242.html)
- [Documentation](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE)

### External

- [SAP Cloud Transport Management - Introduction](https://www.youtube.com/embed/zT4gQJ03WSM)

### Legal

- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Cloud%20Transport%20Management)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Cloud%20Transport%20Management)

## Sample configuration of **SAP Cloud Transport Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **alm-ts** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "alm-ts",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "alm-ts",
      "plan": "standard"
    }
  ]
}
```
