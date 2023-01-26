# one-mds (SAP Master Data Integration)

SAP Business Technology Platform Master Data Integration service offers master data synchronization across SAP solutions and is a central access layer for data sharing and distribution. The service can only be used for SAP to SAP Integration, and must not be directly accessed for 3rd party master data integration scenarios with SAP. SAP Business Technology Platform Master Data Orchestration is part of the master data integration service, and can only be used in conjunction with SAP Master Data Integration service.

## Service plan availability in regions

| Region | s4hana-onpremise | sap-integration |
|--------|------------------|-----------------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CF-ONEMDS

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/master-data-integration?region=all)
- [SAP Discovery Center - Master Data Integration](https://discovery-center.cloud.sap/serviceCatalog/master-data-integration)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/343e91db93e64e6ab258a1e51adc6377/CLOUD/en-US/499a1a82e6134361b9922d989dfecff6.pdf)
- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Master%20Data%20Integration)
- [Initial Setup](https://help.sap.com/viewer/c7713d6177ad479d9ea00958db9f2f81/CLOUD/en-US/39c84a9a3ca947b695d15db11444d999.html)
- [Onboarding](https://help.sap.com/viewer/c7713d6177ad479d9ea00958db9f2f81/CLOUD/en-US/69ae614272654411a4c03acea8d488b3.html)
- [What is SAP Master Data Integration?](https://help.sap.com/viewer/c7713d6177ad479d9ea00958db9f2f81/CLOUD/en-US/dab76d5506a44c8e85f314fc3be30e13.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAP_MASTER_DATA_INTEGRATION/CLOUD/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Master%20Data%20Integration)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Master%20Data%20Integration)

## Sample configuration of **SAP Master Data Integration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **one-mds** by configuring your `usecase.json` file.

### Using the service plan **s4hana-onpremise**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "one-mds",
      "plan": "s4hana-onpremise",
      "parameters" : {
        "businessSystemId": null,
        "enableTenantDeletion": false,
        "writePermissions": null,
        "logSys": null,
        "globalTenantId": null
      }
    }
  ]
}
```

### Using the service plan **sap-integration**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "one-mds",
      "plan": "sap-integration",
      "parameters" : {
        "businessSystemId": null,
        "enableTenantDeletion": false,
        "writePermissions": null,
        "logSys": null,
        "globalTenantId": null,
        "application": null
      }
    }
  ]
}
```
