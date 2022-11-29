# theming (UI theme designer)

The UI theme designer lets you apply your corporate branding to applications built with SAP UI technologies. You can make changes to theme templates supplied by SAP to create custom themes that use your own color scheme, background images, and company logo. You can apply a custom theme to various SAP UI clients and technologies. Additionally, you can include your own custom CSS files without having to modify any of your applications.

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
|  **ch20** | ✅ |
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

### Discovery Center

- [SAP Discovery Center - UI theme designer](https://discovery-center.cloud.sap/serviceCatalog/ui-theme-designer)

### Documentation

- [Feature Scope Description](https://help.sap.com/http.svc/rc/d5f7a7837e96482796accb9ce75f7518/Cloud/en-US/loio1ff9350a0b864ae698037a1f5c2f525d.pdf)
- [Documentation](https://help.sap.com/viewer/09f6818d8e064537973102d6289e2aca/Cloud)
- [Initial Setup](https://help.sap.com/docs/BTP/09f6818d8e064537973102d6289e2aca/6803e8c72cce432d9d22d35acd7d5e7d.html)
- [Onboarding](https://help.sap.com/docs/BTP/09f6818d8e064537973102d6289e2aca/827fd85f82b446cba35c2725d8830531.html)
- [UI Theme Designer](https://help.sap.com/docs/BTP/09f6818d8e064537973102d6289e2aca/935325fb130d41449362181fb6020dd0.html)
- [What's New](https://help.sap.com/docs/BTP/09f6818d8e064537973102d6289e2aca/d756396894ef4f42b62b39efc00ffa83.html)
- [Help Portal Product Page](https://help.sap.com/docs/UI_THEME_DESIGNER)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/ux/ui-theme-designer.html)

### SAP Community

- [UI Theme Designer Community](https://community.sap.com/topics/ui-theme-designer)
- [SAP Community](http://www.sap.com/community/topic/ui-theme-designer.html)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=UI%20theme%20designer)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=UI%20theme%20designer)

### Support

- [Getting Support](https://help.sap.com/docs/BTP/09f6818d8e064537973102d6289e2aca/71e51058c0964399b88ec1ec740c1044.html)

## Sample configuration of **UI theme designer** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **theming** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "theming",
      "plan": "standard"
    }
  ]
}
```
