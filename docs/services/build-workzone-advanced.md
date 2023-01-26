# build-workzone-advanced (SAP Build Work Zone, advanced edition)

Centralizes access to relevant business applications, processes, information, and communication in a unified entry point that users can access from any device. Note: SAP Work Zone was recently renamed to SAP Build Work Zone, advanced edition.

## Service plan availability in regions

| Region | advanced | standard |
|--------|----------|----------|
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
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- EP-WZ-COR

### Discovery Center

- [SAP Discovery Center - SAP Build Work Zone, advanced edition](https://discovery-center.cloud.sap/serviceCatalog/sap-build-work-zone-advanced-edition)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-work-zone)

### Documentation

- [API Documentation](https://jam2.sapjam.com/work_zone/ODataDocs/ui)
- [Feature Scope Description](https://help.sap.com/doc/38609c8ddb7c418ba864e9ded377f1e8/)
- [What is SAP Build Work Zone, advanced edition?](https://help.sap.com/docs/BTP/b03c84105ff74f809631e494bd612e83/5c0103b130de411fb2a4b5416e36d767.html)
- [Onboarding](https://help.sap.com/docs/BTP/b03c84105ff74f809631e494bd612e83/f8c6eab5b9c8437f9367271863ac90eb.html)
- [Help Portal Product Page](https://help.sap.com/docs/WZ)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Build%20Work%20Zone%2C%20advanced%20edition)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Build%20Work%20Zone%2C%20advanced%20edition)

### Support

- [Creating Support Requests](https://help.sap.com/docs/BTP/b03c84105ff74f809631e494bd612e83/37b79483b56c4f088ce01f1d9f444459.html)

## Sample configuration of **SAP Build Work Zone, advanced edition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **build-workzone-advanced** by configuring your `usecase.json` file.

### Using the service plan **advanced**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "build-workzone-advanced",
      "plan": "advanced"
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
      "name": "build-workzone-advanced",
      "plan": "standard"
    }
  ]
}
```
