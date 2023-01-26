# portal (SAP Cloud Portal service)

SAP Business Technology Platform Portal lets you build digital experience portals for employees, customers, and partners. You can streamline access to business data so that your employees can execute their daily business tasks securely, from any device.

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
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- EP-CPP-CF-LND

### API Hub

- [Overview | SAP Build Work Zone and SAP Cloud Portal Service | SAP API Business Hub](https://api.sap.com/package/SAPCLOUDPLATFORMPORTAL/overview)

### Discovery Center

- [SAP Discovery Center - Cloud Portal Service](https://discovery-center.cloud.sap/serviceCatalog/cloud-portal-service)

### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Portal)
- [Feature Scope Description](https://help.sap.com/doc/8bac45b5f9834b039030fd30ef693147/)
- [Documentation](https://help.sap.com/docs/WZ)
- [Documentation](https://help.sap.com/docs/WZ_STD)
- [Documentation](https://help.sap.com/viewer/8422cb487c2146999a2a7dab9cc85cf7/Cloud/en-US)
- [Cloud Portal Service, Neo Environment](https://help.sap.com/docs/BTP/8422cb487c2146999a2a7dab9cc85cf7/04b348a5a6d44c04b1d5d36e18e62ba0.html)
- [Cloud Portal Service, Cloud Foundry Environment](https://help.sap.com/docs/BTP/ad4b9f0b14b0458cad9bd27bf435637d/5798687972fd4c2bace31c65b47f5587.html)
- [Initial Setup](https://help.sap.com/docs/BTP/ad4b9f0b14b0458cad9bd27bf435637d/fd79b232967545569d1ae4d8f691016b.html)
- [Help Portal Product Page](https://help.sap.com/docs/P)
- [Documentation](https://help.sap.com/viewer/product/Portal_Service/1.0/en-US)
- [Documentation](https://help.sap.com/viewer/product/Portal_Service/latest/en-US)
- [openSAP: Building Portal Sites on SAP Business Technology Platform](https://open.sap.com/courses/portal2)
- [SAP Cloud Portal Community](https://www.sap.com/community/topic/portal.html)
- [SAP Portal Deployment Options](https://www.sap.com/documents/2015/07/60bf3952-5a7c-0010-82c7-eda71af511fa.html)
- [SAP Business Technology Platform Portal Roadmap](https://www.sap.com/documents/2017/06/5c1b1e2a-c37c-0010-82c7-eda71af511fa.gate.html)
- [SAP Business Technology Platform Portal - Solution Brief](https://www.sap.com/documents/2017/09/2a6c387b-d47c-0010-82c7-eda71af511fa.html)

### External

- [SAP Portal YouTube Channel](https://www.youtube.com/channel/UCqV5n0s204-CLxCNW80aR7g)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/ux/cloud-portal.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Cloud%20Portal%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Cloud%20Portal%20service)

### Support

- [Troubleshooting and Monitoring](https://help.sap.com/docs/BTP/ad4b9f0b14b0458cad9bd27bf435637d/de4d7d6401dd44af914af1405ba667c8.html)

### Tutorial

- [Tutorial Starter Scenario: Deliver Your First Portal Site](https://help.sap.com/viewer/disclaimer-for-links?q=https://developers.sap.com/mission.cp-starter-digitalexp-portal.html)

## Sample configuration of **SAP Cloud Portal service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **portal** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "portal",
      "plan": "standard"
    }
  ]
}
```
