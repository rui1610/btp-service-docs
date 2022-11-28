# auditlog-management (SAP Audit Log Management service)

SAP Audit Log Management service helps to retrieve logs and change retention.

## Service plan availability in regions

| Region | central | default |
|--------|---------|---------|
|  **ap10** | | ✅ |
|  **ap11** | | ✅ |
|  **ap12** | | ✅ |
|  **ap20** | | ✅ |
|  **ap21** | | ✅ |
|  **br10** | | ✅ |
|  **ca10** | | ✅ |
|  **ch20** | | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | | ✅ |
|  **eu20** | | ✅ |
|  **eu30** | | ✅ |
|  **in30** | | ✅ |
|  **jp10** | | ✅ |
|  **jp20** | | ✅ |
|  **us10** | | ✅ |
|  **us20** | | ✅ |
|  **us21** | | ✅ |
|  **us30** | | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/audit-log-service)

### Documentation

- [Documentation](https://help.sap.com/products/BTP/65de2977205c403bbc107264b8eccf4b/f92c86ab11f6474ea5579d839051c334.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/30ece35bac024ca69de8b16bff79c413.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Audit%20Log%20Management%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Audit%20Log%20Management%20service)

## Sample configuration of **SAP Audit Log Management service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **auditlog-management** by configuring your `usecase.json` file.

### Using the service plan **central** (Central)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "auditlog-management",
      "plan": "central"
    }
  ]
}
```

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "auditlog-management",
      "plan": "default"
    }
  ]
}
```
