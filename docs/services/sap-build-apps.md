# sap-build-apps (SAP Build Apps)

SAP Build Apps is a full stack no-code development platform for creating Web and native mobile applications. Please note that an instance of Cloud Identity Services is required to successfully create a subscription. See Documentation for more information.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **eu10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/sap-build-apps)
- [SAP Discovery Center - SAP Build Apps](https://discovery-center.cloud.sap/serviceCatalog/sap-build-apps)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/2acecfb777684ce5a0a8a75fd78caffb/Latest/en-US/2a23b2bcd9084d83b9a8e76b2d1b4372.pdf)
- [Help Portal Product Page](https://help.sap.com/docs/BUILD_APPS)
- [Initial Setup](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/39a35cf3447241509f4dbbd19a96dbc0.html)
- [What is SAP Build Apps](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/daece9f87abf4f7187a14ae0b1f8b2ab.html)
- [What's New](https://help.sap.com/whats-new/cf0cb2cb149647329b5d02aa96303f56?Component=SAP%20Build%20Apps)

### Learning

- [SAP Build Apps Sandbox](https://groups.community.sap.com/t5/sap-builders-blog-posts/announcing-the-sap-build-apps-sandbox/ba-p/128821)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Build%20Apps)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Build%20Apps)
- [Community Content](https://community.sap.com/topics/build-apps?ct=blog&lng=en&tab=content)

### Support

- [Support At SAP](https://support.sap.com/)

## Sample configuration of **SAP Build Apps** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-build-apps** by configuring your `usecase.json` file.

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sap-build-apps",
      "plan": "free"
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
      "category": "APPLICATION",
      "name": "sap-build-apps",
      "plan": "standard"
    }
  ]
}
```
