# sap-bigdataservices (SAP Big Data Services)

Big Data Services

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Documentation

- [Initial Setup](https://help.sap.com/docs/BTP/50f26aa0f2044127bc5f6d5ad3d090fe/2e62036476b8101480abd76da746ffe7.html)
- [SAP Big Data Services](https://help.sap.com/docs/BTP/50f26aa0f2044127bc5f6d5ad3d090fe/2e660d5a76b8101480abd76da746ffe7.html)
- [What's New](https://help.sap.com/docs/BTP/50f26aa0f2044127bc5f6d5ad3d090fe/336334d6fe62495d84b66f60e7f1acac.html)
- [Getting Started Guide](https://help.sap.com/docs/BTP/50f26aa0f2044127bc5f6d5ad3d090fe/7d7ad1c0f90e42578a8a1a71b3307f4f.html)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_CLOUD_PLATFORM_BIG_DATA_SERVICES)
- [SAP Business Technology Platform Big Data Services for Manufacturing](https://www.sap.com/documents/2017/01/821512c3-a27c-0010-82c7-eda71af511fa.html)
- [SAP Business Technology Platform Big Data Services for Healthcare](https://www.sap.com/documents/2017/01/8a804bc6-a27c-0010-82c7-eda71af511fa.html)
- [Solution Overview](https://www.sap.com/documents/2017/01/c69fad31-a27c-0010-82c7-eda71af511fa.html)
- [SAP Business Technology Platform Big Data Services for Financial Services](https://www.sap.com/documents/2017/01/fe36f0c9-a27c-0010-82c7-eda71af511fa.html)
- [SAP Business Technology Platform Big Data Services for Oil and Gas](https://www.sap.com/documents/2017/07/7c3f7ed0-c87c-0010-82c7-eda71af511fa.html)
- [ SAP Business Technology Platform Big Data Services for Utilities](https://www.sap.com/documents/2017/07/f80ce562-c77c-0010-82c7-eda71af511fa.html)
- [Solution in Detail](https://www.sap.com/documents/2017/08/82cb27e3-cf7c-0010-82c7-eda71af511fa.html)
- [Nesutar BTS (Optimizing Marketing Spend with SAP Business Technology Platform Big Data Services)](https://www.sap.com/documents/2018/01/e27876d2-ed7c-0010-82c7-eda71af511fa.html)
- [The Role of Big Data and Data Warehousing in the Modern Analytics Ecosystem](https://www.sap.com/documents/2018/04/cce95c02-ff7c-0010-87a3-c30de2ffd8ff.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Big%20Data%20Services)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Big%20Data%20Services)

## Sample configuration of **SAP Big Data Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-bigdataservices** by configuring your `usecase.json` file.

### Using the service plan **standard** (Big Data Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-bigdataservices",
      "plan": "standard"
    }
  ]
}
```
