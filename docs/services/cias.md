# cias (Cloud Integration Automation)

Cloud Integration Automation service provides you a guided workflow to integrate SAP cloud solutions to On-Premise and other SAP Cloud solutions. The guided workflow contains instructions for manual and automated tasks to enable a simpler and faster integration configuration setup

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **us10** | ✅ |

## Additional details
### Blog

- [Cloud Integration Automation Service – What is it?](https://blogs.sap.com/2018/05/28/cloud-integration-automation-service-what-is-it/)
- [Cloud Integration Automation Service: Step-by Step](https://blogs.sap.com/2018/06/08/cloud-integration-automation-service-step-by-step/)

### Discovery Center

- [SAP Discovery Center - Cloud Integration Automation](https://discovery-center.cloud.sap/serviceCatalog/cloud-integration-automation)

### Documentation

- [Initial Setup](https://launchpad.support.sap.com/#/notes/2608492)
- [What is Cloud Integration Automation Service](https://help.sap.com/viewer/edfa11059aca499892c08168fd68d97d/Latest/en-US/35fbf2ab8a844217b3486f85a2bd9ab2.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/Cloud%20Integration%20Automation%20Service/Latest/en-US)
- [Documentation](https://help.sap.com/viewer/product/Cloud%2520Integration%2520Automation%2520Service/Latest/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Cloud%20Integration%20Automation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Cloud%20Integration%20Automation)

## Sample configuration of **Cloud Integration Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **cias** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "cias",
      "plan": "standard"
    }
  ]
}
```
