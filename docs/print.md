# print (SAP Print service)

Manage print queues, connect print clients and monitor print status

## Service plan availability in regions

| Region | receiver | sender |
|--------|----------|--------|
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |

## Additional details

### Support components

- BC-CCM-PRN-OM-SCP

### API Hub

- [Overview | SAP Print Service | SAP API Business Hub](https://api.sap.com/package/SCPPrintService/overview)

### Discovery Center

- [SAP Discovery Center - Print Service](https://discovery-center.cloud.sap/serviceCatalog/print-service)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/4e8b1f3ae56d4de2a60d9b60685fe83a/SHIP/en-US/8c0d3ecb69d64505b9fcd4c2086fc8b7.pdf)
- [Documentation](https://help.sap.com/viewer/07d0692a5a994703992d7538ad78d54b/SHIP/en-US)
- [Administration Guide for SAP Print Service](https://help.sap.com/viewer/07d0692a5a994703992d7538ad78d54b/SHIP/en-US/5abafd8af72e4a88a4cfaa39ca9b8e2b.html)
- [End User Guide for SAP Print Service](https://help.sap.com/viewer/7615de0949ce441d8bc5df7725a6bfc6/SHIP/en-US/f9b7721c83724178a87702d8bf1eb464.html)
- [What is SAP Print service?](https://help.sap.com/viewer/9fd06c162b874c3bac7ef214be7fdb9a/SHIP/en-US)
- [Documentation](https://help.sap.com/viewer/9fd06c162b874c3bac7ef214be7fdb9a/SHIP/en-US/553c9ca63cd84537b140d2aa547b8c02.html)
- [Initial Setup](https://help.sap.com/viewer/9fd06c162b874c3bac7ef214be7fdb9a/SHIP/en-US/f24202b39b614bd6b81c4f8513d0244f.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SCP_PRINT_SERVICE/SHIP/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Print%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Print%20service)

### Support

- [Support](https://launchpad.support.sap.com)

## Sample configuration of **SAP Print service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **print** by configuring your `usecase.json` file.

### Using the service plan **receiver**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "print",
      "plan": "receiver"
    }
  ]
}
```

### Using the service plan **sender**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "print",
      "plan": "sender"
    }
  ]
}
```
