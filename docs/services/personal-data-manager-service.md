# personal-data-manager-service (SAP Personal Data Manager)

SAP Personal Data Manager provides the capability to generate reports showing the personal data stored in an application point of view with the help of a CSR. The reports can be generated and exported either in machine readable form (JSON) or human readable form (PDF). Data subjects can request the correction and deletion of personal data that is stored in an application point of view.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | |

## Additional details

### Support components

- LOD-CBS-GDP

### Discovery Center

- [SAP Discovery Center - Personal Data Manager](https://discovery-center.cloud.sap/serviceCatalog/personal-data-manager)

### Documentation

- [Documentation](https://help.sap.com/docs/PERSONAL_DATA_MANAGER)
- [What's New](https://help.sap.com/docs/PERSONAL_DATA_MANAGER/1e4f89a3d9dc473b842e7d35b42143de/e66e5036be7c4583b5c4cf1052e53841.html)
- [Feature Scope Description](https://help.sap.com/docs/PERSONAL_DATA_MANAGER/ee7c0959f5c047fc860e3e52d5f2bd0f/0062c2e06add4f23bfa86723044c416c.html)
- [What is Personal Data Manager](https://help.sap.com/viewer/620a3ea6aaf64610accdd05cca9e3de2/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/620a3ea6aaf64610accdd05cca9e3de2/SHIP/en-US/392fff93d1de4d168d320010ddc3b803.html)
- [User Guide](https://help.sap.com/viewer/b43057c4bb5f4e02a1913798bb8693d0/Cloud/en-US)

### External

- [SAP Business Technology Platform Personal Data Manager](https://www.youtube.com/embed/CJmG-Xu0jzA)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Personal%20Data%20Manager)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Personal%20Data%20Manager)

## Sample configuration of **SAP Personal Data Manager** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **personal-data-manager-service** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "personal-data-manager-service",
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
      "name": "personal-data-manager-service",
      "plan": "standard"
    }
  ]
}
```
