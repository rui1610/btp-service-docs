# WorkflowManagementSaaS (SAP Workflow Management)

Digitize workflows, manage decisions and gain end-to-end process visibility

## Service plan availability in regions

| Region | saas-application |
|--------|------------------|
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
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- LOD-BPM-WFS

### Discovery Center

- [SAP Discovery Center - Workflow Management](https://discovery-center.cloud.sap/serviceCatalog/workflow-management)

### Documentation

- [Roadmap](https://roadmaps.sap.com/board?BC=6EAE8B28C5D91EDA9E819CA3AB46E0E5)
- [Feature Scope Description](https://help.sap.com/doc/4017908370e54d318faed689bdbca6a6/)
- [API Documentation](https://help.sap.com/docs/BTP/6f55baaf330443bd8132d071581bbae6/98f1df747e344adcbfbb81747a530dba.html)
- [Initial Setup](https://help.sap.com/docs/BTP/6f55baaf330443bd8132d071581bbae6/d7910e2bf7f64afc9d0eb21b0cc9e84d.html)
- [What is Workflow Management](https://help.sap.com/docs/BTP/6f55baaf330443bd8132d071581bbae6/da4a2678e5c4406d803e6879cf7427bc.html)
- [Help Portal Product Page](https://help.sap.com/docs/WORKFLOW_MANAGEMENT)

### External

- [Purchase Requisition Approval and Release with SAP Workflow Management](https://www.youtube.com/embed/aUvOt7DGyeU)

### SAP Community

- [Digital Process Automation – Topic Page](https://community.sap.com/topics/digital-process-automation)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Workflow%20Management)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Workflow%20Management)

### Support

- [Support Components](https://launchpad.support.sap.com/#/notes/1888290)

### Tool

- [Workflow Editor](https://help.sap.com/docs/BTP/e157c391253b4ecd93647bf232d18a83/0047e4b99ac240ffae5ab870ff866f9f.html)
- [Monitor Workflows app](https://help.sap.com/docs/BTP/e157c391253b4ecd93647bf232d18a83/e6163e119ba645d0ae6a31022b670381.html)

### Tutorial

- [Tutorial: Automate and Extend Employee Onboarding](https://developers.sap.com/mission.cp-starter-ibpm-employeeonboarding.html)

## Sample configuration of **SAP Workflow Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **WorkflowManagementSaaS** by configuring your `usecase.json` file.

### Using the service plan **saas-application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "WorkflowManagementSaaS",
      "plan": "saas-application"
    }
  ]
}
```
