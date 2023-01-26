# sapappstudio (SAP Business Application Studio)

SAP Business Application Studio is the next generation of SAP Web IDE, offering a modular development environment tailored for efficient development of business applications for the SAP Intelligent Enterprise. It provides pre-configured environments where you can develop, build, test and run using pre-installed runtimes and tools tailored for key scenarios such as: S/4HANA extensions, full stack business applications, Fiori applications and more. It supports quick integration with SAP solutions and services to allow building smarter and more intelligent applications.

## Service plan availability in regions

| Region | free | standard-edition |
|--------|------|------------------|
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
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- CA-BAS

### Discovery Center

- [SAP Discovery Center - Business Application Studio](https://discovery-center.cloud.sap/serviceCatalog/business-application-studio)

### Documentation

- [Initial Setup](https://help.sap.com/docs/BTP/9d1db9835307451daa8c930fbd9ab264/19611ddbe82f4bf2b493283e0ed602e5.html)
- [What is SAP Business Application Studio](https://help.sap.com/docs/BTP/9d1db9835307451daa8c930fbd9ab264/8f46c6e6f86641cc900871c903761fd4.html)
- [What's New](https://help.sap.com/docs/BTP/9d1db9835307451daa8c930fbd9ab264/ed631d4ee2214e9f932b03d40b2c7e41.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAP%20Business%20Application%20Studio/Cloud/en-US)

### External

- [Introduction to SAP Business Application Studio](https://www.youtube.com/embed/ulukOikw53I)

### Learning

- [Building Applications with SAP Cloud Application Programming Model](https://open.sap.com/courses/cp7)
- [SAP Fiori Overview: Design, Develop and Deploy](https://open.sap.com/courses/fiori3)

### Legal

- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Business Application Studio Homepage](https://community.sap.com/topics/business-application-studio)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Business%20Application%20Studio)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Business%20Application%20Studio)

### Support

- [Support](https://help.sap.com/docs/BTP/9d1db9835307451daa8c930fbd9ab264/a3467fe642ce4f6bb36de0a100440602.html)

### Tutorial

- [Tutorials](https://developers.sap.com/tutorial-navigator.html?tag=products:technology-platform/sap-business-application-studio)

## Sample configuration of **SAP Business Application Studio** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sapappstudio** by configuring your `usecase.json` file.

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sapappstudio",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **standard-edition**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sapappstudio",
      "plan": "standard-edition"
    }
  ]
}
```
