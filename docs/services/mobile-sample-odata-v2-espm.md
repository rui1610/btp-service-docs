# mobile-sample-odata-v2-espm (Mobile Sample OData)

Mobile Sample OData

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **br10** | ✅ |
|  **eu10** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/468990a67780424a9e66eb096d4345bb/1c2e51a24361487f8b0649702d59dd0f.html)
- [Documentation](https://mobile-service-cockpit-web.cfapps.ap10.hana.ondemand.com)
- [Documentation](https://mobile-service-cockpit-web.cfapps.ap11.hana.ondemand.com)
- [Documentation](https://mobile-service-cockpit-web.cfapps.br10.hana.ondemand.com)
- [Documentation](https://mobile-service-cockpit-web.cfapps.eu10.hana.ondemand.com)
- [Documentation](https://mobile-service-cockpit-web.cfapps.jp10.hana.ondemand.com)
- [Documentation](https://mobile-service-cockpit-web.cfapps.us10.hana.ondemand.com)

## Sample configuration of **Mobile Sample OData** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **mobile-sample-odata-v2-espm** by configuring your `usecase.json` file.

### Using the service plan **standard** (Mobile Sample OData v2 ESPM Service is a sample OData service used for development and testing)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "mobile-sample-odata-v2-espm",
      "plan": "standard"
    }
  ]
}
```
