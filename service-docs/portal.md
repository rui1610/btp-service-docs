# portal (SAP Cloud Portal service)

SAP Business Technology Platform Portal lets you build digital experience portals for employees, customers, and partners. You can streamline access to business data so that your employees can execute their daily business tasks securely, from any device.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **eu30** | ✅ |
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- EP-CPP-CF-LND

### API Hub

- [Overview | SAP Cloud Portal Service | SAP API Business Hub](https://api.sap.com/package/SAPCLOUDPLATFORMPORTAL/overview)

### Documentation

- [Documentation](https://help.sap.com/viewer/8422cb487c2146999a2a7dab9cc85cf7/Cloud/en-US)
- [Documentation](https://help.sap.com/docs/BTP/ad4b9f0b14b0458cad9bd27bf435637d/5798687972fd4c2bace31c65b47f5587.html)
- [Documentation](https://help.sap.com/viewer/product/Launchpad_Service/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/product/Portal_Service/1.0/en-US)
- [Documentation](https://help.sap.com/viewer/product/Portal_Service/latest/en-US)
- [Documentation](https://help.sap.com/docs/WZ)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/ux/cloud-portal.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Cloud%20Portal%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Cloud%20Portal%20service)

## Sample configuration of **SAP Cloud Portal service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **portal** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "portal",
      "plan": "standard"
    }
  ]
}
```
