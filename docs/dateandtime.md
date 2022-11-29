# dateandtime (Date and Time)

Get default date format for a given country, timezone details and time difference between two provided time values.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- BC-ABS

### API Hub

- [Overview | Date and Time | SAP API Business Hub](https://api.sap.com/package/dateandtime/overview)

### Discovery Center

- [SAP Discovery Center - Date and Time](https://discovery-center.cloud.sap/serviceCatalog/date-and-time)

### Documentation

- [Help Portal Product Page](https://help.sap.com/docs/DATE_AND_TIME)
- [What's New](https://help.sap.com/docs/DATE_AND_TIME/17d7e70611c64e1182ebe7f0079c9e63/272475ef4c1b49d0af55ab452db9e53e.html)
- [What is Date and Time?](https://help.sap.com/docs/DATE_AND_TIME/17d7e70611c64e1182ebe7f0079c9e63/6df6e8f7b6a3458ab131b05cb267eea4.html)
- [Initial Setup](https://help.sap.com/docs/DATE_AND_TIME/17d7e70611c64e1182ebe7f0079c9e63/9c2f6f839cf94c88881e59e24b4ea82a.html)
- [API Documentation](https://help.sap.com/docs/DATE_AND_TIME/17d7e70611c64e1182ebe7f0079c9e63/f90a76b22b83444b94e10538a5c3eecf.html)
- [Documentation](https://help.sap.com/viewer/product/DATE_AND_TIME/Latest/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Date%20and%20Time)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Date%20and%20Time)

## Sample configuration of **Date and Time** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dateandtime** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "dateandtime",
      "plan": "default"
    }
  ]
}
```
