# ibanservice (IBAN service)

Check validity and get details of given IBAN number.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- BC-ABS

### API Hub

- [Overview | IBAN Service | SAP API Business Hub](https://api.sap.com/package/ibanservice/overview)

### Discovery Center

- [Discovery Center]( https://discovery-center.cloud.sap/serviceCatalog/iban-service)
- [SAP Discovery Center - IBAN service](https://discovery-center.cloud.sap/serviceCatalog/iban-service)

### Documentation

- [Help Portal Product Page](https://help.sap.com/docs/IBAN_SERVICE)
- [Initial Setup](https://help.sap.com/docs/IBAN_SERVICE/9ba82223f71c46898e417c636cf24f56/a4fd370dd23f41989afde2646cfc06fb.html)
- [What's New](https://help.sap.com/docs/IBAN_SERVICE/9ba82223f71c46898e417c636cf24f56/ab033167c7494d8db9644a8a8f2d4553.html)
- [API Documentation](https://help.sap.com/docs/IBAN_SERVICE/9ba82223f71c46898e417c636cf24f56/c7cd3d07baf345df97a85e0eb450df61.html)
- [What is IBAN service?](https://help.sap.com/docs/IBAN_SERVICE/9ba82223f71c46898e417c636cf24f56/dc6d668b63dd456c866f91f312445cde.html)
- [Documentation](https://help.sap.com/viewer/product/IBAN_SERVICE/Latest/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=IBAN%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=IBAN%20service)

## Sample configuration of **IBAN service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ibanservice** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ibanservice",
      "plan": "default"
    }
  ]
}
```
