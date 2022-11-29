# processvisibility (Process Visibility)

Provides end-to-end visibility into processes that run in cloud, on-premise & in hybrid environments

## Service plan availability in regions

| Region | standard | workflow |
|--------|----------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | | ✅ |

## Additional details

### Support components

- LOD-BPM-VIS

### API Hub

- [Overview | Process Visibility on Contract Logistics | SAP API Business Hub](https://api.sap.com/package/ContractLogistics/overview)
- [Overview | Process Visibility on Invoice Management | SAP API Business Hub](https://api.sap.com/package/InvoiceManagement/overview)
- [Overview | Process Visibility on Meter to Cash | SAP API Business Hub](https://api.sap.com/package/MetertoCash/overview)

### Blog

- [Blogs for Process Visibility](https://blogs.sap.com/tags/5a7011ac-8031-4195-8250-704c3fd57599/)

### Discovery Center

- [SAP Discovery Center - Process Visibility](https://discovery-center.cloud.sap/serviceCatalog/process-visibility)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/7631de5808024cc2a16b00c5b15b6831/)
- [What is Process Visibility?](https://help.sap.com/docs/BTP/62fd39fa3eae4046b23dba285e84bfd4/2f72882f457a4b87a054bdf45d85fe52.html)
- [Initial Setup](https://help.sap.com/docs/BTP/62fd39fa3eae4046b23dba285e84bfd4/5d048d285e1b43d29efe04e2f9ab98fb.html)
- [Developer Guide](https://help.sap.com/docs/BTP/62fd39fa3eae4046b23dba285e84bfd4/82aa325d66d44d1c97737af8348f46c8.html)
- [What's New](https://help.sap.com/viewer/7ceb6d60b0f64b37b8a48b12ae9c452b/Cloud/en-US)
- [Documentation](https://smartprocessappsa636d78be.hana.ondemand.com/sap/opi/pv/workspace/?user=Lorin&password=1234Abcd#/scenarios/SCN0378ff049bbb4e23beac8cea36ac474f)
- [Documentation](https://smartprocessappsa636d78be.hana.ondemand.com/sap/opi/pv/workspace/?user=Lorin&password=1234Abcd#/scenarios/SCNf8f20510f84c421a9b8713ff326a953b)
- [Documentation](https://smartprocessappsa636d78be.hana.ondemand.com/sap/opi/pv/workspace/?user=Lorin&password=1234Abcd#/scenarios/SCNfbd2428a18d5466aa2cac194a43ff9d3)

### Learning

- [Learning Journey: Process Visibility](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/06b8fbcb3a464f02b11eae9468e69326.html)

### Marketing

- [Learn more about this service and how to purchase it.](https://help.sap.com/docs/VISIBILITY_SERVICE)

### Support

- [Support Components for SAP BTP](https://launchpad.support.sap.com/#/notes/1888290)

### Tutorial

- [Tutorial: Get Started with Process Visibility](https://developers.sap.com/mission.cp-visibility-get-started.html)

## Sample configuration of **Process Visibility** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **processvisibility** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "processvisibility",
      "plan": "standard"
    }
  ]
}
```

### Using the service plan **workflow**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "processvisibility",
      "plan": "workflow"
    }
  ]
}
```
