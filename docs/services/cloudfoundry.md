# cloudfoundry (SAP BTP, Cloud Foundry runtime)

The SAP BTP, Cloud Foundry runtime lets you develop polyglot cloud-native applications and run them on the SAP BTP Cloud Foundry environment.

## Service plan availability in regions

| Region | free |
|--------|------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **ch20** | ✅ |
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

- BC-CP-CF

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/cloud-foundry-runtime?service_plan=cloud-foundry-runtime&region=all)
- [SAP Discovery Center - Cloud Foundry Runtime](https://discovery-center.cloud.sap/serviceCatalog/cloud-foundry-runtime)

### Documentation

- [SFLIGHT Sample Application Using SAP Cloud Application Programming Model (CAP)](https://github.com/SAP-samples/cap-sflight)
- [Sample Node.js Application Using SAP Cloud Application Programming Model (CAP)](https://github.com/SAP-samples/cloud-cap-samples)
- [Sample Java Application Using SAP Cloud Application Programming Model (CAP)](https://github.com/SAP-samples/cloud-cap-samples-java)
- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Application%20Programming%20Model;HTML5%20Application%20Repository;Multitenancy;Node.js%20System%20Buildpack;Python%20Buildpack;SAP%20Java%20Buildpack;SAPUI5&date=all)
- [Feature Scope Description](https://help.sap.com/doc/5e8107bf49684962b897217040398007/)
- [Developing HTML5 Applications](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/11d77aa154f64c2e83cc9652a78bb985.html)
- [Development in the Cloud Foundry Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/40a8f8f6f1724e0ca0fd2a8777f45504.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/9c7092c7b7ae4d49bc8ae35fdd0e0b18.html)
- [Help Portal Product Page](https://help.sap.com/docs/CF_RUNTIME)
- [SAPUI5 API Reference](https://sapui5.hana.ondemand.com/#/api)

### Learning

- [Develop Node.js Applications](https://open.sap.com/courses/cp1-2)
- [Building Applications with SAP Cloud Application Programming Model](https://open.sap.com/courses/cp7/resume)
- [Developing Web Apps with SAPUI5](https://open.sap.com/courses/ui51/resume)
- [Evolved Web Apps with SAPUI5](https://open.sap.com/courses/ui52/resume)
- [SAP BTP, Cloud Foundry Environment Learning Journey](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/d3d210f71462488883768bb02e05174d.html)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [Business Application Studio](https://community.sap.com/topics/business-application-studio)
- [SAP BTP](https://community.sap.com/topics/business-technology-platform)
- [SAP Cloud Application Programming Model](https://community.sap.com/topics/cloud-application-programming)
- [Low-Code/No-Code](https://community.sap.com/topics/low-code-no-code)
- [SAPUI5](https://community.sap.com/topics/ui5/developing-sapui5-applications)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20BTP%2C%20Cloud%20Foundry%20runtime)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20BTP%2C%20Cloud%20Foundry%20runtime)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

### Tutorial

- [Get Ready to Develop on SAP BTP](https://developers.sap.com/group.scp-1-get-ready.html?url_id=text-us-recommendation)
- [Build an Application End-to-End Using CAP, Node.js and VS Code](https://developers.sap.com/mission.btp-application-cap-e2e.html)
- [Build a Business Application Using CAP for Java](https://developers.sap.com/mission.cap-java-app.html)
- [Build a Business Application Using CAP for Node.js](https://developers.sap.com/mission.cp-starter-extensions-cap.html)

## Sample configuration of **SAP BTP, Cloud Foundry runtime** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **cloudfoundry** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "ENVIRONMENT",
      "name": "cloudfoundry",
      "plan": "free"
    }
  ]
}
```
