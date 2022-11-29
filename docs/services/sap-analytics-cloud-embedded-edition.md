# sap-analytics-cloud-embedded-edition (SAP Analytics Cloud, embedded edition)

With SAP Analytics Cloud, embedded edition, you can build and embed reports, dashboards, and visuals into your business application to make confident decisions. Explore your business data via live connection between your SAP Analytics Cloud tenant and the remote SAP HANA database on SAP Business Technology Platform.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- LOD-ANA-OEM-CP

### API Hub

- [Overview | SAP Analytics Cloud, Embedded Edition | SAP API Business Hub](https://api.sap.com/package/SAPAnalyticsCloudEmbeddedEdition/overview)

### Discovery Center

- [SAP Discovery Center - SAP Analytics Cloud, embedded edition](https://discovery-center.cloud.sap/serviceCatalog/sap-analytics-cloud-embedded-edition)

### Documentation

- [SAP Analytics Cloud, Embedded Edition Service on SAP BTP: Getting Started Guide](https://help.sap.com/viewer/7466893ec68641198fc189757dc5f7a6/1.0/en-US/842009c3f599432a8f6c6e248267380d.html)
- [Documentation](https://help.sap.com/viewer/7466893ec68641198fc189757dc5f7a6/1.0/en-US/ce081403aaf14feca286d7d0b4af2b86.html)
- [Feature Scope Description SAP Analytics Cloud, Embedded Edition on SAP BTP](https://help.sap.com/viewer/777b4c63a7da46d3ad92b123a83c0673/1.0/en-US/3c0960ff0516426c8ffca7d18c7b060d.html)
- [SAP Analytics Cloud, Embedded Service on SAP BTP: Development](https://help.sap.com/viewer/8c9fe042688a4354876cc536267d442f/1.0/en-US/738ee174a5244573a3f52848cba0e926.html)
- [Documentation](https://help.sap.com/viewer/8c9fe042688a4354876cc536267d442f/1.1/en-US)
- [Documentation](https://help.sap.com/viewer/product/SAC_EMBEDDED_EDITION/1.0/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAC_EMBEDDED_EDITION/1.1/en-US)

### External

- [SAP Analytics Cloud, Embedded Edition](https://www.youtube.com/embed/QXK4qRh7qTc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Analytics%20Cloud%2C%20embedded%20edition)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Analytics%20Cloud%2C%20embedded%20edition)

## Sample configuration of **SAP Analytics Cloud, embedded edition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-analytics-cloud-embedded-edition** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-analytics-cloud-embedded-edition",
      "plan": "standard"
    }
  ]
}
```
