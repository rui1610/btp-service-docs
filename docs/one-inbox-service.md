# one-inbox-service (SAP Task Center)

The SAP Task Center service only enables, but does not include the integration implementation from the supported SAP solutions. The SAP Task Center service enables integration with SAP applications to provide a single entry point for end users to access all their assigned workflow tasks. The tasks can be accessed by end users through the SAP Task Center Web application.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap20** | ✅ |
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

- LOD-BPM-INB

### API Hub

- [Overview | SAP Task Center | SAP API Business Hub](https://api.sap.com/package/SAPTaskCenter/overview)

### Discovery Center

- [SAP Discovery Center - SAP Task Center](https://discovery-center.cloud.sap/serviceCatalog/sap-task-center)

### Documentation

- [API Documentation](https://api.sap.com/package/SAPTaskCenter?section=Artifacts)
- [Access the SAP Task Center API using Postman](https://blogs.sap.com/2021/06/08/access-the-sap-task-center-api-using-postman/)
- [See all SAP Task Center Blogs](https://community.sap.com/topics/task-center?ct=blog)
- [SAP Task Center Detailed Presentation](https://d.dam.sap.com/a/a2x3zwM/SAP%20Task%20Center_L3%20Presentation.pdf?rc=10)
- [SAP Task Center: Click, Read, Approve, Repeat!](https://news.sap.com/2021/12/sap-task-center-click-read-approve-repeat/)
- [Integrate Solutions in Your Intelligent Enterprise: What's Trending?](https://www.youtube.com/watch?v=CF1ADKt4l3k)
- [Simplifying approvals across the Intelligent Suite in One Workflow Inbox (SAP Task Center) – SAP Garage 2022](https://www.youtube.com/watch?v=Epc-EfTO-rI)
- [Feature Scope Description](https://help.sap.com/doc/1599f0308de2496582b9da1680f3519e/)
- [What Is SAP Task Center?](https://help.sap.com/viewer/08cbda59b4954e93abb2ec85f1db399d/Cloud/en-US)
- [What's New](https://help.sap.com/docs/BTP/08cbda59b4954e93abb2ec85f1db399d/1bcdd459f84d4323a27581226d1d210e.html)
- [Initial Setup](https://help.sap.com/docs/BTP/08cbda59b4954e93abb2ec85f1db399d/834769400794464489f390350a82bbd6.html)
- [Documentation](https://help.sap.com/viewer/product/TASK_CENTER/Cloud)
- [Help Portal Product Page](https://help.sap.com/docs/TASK_CENTER)

### External

- [SAP Task Center](https://www.youtube.com/embed/ai3G7ejuiB4)
- [SAP Mobile Start – Your native entry point to the Intelligent Enterprise](https://www.youtube.com/embed/sv_q64zJ5cA)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Task%20Center)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Task%20Center)

### Support

- [Troubleshooting](https://help.sap.com/docs/BTP/08cbda59b4954e93abb2ec85f1db399d/89c09a4067bd4c62a5a4b2f5c0da48c5.html)
- [Support](https://help.sap.com/docs/BTP/08cbda59b4954e93abb2ec85f1db399d/9693186f1fe54cbe801085d6bdfe8287.html)

## Sample configuration of **SAP Task Center** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **one-inbox-service** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "one-inbox-service",
      "plan": "standard",
      "parameters" : {
        "authorities": null,
        "defaultCollectionQueryFilter": null
      }
    }
  ]
}
```
