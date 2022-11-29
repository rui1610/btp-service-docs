# process-automation (SAP Build Process Automation)

SAP Build Process Automation is a citizen development solution to adapt, improve, and innovate business processes with the low-code/no-code capabilities of SAP Workflow Management and SAP Intelligent RPA.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- BPI-PA

### API Hub

- [Overview | SAP Build Process Automation | SAP API Business Hub](https://api.sap.com/package/SAPProcessAutomation/overview)

### Discovery Center

- [SAP Discovery Center - SAP Build Process Automation](https://discovery-center.cloud.sap/serviceCatalog/sap-build-process-automation)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/b3c2de746b0645aeb627deda35b896a0/)
- [Documentation](https://help.sap.com/docs/PROCESS_AUTOMATION)
- [Initial Setup](https://help.sap.com/docs/BTP/a331c4ef0a9d48a89c779fd449c022e7/b9758013e1114c9194cd52de2885e9a9.html)
- [What Is SAP Build Process Automation?](https://help.sap.com/docs/BTP/a331c4ef0a9d48a89c779fd449c022e7/c20b4e77201b4cde9ce4227e21850deb.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/PROCESS_AUTOMATION/Cloud)

### Learning

- [Learning Journey: Low-Code and No-Code Automations and Applications for Citizen Developers](https://learning.sap.com/learning-journey/low-code-no-code-applications-and-automations-for-citizen-developers)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### Onboarding

- [Tutorial: Onboarding](https://blogs.sap.com/2022/03/29/sap-process-automation-free-tier-availability/)

## Sample configuration of **SAP Build Process Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **process-automation** by configuring your `usecase.json` file.

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "process-automation",
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
      "name": "process-automation",
      "plan": "standard"
    }
  ]
}
```
