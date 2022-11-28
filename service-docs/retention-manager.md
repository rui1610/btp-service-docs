# retention-manager (SAP Data Retention Manager)

The SAP Business Technology Platform Data Retention Manager lets you block or delete personal data based on the residence and retention rules maintained.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- LOD-GDP-RM

### API Hub

- [Overview | SAP Data Retention Manager | SAP API Business Hub](https://api.sap.com/package/SAPDataRetentionManager/overview)

### Blog

- [Data Retention Manager Blog](https://blogs.sap.com/2020/05/04/orchestrate-your-data-deletion-using-sap-cloud-platform-data-retention-manager/?preview_id=1093744)

### Discovery Center

- [SAP Discovery Center - SAP Data Retention Manager](https://discovery-center.cloud.sap/serviceCatalog/sap-data-retention-manager)

### Documentation

- [API Documentation](https://api.sap.com/package/SAPDataRetentionManager?section=Artifacts)
- [Feature Scope Description](https://help.sap.com/http.svc/rc/17df490294c24f89ab2338037f6ad6b5/SHIP/en-US/loioe93bad59a2ec47448390257bb9d5deab.pdf)
- [Initial Setup](https://help.sap.com/viewer/7b96239812444caf9dc36faa15292a2f/SHIP/en-US)
- [What is Data Retention Manager Service](https://help.sap.com/viewer/7b96239812444caf9dc36faa15292a2f/SHIP/en-US/08ad7d7ecfc740518d060d57e3f3e7a1.html)
- [Documentation](https://help.sap.com/viewer/d5e4ff1a64cc481185f23d16daa22110/SHIP/en-US/777c4864f9894c6287652ba799573cda.html)
- [User Guide for Data Retention Manager](https://help.sap.com/viewer/d5e4ff1a64cc481185f23d16daa22110/SHIP/en-US/7dc2912c4ca44573a5a15368313a800a.html)
- [Documentation](https://help.sap.com/docs/DATA_RETENTION_MANAGER)
- [Help Portal Product Page](https://help.sap.com/viewer/product/DATA_RETENTION_MANAGER/SHIP/en-US)

### External

- [DRM no restrictions Delete Data Subject Information Demo Video](https://www.youtube.com/embed/B_IzKf_GVXg)
- [DRM no restrictions Manage Business Purpose Demo Video](https://www.youtube.com/embed/HcGFFKg_k7s)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Data%20Retention%20Manager)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Data%20Retention%20Manager)

## Sample configuration of **SAP Data Retention Manager** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **retention-manager** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "retention-manager",
      "plan": "free"
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
      "name": "retention-manager",
      "plan": "standard"
    }
  ]
}
```
