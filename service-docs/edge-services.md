# edge-services (SAP Edge Services)

SAP Edge Services

## Service plan availability in regions

| Region | Enterprise | Standard |
|--------|------------|----------|
|  **eu10** | ✅ | ✅ |
|  **eu20** | | ✅ |
|  **us20** | ✅ | |

## Additional details

### Support components

- IOT-EDG

### Discovery Center

- [SAP Discovery Center - SAP Edge Services](https://discovery-center.cloud.sap/serviceCatalog/sap-edge-services)

### Documentation

- [API Documentation](https://help.sap.com/doc/5978814091b24ca08fc8d294d7a09f49/1912/en-US/EdgeServicesCEBusinessEssentialFunctionsAPIGuide1912.pdf)
- [Edge Services Overview Guide](https://help.sap.com/viewer/17e9e088c03b4d0cb59cd848e4e1c886/1912/en-US)
- [What's New](https://help.sap.com/viewer/41b0d35a94d1403c8eaef4bb840ca85d/1912/en-US)
- [Initial Setup](https://help.sap.com/viewer/9726aea5a09a47a184d40148dbd8be6a/1912/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/EDGE_SERVICES/1912/en-US)
- [SAP Edge Services Demo](https://www.sap.com/products/edge-services.deployment.html)

### Onboarding

- [Tutorial: Onboarding](https://help.sap.com/viewer/a25aa12c7a1344e8aeece1a83563660a/1912/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Edge%20Services)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Edge%20Services)

## Sample configuration of **SAP Edge Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **edge-services** by configuring your `usecase.json` file.

### Using the service plan **Enterprise** (SAP Edge Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "edge-services",
      "plan": "Enterprise"
    }
  ]
}
```

### Using the service plan **Standard** (SAP Edge Services Cloud Standard Edition)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "edge-services",
      "plan": "Standard"
    }
  ]
}
```
