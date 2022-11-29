# workcalendar (Work Calendar)

Get details of factory calendar such as weekday, holiday, workday for a country.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- BC-ABS

### API Hub

- [Overview | Work Calendar | SAP API Business Hub](https://api.sap.com/package/workcalendar/overview)

### Discovery Center

- [SAP Discovery Center - Work Calendar](https://discovery-center.cloud.sap/serviceCatalog/work-calendar)

### Documentation

- [Help Portal Product Page](https://help.sap.com/docs/WORK_CALENDAR)
- [API Documentation](https://help.sap.com/docs/WORK_CALENDAR/7c89122441b241e9853dd422bdf6604d/21b81723d30645c4977804085c40db52.html)
- [What's New](https://help.sap.com/docs/WORK_CALENDAR/7c89122441b241e9853dd422bdf6604d/4f551ad2f46a46ac8cf75edb37444041.html)
- [Initial Setup](https://help.sap.com/docs/WORK_CALENDAR/7c89122441b241e9853dd422bdf6604d/7f624c72f2364bdb9fb2e3d9afe4b5a4.html)
- [What is Work Calendar?](https://help.sap.com/docs/WORK_CALENDAR/7c89122441b241e9853dd422bdf6604d/b755e79cdf764579bbad4cca9953c018.html)
- [Documentation](https://help.sap.com/viewer/product/WORK_CALENDAR/Latest/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Work%20Calendar)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Work%20Calendar)

## Sample configuration of **Work Calendar** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **workcalendar** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "workcalendar",
      "plan": "default"
    }
  ]
}
```
