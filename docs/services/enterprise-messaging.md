# enterprise-messaging (SAP Event Mesh)

The SAP Event Mesh service decouples communication and allows for event-driven business processes.

## Service plan availability in regions

| Region | default | event-mesh-connectivity | event-mesh-connectivity-beta |
|--------|---------|-------------------------|------------------------------|
|  **ap10** | ✅ | | |
|  **ap11** | ✅ | | |
|  **ap12** | ✅ | | |
|  **ap20** | ✅ | | |
|  **ap21** | ✅ | | |
|  **br10** | ✅ | | |
|  **ca10** | ✅ | | |
|  **ch20** | ✅ | | |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | | |
|  **eu20** | ✅ | | |
|  **eu30** | ✅ | | |
|  **in30** | ✅ | | |
|  **jp10** | ✅ | | |
|  **jp20** | ✅ | | |
|  **us10** | ✅ | | |
|  **us20** | ✅ | | ✅ |
|  **us21** | ✅ | | |
|  **us30** | ✅ | | |

## Additional details

### Support components

- BC-CP-EM-MES

### API Hub

- [Overview | SAP Event Mesh Default Plan | SAP API Business Hub](https://api.sap.com/package/SAPEventMeshDefaultPlan/overview)

### Blog

- [Blogs](https://blogs.sap.com/tags/73554900100800000765/)

### Discovery Center

- [SAP Discovery Center - Event Mesh](https://discovery-center.cloud.sap/serviceCatalog/event-mesh)

### Documentation

- [What's New for Event Mesh](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Enterprise%20Messaging%3BEvent%20Mesh&from=2021-01-01&title=JVM6&to=2021-12-30%22)
- [Feature Scope Description](https://help.sap.com/doc/e56d7e676cc74906b813d226062d8634/)
- [What Is Event Mesh?](https://help.sap.com/viewer/bf82e6b26456494cbdd197057c09979f/Cloud/en-US)
- [Documentation](https://help.sap.com/docs/BTP/bf82e6b26456494cbdd197057c09979f/00d56d697c7549408cfacc8cb6a46b11.html)
- [Initial Setup](https://help.sap.com/docs/BTP/bf82e6b26456494cbdd197057c09979f/3ef34ffcbbe94d3e8fff0f9ea2d5911d.html)
- [Documentation](https://help.sap.com/docs/BTP/bf82e6b26456494cbdd197057c09979f/6a0e4c77e3014acb8738af039bd9df71.html)
- [API Documentation](https://help.sap.com/docs/BTP/bf82e6b26456494cbdd197057c09979f/dc18d8ebc226404c87db22e818f70145.html)
- [Documentation](https://help.sap.com/docs/BTP/bf82e6b26456494cbdd197057c09979f/df532e8735eb4322b00bfc7e42f84e8d.html)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_ENTERPRISE_MESSAGING)

### External

- [SAP BTP in the Garage | Event Mesh Service](https://www.youtube.com/watch?v=lurri4pnW0c)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/integration/enterprise-messaging.html)

### Onboarding

- [Tutorial: Onboarding](https://developers.sap.com/group.cp-enterprisemessaging-get-started.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Event%20Mesh)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Event%20Mesh)

### Support

- [Guided Answers for Event Mesh](https://ga.support.sap.com/dtp/viewer/#/tree/2065/actions/26547:26549:28901:35015)
- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)
- [Monitoring and Troubleshooting](https://help.sap.com/docs/BTP/bf82e6b26456494cbdd197057c09979f/74cc07a56b974db4893e6b773fd1c02e.html)

### Tutorial

- [Tutorial: Develop a Node.js-Based Event Mesh App](https://developers.sap.com/group.cp-enterprisemessaging-app-create.html)

## Sample configuration of **SAP Event Mesh** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **enterprise-messaging** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "enterprise-messaging",
      "plan": "default",
      "parameters" : {
        "emname": null,
        "namespace": null,
        "version": null,
        "resources": null,
        "options": null,
        "rules": null,
        "authorities": null,
        "xs-security": null
      }
    }
  ]
}
```

### Using the service plan **event-mesh-connectivity** (Event Mesh Connectivity)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "enterprise-messaging",
      "plan": "event-mesh-connectivity"
    }
  ]
}
```

### Using the service plan **event-mesh-connectivity-beta**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "enterprise-messaging",
      "plan": "event-mesh-connectivity-beta"
    }
  ]
}
```
