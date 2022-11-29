# application-logs (SAP Application Logging service for SAP BTP)

In the Cloud Foundry environment, the SAP Application Logging service for SAP BTP lets you stream logs of bound applications to a central application logging stack. SAP Application Logging service for SAP BTP uses Elastic Stack to store and visualize your application log data. To fully leverage this service, please also consider using one of SAP&apos;s open source libraries (for example, cf-java-logging-support or cf-nodejs-logging-support). In the Neo environment, the application logging allows you to configure loggers for Java applications through the cockpit or the console client. Furthermore, you can retrieve default trace logs, HTTP access logs, and garbage collection logs for the last 7 days.

## Service plan availability in regions

| Region | large | lite | standard |
|--------|-------|------|----------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ |
|  **in30** | ✅ | | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CF-APPLOG

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/application-logging-service)
- [SAP Discovery Center - Application Logging Service](https://discovery-center.cloud.sap/serviceCatalog/application-logging-service)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/2992cdb21d194bab9926f7bb054f8b29/)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)
- [Application Logging for the Cloud Foundry Environment](https://help.sap.com/docs/BTP/ee8e8a203e024bbb8c8c2d03fce527dc/68454d44ad41458788959485a24305e2.html)
- [Help Portal Product Page](https://help.sap.com/docs/APPLICATION_LOGGING)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Application%20Logging%20service%20for%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Application%20Logging%20service%20for%20SAP%20BTP)

## Sample configuration of **SAP Application Logging service for SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **application-logs** by configuring your `usecase.json` file.

### Using the service plan **large**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "application-logs",
      "plan": "large"
    }
  ]
}
```

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "application-logs",
      "plan": "lite"
    }
  ]
}
```

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "application-logs",
      "plan": "standard"
    }
  ]
}
```
