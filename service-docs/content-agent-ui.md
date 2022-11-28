# content-agent-ui (SAP Content Agent service)

SAP Content Agent service is a tool for SAP BTP applications offering generic content management operations such as view, export and import content with inter-dependencies and integration with SAP Cloud Transport Management service. It offers a view to track all activities along with logs, status and other information.

## Service plan availability in regions

| Region | free |
|--------|------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **ch20** | ✅ |
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

- BC-CP-LCM-CAS

### API Hub

- [Overview | SAP Content Agent Service | SAP API Business Hub](https://api.sap.com/package/SAPContentAgentService/overview)

### Documentation

- [Documentation](https://help.sap.com/docs/BTP/ae1a4f2d150d468d9ff56e13f9898e07/9d9f235a96a947f5986021bbcebcef8c.html)
- [Documentation](https://help.sap.com/docs/CONTENT_AGENT_SERVICE)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Content%20Agent%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Content%20Agent%20service)

## Sample configuration of **SAP Content Agent service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **content-agent-ui** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "content-agent-ui",
      "plan": "free"
    }
  ]
}
```
