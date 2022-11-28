# html5-apps-repo (SAP HTML5 Application Repository service for SAP BTP)

The HTML5 Application Repository service enables central storage of HTML5 applications in SAP BTP. In runtime, the service enables the consuming application, typically the application router, to access HTML5 application static content in a secure and efficient manner.

## Service plan availability in regions

| Region | app-host | app-runtime |
|--------|----------|-------------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **ch20** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CF-HTML5

### Discovery Center

- [SAP Discovery Center - HTML5 Application Repository Service](https://discovery-center.cloud.sap/serviceCatalog/html5-application-repository-service)

### Documentation

- [What is SAP HTML5 Applications in the Cloud Foundry Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/11d77aa154f64c2e83cc9652a78bb985.html)
- [HTML5 Application Repository Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/f8520f572a6445a7bfaff4a1bbcbe60a.html)
- [Help Portal Product Page](https://help.sap.com/docs/HTML5_APPLICATIONS)

### Onboarding

- [Tutorial: Onboarding](https://developers.sap.com/mission.cp-starter-ibpm-employeeonboarding.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20HTML5%20Application%20Repository%20service%20for%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20HTML5%20Application%20Repository%20service%20for%20SAP%20BTP)

### Support

- [Getting Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/9220a2fd35d84c888c0ae870ca62bfb7.html)
- [Troubleshooting](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/ae1d53e5fbe14383bfafe690f52711d7.html)

## Sample configuration of **SAP HTML5 Application Repository service for SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **html5-apps-repo** by configuring your `usecase.json` file.

### Using the service plan **app-host**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "html5-apps-repo",
      "plan": "app-host"
    }
  ]
}
```

### Using the service plan **app-runtime**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "html5-apps-repo",
      "plan": "app-runtime"
    }
  ]
}
```
