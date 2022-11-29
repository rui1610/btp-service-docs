# sap-graph (SAP Graph)

SAP Graph is a new unified API for SAP, using modern open standards like OData v4. With SAP Graph, developers access SAP-managed business data as a single semantically connected data graph, spanning the suite of SAP products. Targeting SAP's ecosystem of developers and customers, SAP Graph's one API and Business Data Graph reduce the cost and complexity of creating and deploying reusable extension applications. The unified API exposes a unified graph-like model of business objects (entities) and relationships. As a BTP service, SAP Graph is compatible with SAP Cloud Application Programming (CAP) extension solutions, events managed via SAP Event Mesh, and No-Code/Low-Code applications like SAP AppGyver. SAP Graph uses open standards, such as OData v.4 and OAuth, thus allowing you to easily build applications and extensions for the SAP Intelligent Enterprise.

## Service plan availability in regions

| Region | free |
|--------|------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- CA-GRAPH

### API Hub

- [Overview | SAP Graph | SAP API Business Hub](https://api.sap.com/package/SAPGRAPH/overview)

### Blog

- [SAP Graph Blogs](https://blogs.sap.com/tags/da20f5de-7c9f-47c9-b766-b98820e5be12/)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/sap-graph)
- [SAP Discovery Center - SAP Graph](https://discovery-center.cloud.sap/serviceCatalog/sap-graph)

### Documentation

- [Documentation](https://help.sap.com/docs/SAP_GRAPH/84bbf6acb5384861add4cb6939bef647/d3a155b8842b4a43b1367c2edb1c964e.html#3.-register-client-applications)
- [What's New for SAP Graph](https://help.sap.com/products/SAP_GRAPH/84bbf6acb5384861add4cb6939bef647/a509e6a5a1f64abeb95b8ceb348ad939.html)
- [What is SAP Graph?](https://help.sap.com/products/SAP_GRAPH/84bbf6acb5384861add4cb6939bef647/af92ea0700ab4c59a3cfcd79158fdd56.html)
- [Developer Guide](https://help.sap.com/products/SAP_GRAPH/84bbf6acb5384861add4cb6939bef647/ddb10ff724884dfa805077a4f4d7b7a1.html)
- [Configuration Guide](https://help.sap.com/products/SAP_GRAPH/84bbf6acb5384861add4cb6939bef647/e066b359ee71467c90b916f61f30a8e1.html)

### External

- [External](https://explore.dev.graph.sap/docs/beta)
- [External](https://explore.graph.sap/docs)
- [External](https://graph.sap/docs/beta/)
- [SAP Graph Navigator](https://navigator.graph.sap/entities)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### Support

- [Ask a question about SAP Graph](https://answers.sap.com/tags/da20f5de-7c9f-47c9-b766-b98820e5be12)

## Sample configuration of **SAP Graph** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-graph** by configuring your `usecase.json` file.

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-graph",
      "plan": "free"
    }
  ]
}
```
