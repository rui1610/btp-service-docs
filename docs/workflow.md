# workflow (SAP Workflow Management)

SAP Workflow service allows you to build, run, and manage workflows, from simple approvals to end-to-end processes that span across different organizations and applications. With an inbox application and custom-built user interfaces, you involve end users into business processes for decision making and data entry. The workflow service comes with web-based tools for workflow modeling, APIs for consumption in custom applications, monitoring tools, and a set of Fiori-based applications for end-user access. You can use JavaScript to embed custom business logic.

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
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- LOD-BPM-WFS

### API Hub

- [Overview | SAP Workflow Service | SAP API Business Hub](https://api.sap.com/package/SAPCPWorkflowAPIs/overview)

### Blog

- [Blogs](https://blogs.sap.com/tags/73554900100800000555/)

### Discovery Center

- [SAP Discovery Center - Workflow](https://discovery-center.cloud.sap/serviceCatalog/workflow)

### Documentation

- [What's New](https://help.sap.com/doc/8c8be0fcde064d4d95e958c44bbce34c/Cloud/en-US/34a79458361c4cadb7fdac12e4294b6b.html)
- [Feature Scope Description](https://help.sap.com/doc/a78c0b1278914d8cacdee12ab4c18b63/)
- [What is Workflow](https://help.sap.com/docs/WORKFLOW/16e4ca742bd742e98184ef1e53d2ec2d/a3220658f2dc46a48e47614aa2a2c663.html)
- [Developing Applications with Workflow Capability](https://help.sap.com/docs/WORKFLOW/e157c391253b4ecd93647bf232d18a83/60ae81179050478caa4212fad4ba50f2.html)
- [Consuming the Workflow Capability at Application Runtime](https://help.sap.com/docs/WORKFLOW/e157c391253b4ecd93647bf232d18a83/e379f6b9d2354e3ba09908f736c89e2a.html)
- [Initial Setup in the Cloud Foundry Environment](https://help.sap.com/docs/WORKFLOW/e157c391253b4ecd93647bf232d18a83/fc3d44872c354742afd672aa8d9c16b4.html)
- [Help Portal Product Page](https://help.sap.com/docs/WORKFLOW)
- [Documentation](https://help.sap.com/docs/BTP/e157c391253b4ecd93647bf232d18a83/fab405aa1ec64d6e9880761a31b0cd06.html)
- [Documentation](https://help.sap.com/docs/BTP/f85276c5069a429fa37d1cd352785c25/df943e71122448caaf3c49f5ffd80627.html)
- [Documentation](https://help.sap.com/docs/WORKFLOW_SERVICE)
- [Documentation](https://www.sap.com/documents/2020/07/f8d617a4-a67d-0010-87a3-c30de2ffd8ff.html)

### Learning

- [Learning Journey: Workflow Capability](https://help.sap.com/learning-journeys/34c3e8adf5234d91b9b4cdee94b9306b)

### Marketing

- [Learn more about this service and how to purchase it.](https://launchpad.support.sap.com/#/notes/2483733)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Workflow%20Management)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Workflow%20Management)

### Support

- [Support Components for SAP BTP](https://launchpad.support.sap.com/#/notes/1888290)

### Tutorial

- [Get Started with SAP BTP Workflows](https://developers.sap.com/group.cp-workflow-cf.html)
- [Automate and Extend Employee Onboarding](https://developers.sap.com/mission.cp-starter-ibpm-employeeonboarding.html)

## Sample configuration of **SAP Workflow Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **workflow** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "workflow",
      "plan": "standard",
      "parameters" : {
        "authorities": null,
        "defaultCollectionQueryFilter": null
      }
    }
  ]
}
```
