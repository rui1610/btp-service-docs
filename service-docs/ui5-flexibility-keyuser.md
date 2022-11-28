# ui5-flexibility-keyuser (UI5 flexibility for key users)

The UI5 flexibility service for key users lets you provide UI adaptation capabilites for your UI5 applications on Cloud Foundry. Users of your applications can change the user interface of your applications in an upgrade-safe and modification-free way, without affecting any other customer.

## Service plan availability in regions

| Region | free | keyuser |
|--------|------|---------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | | ✅ |
|  **in30** | | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- CA-UI5-FL-CLS

### API Hub

- [Overview | UI5 Flexibility for Key Users | SAP API Business Hub](https://api.sap.com/package/UI5FlexibilityForKeyUsers/overview)

### Blog

- [Understanding the Nuts and Bolts of SAP Fiori Development in the Cloud Foundry Environment](https://blogs.sap.com/2020/06/22/understanding-the-nuts-and-bolts-of-sap-fiori-development-for-cloud-foundry/)

### Discovery Center

- [SAP Discovery Center - UI5 flexibility for key users](https://discovery-center.cloud.sap/serviceCatalog/ui5-flexibility-for-key-users)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/d6b262dba5db484ea0b0ea1fcb53edd0/)
- [Documentation](https://help.sap.com/docs/UI5_FLEXIBILITY_KEY_USER/0f8b49c4dfc94bc0bda25a19aa93d5b2/3896117fb42f4602953c646090bc9447.html)
- [Documentation](https://help.sap.com/docs/UI5_FLEXIBILITY_KEY_USER)
- [Initial Setup](https://help.sap.com/docs/BTP/0f8b49c4dfc94bc0bda25a19aa93d5b2/365187a3cb1b4579a910532aa3c48ba2.html)
- [What Is UI5 Flexibility for Key Users?](https://help.sap.com/docs/BTP/0f8b49c4dfc94bc0bda25a19aa93d5b2/a0aa4a0d62834a62b827fc97929405ba.html)
- [What's New](https://help.sap.com/docs/BTP/0f8b49c4dfc94bc0bda25a19aa93d5b2/fcca383099bd40f48bcbb6ad378ea2a9.html)

### External

- [What is SAPUI5?](https://www.youtube.com/embed/6_CQYtmRJNg)
- [SAPUI5 Flexibility - Key User Adaptation](https://www.youtube.com/embed/VrFVB1b4kAI)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=UI5%20flexibility%20for%20key%20users)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=UI5%20flexibility%20for%20key%20users)

## Sample configuration of **UI5 flexibility for key users** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ui5-flexibility-keyuser** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ui5-flexibility-keyuser",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **keyuser**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ui5-flexibility-keyuser",
      "plan": "keyuser"
    }
  ]
}
```
