# objectstore (Object Store on SAP BTP)

Object Store on SAP BTP provisions an object storage space that can be used by applications to store and manage objects.

## Service plan availability in regions

| Region | azure-standard | gcs-standard | s3-standard |
|--------|----------------|--------------|-------------|
|  **ap10** | | | ✅ |
|  **ap11** | | | ✅ |
|  **ap12** | | | ✅ |
|  **ap20** | ✅ | | |
|  **ap21** | ✅ | | |
|  **br10** | | | ✅ |
|  **ca10** | | | ✅ |
|  **ch20** | ✅ | | |
|  **eu10** | | | ✅ |
|  **eu11** | | | ✅ |
|  **eu20** | ✅ | | |
|  **eu30** | | ✅ | |
|  **in30** | | ✅ | |
|  **jp10** | | | ✅ |
|  **jp20** | ✅ | | |
|  **us10** | | | ✅ |
|  **us20** | ✅ | | |
|  **us21** | ✅ | | |
|  **us30** | | ✅ | |

## Additional details

### Support components

- BC-CP-CF-OSAAS

### Discovery Center

- [SAP Discovery Center - Object Store](https://discovery-center.cloud.sap/serviceCatalog/object-store)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/1aab7a8ce65e4c53a65adfe5c18ca6a3/)
- [Documentation](https://help.sap.com/viewer/2ee77ef7ea4648f9ab2c54ee3aef0a29/Cloud/en-US)
- [What's New](https://help.sap.com/docs/BTP/2ee77ef7ea4648f9ab2c54ee3aef0a29/6882672b5bc24c40b8d987a30e6c59e7.html)
- [What is Object Store on SAP BTP](https://help.sap.com/docs/BTP/2ee77ef7ea4648f9ab2c54ee3aef0a29/84eb69a421294ba0a407579490413dfa.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/ObjectStore/Cloud/en-US)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/data-storage/objectstore.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Object%20Store%20on%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Object%20Store%20on%20SAP%20BTP)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Object Store on SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **objectstore** by configuring your `usecase.json` file.

### Using the service plan **azure-standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "objectstore",
      "plan": "azure-standard"
    }
  ]
}
```

### Using the service plan **gcs-standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "objectstore",
      "plan": "gcs-standard"
    }
  ]
}
```

### Using the service plan **s3-standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "objectstore",
      "plan": "s3-standard"
    }
  ]
}
```
