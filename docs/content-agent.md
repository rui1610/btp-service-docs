# content-agent (SAP Content Agent service)

SAP Content Agent service is a tool for SAP BTP applications offering generic content management operations such as view, export and import content with inter-dependencies and integration with SAP Cloud Transport Management service. It offers a view to track all activities along with logs, status and other information.

## Service plan availability in regions

| Region | application | standard |
|--------|-------------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **ch20** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-LCM-CAS

### API Hub

- [Overview | SAP Content Agent Service | SAP API Business Hub](https://api.sap.com/package/SAPContentAgentService/overview)

### Blog

- [Blog: SAP Content Agent Service](https://blogs.sap.com/2020/08/30/introducing-sap-cloud-platform-content-agent-enhanced-transport-capabilities-for-sap-cloud-platform-integration-suite-content/)
- [How to use SAP Content Agent Service](https://blogs.sap.com/2022/09/05/how-to-use-sap-content-agent-service-video/)

### Discovery Center

- [SAP Discovery Center - Content Agent](https://discovery-center.cloud.sap/serviceCatalog/content-agent)

### Documentation

- [Roadmap](https://roadmaps.sap.com/board?range=CURRENT-LAST)
- [Documentation](https://help.sap.com/docs/BTP/ae1a4f2d150d468d9ff56e13f9898e07/9d9f235a96a947f5986021bbcebcef8c.html)
- [SAP Content Agent Service](https://help.sap.com/viewer/ae1a4f2d150d468d9ff56e13f9898e07/Latest/en-US)
- [Initial Setup](https://help.sap.com/viewer/ae1a4f2d150d468d9ff56e13f9898e07/Latest/en-US/15406a06dfac4c1fabd7845c703773ba.html)
- [What's New](https://help.sap.com/viewer/afbc0365ec0d41adaefc74714119149e/Latest/en-US)
- [Documentation](https://help.sap.com/docs/CONTENT_AGENT_SERVICE)
- [Help Portal Product Page](https://help.sap.com/viewer/product/CONTENT_AGENT_SERVICE/Latest/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Content%20Agent%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Content%20Agent%20service)

## Sample configuration of **SAP Content Agent service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **content-agent** by configuring your `usecase.json` file.

### Using the service plan **application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "content-agent",
      "plan": "application"
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
      "name": "content-agent",
      "plan": "standard"
    }
  ]
}
```
