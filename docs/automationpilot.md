# automationpilot (SAP Automation Pilot)

SAP Automation Pilot provides out-of-the-box high-quality automation such as application restarts and reconfigurations, database restarts and updates, application and database health statuses, RCA, recommended actions, and more. Complex DevOps tasks are made simple without the need of having deep SAP Business Technology Platform knowledge. In addition, recommended actions are automated by using the SAP Alert Notification service for SAP BTP (sophisticated integration to immediately react on incoming alerts) or any other alerting system.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-LCM-AP

### API Hub

- [Overview | SAP Automation Pilot | SAP API Business Hub](https://api.sap.com/package/SAPCloudPlatformAutomationPilot/overview)

### Blog

- [Blog](https://blogs.sap.com/tags/73554900100800002433)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/automation-pilot)
- [SAP Discovery Center - Automation Pilot](https://discovery-center.cloud.sap/serviceCatalog/automation-pilot)

### Documentation

- [Initial Setup](https://help.sap.com/docs/BTP/de3900c419f5492a8802274c17e07049/76e77c4563d042b2b46f6c622be3a091.html)
- [What's New](https://help.sap.com/docs/BTP/de3900c419f5492a8802274c17e07049/e0809493f059463aa4fa3f3880224683.html)
- [Documentation](https://help.sap.com/docs/AUTOMATION_PILOT)
- [Documentation](https://help.sap.com/viewer/product/AUTOMATION_PILOT)

### External

- [SAP Automation Pilot - Introduction](https://www.youtube.com/embed/BIS_OK1ZNXI)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Automation%20Pilot)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Automation%20Pilot)

## Sample configuration of **SAP Automation Pilot** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **automationpilot** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "automationpilot",
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
      "name": "automationpilot",
      "plan": "standard"
    }
  ]
}
```
