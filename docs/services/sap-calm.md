# sap-calm (SAP Cloud ALM, memory extension)

This is memory extension for SAP Cloud ALM.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **eu20** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- SV-CLM-OP

### API Hub

- [Overview |  SAP Cloud ALM | SAP API Business Hub](https://api.sap.com/package/SAPCloudALM/overview)

### Discovery Center

- [SAP Discovery Center - SAP Cloud ALM, memory extension](https://discovery-center.cloud.sap/serviceCatalog/sap-cloud-alm-memory-extension)

### Documentation

- [Help Portal: about SAP Cloud ALM, memory extension](https://help.sap.com/viewer/08879d094f3b4de3ac67832f4a56a6de/latest/en-US/94cd95e1b8454b5180d6a3daeccb1500.html)
- [What's New](https://help.sap.com/viewer/604f6e2484984622a01ac1e5aa9415a1/latest/en-US)
- [Documentation](https://help.sap.com/viewer/product/CloudALM)
- [Documentation](https://support.sap.com/en/alm/sap-cloud-alm.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Cloud%20ALM%2C%20memory%20extension)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Cloud%20ALM%2C%20memory%20extension)

## Sample configuration of **SAP Cloud ALM, memory extension** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-calm** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-calm",
      "plan": "default"
    }
  ]
}
```
