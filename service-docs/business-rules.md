# business-rules (SAP Business Rules Management)

SAP Business Rules service translates business-decision logic into natural language that is configurable directly by line-of-business key users or knowledge experts without IT or developer intervention. It provides web-based tools to solution architects and developers, enabling them to model, author, and simulate business rules independent of the backend system.

## Service plan availability in regions

| Region | basic | standard |
|--------|-------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | |
|  **ap20** | ✅ | |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | |

## Additional details

### Support components

- LOD-BPM-RUL

### API Hub

- [Overview | Business Rules Service | SAP API Business Hub](https://api.sap.com/package/SAPCPBusinessRulesAPIs/overview)

### Blog

- [Blogs](https://blogs.sap.com/tags/73554900100800000842/)

### Discovery Center

- [SAP Discovery Center - Business Rules](https://discovery-center.cloud.sap/serviceCatalog/business-rules)

### Documentation

- [API Documentation](https://api.sap.com/package/SAPCPBusinessRulesAPIs?section=OVERVIEW)
- [Feature Scope Description](https://help.sap.com/http.svc/rc/2d4bd70d121b4e56adff94a901721d69/Cloud/en-US/FSD_en.pdf)
- [What is Business Rules Capability?](https://help.sap.com/docs/BTP/0e4dd38c4e204f47b1ffd09e5684537b/7457217efc8b47539160eeb9d2ee9db0.html)
- [What's New](https://help.sap.com/viewer/5a2fbf4f7c184dd086fdcc67d84aa682/Cloud/en-US)
- [Help Portal Product Page](https://help.sap.com/docs/BUSINESS_RULES)

### External

- [External](https://www.youtube.com/watch?v=Q8jUHt9UMw8)

### Learning

- [Learning Journey: Business Rules](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/2a01085aa2d84c579bdf0cd9e397e5b7.html)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/integration/business-rules.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Business%20Rules%20Management)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Business%20Rules%20Management)

### Support

- [Support Components for SAP BTP](https://launchpad.support.sap.com/#/notes/1888290)

### Tutorial

- [Tutorial: Automate and Extend Employee Onboarding](https://developers.sap.com/mission.cp-starter-ibpm-employeeonboarding.html)

## Sample configuration of **SAP Business Rules Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **business-rules** by configuring your `usecase.json` file.

### Using the service plan **basic**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "business-rules",
      "plan": "basic"
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
      "name": "business-rules",
      "plan": "standard"
    }
  ]
}
```
