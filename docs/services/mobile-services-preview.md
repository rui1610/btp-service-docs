# mobile-services-preview (Mobile Services, preview)

Mobile Services Preview gives you an opportunity to test new features a couple of weeks before their production release of Mobile Services. Mobile Services Preview is not intended as a production environment. Use Mobile Services Preview to provide mobile access to enterprise information. Key features include app content lifecycle management, push notifications and support for offline apps, app security, app monitoring and usage reporting. Mobile Services Preview can be used for native built apps, Mobile Development Kit apps and SAP Mobile Cards. Get started by clicking on the Support link below.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/mobile-services)

### Documentation

- [Documentation](https://developers.sap.com/mobile)
- [Documentation](https://help.sap.com/docs/SAP_MOBILE_SERVICES)
- [Documentation](https://mobile-service-cockpit-web-preview.cfapps.eu10.hana.ondemand.com)

## Sample configuration of **Mobile Services, preview** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-services-preview** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-services-preview",
      "plan": "standard"
    }
  ]
}
```
