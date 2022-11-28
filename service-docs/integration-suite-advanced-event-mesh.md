# integration-suite-advanced-event-mesh (SAP Integration Suite, advanced event mesh)

Advanced event mesh for SAP Integration Suite is a complete event streaming, event management, and monitoring platform that incorporates best practices, expertise, and technology for event-driven architecture (EDA) on a single platform.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |

## Additional details

### Support components

- BC-CP-EM-AEM

### Discovery Center

- [SAP Discovery Center - Advanced Event Mesh](https://discovery-center.cloud.sap/serviceCatalog/advanced-event-mesh)

### Documentation

- [API Documentation](https://help.pubsub.em.services.cloud.sap/Cloud/solace_cloud_rest_api.htm)
- [Feature Scope Description](https://help.sap.com/doc/59d9991b28724bf891308c8c641c21dc/)
- [What is SAP Integration Suite, advanced event mesh?](https://help.sap.com/docs/SAP_ADVANCED_EVENT_MESH/649cec0ae9ac49059564a1870fb8a1b7/0d4bcd5a2be744688039160b9bb289ae.html)
- [Initial Setup](https://help.sap.com/docs/SAP_ADVANCED_EVENT_MESH/649cec0ae9ac49059564a1870fb8a1b7/4ffe28ff6eaa4037a89c3559793c941a.html)
- [Documentation](https://help.sap.com/docs/SAP_ADVANCED_EVENT_MESH/728c56cd25854f0fad611eb26ae17152/0d4bcd5a2be744688039160b9bb289ae.html)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_ADVANCED_EVENT_MESH)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Integration%20Suite%2C%20advanced%20event%20mesh)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Integration%20Suite%2C%20advanced%20event%20mesh)

### Tutorial

- [Creating and Sharing Event API Products](https://help.pubsub.em.services.cloud.sap/Cloud/Event-Portal/get-started-event-api-products.htm)
- [Designing Your Event-Driven Architecture](https://help.pubsub.em.services.cloud.sap/Cloud/Event-Portal/get-started-event-portal-designer.htm)
- [Discovering and Importing Your Event's Runtime Data](https://help.pubsub.em.services.cloud.sap/Cloud/Event-Portal/get-started-event-portal-discovery.htm)
- [Creating Your First Event Broker Service](https://help.pubsub.em.services.cloud.sap/Cloud/ggs_create_first_service.htm)
- [Creating Your First Queue](https://help.pubsub.em.services.cloud.sap/Cloud/ggs_queue.htm)
- [Trying Out Your Event Broker Service](https://help.pubsub.em.services.cloud.sap/Cloud/ggs_tryme.htm)

## Sample configuration of **SAP Integration Suite, advanced event mesh** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **integration-suite-advanced-event-mesh** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "integration-suite-advanced-event-mesh",
      "plan": "default"
    }
  ]
}
```
