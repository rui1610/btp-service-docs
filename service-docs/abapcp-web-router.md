# abapcp-web-router (Web access for ABAP)

Get web access to your instances in the ABAP Environment including access to administrative UIs 

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/98928b0941294c74b946cdcefca9b047.html)

## Sample configuration of **Web access for ABAP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **abapcp-web-router** by configuring your `usecase.json` file.

### Using the service plan **default** (Web Access for ABAP Environment)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "abapcp-web-router",
      "plan": "default"
    }
  ]
}
```
