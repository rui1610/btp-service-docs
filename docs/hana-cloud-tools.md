# hana-cloud-tools (SAP HANA Cloud)

SAP HANA Cloud provides a single place to access, store, and process all enterprise data in real time. It is a cloud-native platform that reduces the complexity of multi-cloud or hybrid system landscapes. SAP HANA Cloud provides all of the advanced SAP HANA technologies for multi-model data processing in-memory or on disk. You can benefit from cloud qualities such as automatic software updates, elasticity, and low total cost of ownership by using SAP HANA Cloud either as a stand-alone solution or as an extension to your existing on-premise environment.

## Service plan availability in regions

| Region | tools |
|--------|-------|
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
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-hana-cloud)

### Documentation

- [Documentation](https://help.sap.com/docs/HANA_CLOUD)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20HANA%20Cloud)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20HANA%20Cloud)

### Support

- [Support](https://help.sap.com/viewer/db19c7071e5f4101837e23f06e576495/cloud/en-US/4f8dabb4d8214d5d93b98dd5f2ad76c9.html)

## Sample configuration of **SAP HANA Cloud** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hana-cloud-tools** by configuring your `usecase.json` file.

### Using the service plan **tools**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "hana-cloud-tools",
      "plan": "tools"
    }
  ]
}
```
