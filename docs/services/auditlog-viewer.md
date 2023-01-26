# auditlog-viewer (SAP Audit Log Viewer service for SAP BTP)

SAP Audit Log Viewer service for SAP BTP helps to view and manage audit logs.

## Service plan availability in regions

| Region | free |
|--------|------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-CP-CF-SEC-AUDITLG

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/audit-log-service)

### Documentation

- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e3baa5f1a0c64c44aac8ab3ea3d1b500.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Audit%20Log%20Viewer%20service%20for%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Audit%20Log%20Viewer%20service%20for%20SAP%20BTP)

## Sample configuration of **SAP Audit Log Viewer service for SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **auditlog-viewer** by configuring your `usecase.json` file.

### Using the service plan **free** (Audit Log Viewer)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "auditlog-viewer",
      "plan": "free"
    }
  ]
}
```
