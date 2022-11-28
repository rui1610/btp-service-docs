# sap-build-apps (SAP Build Apps)

SAP Build Apps is a full stack no-code development platform for creating Web and native mobile applications.

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
- [What is SAP Build Apps](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/daece9f87abf4f7187a14ae0b1f8b2ab.html)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### Onboarding

- [Tutorial: Onboarding](https://docs.appgyver.com/docs/onboarding)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Build%20Apps)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Build%20Apps)

### Support

- [Support At SAP](https://support.sap.com/)

## Sample configuration of **SAP Build Apps** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-build-apps** by configuring your `usecase.json` file.

### Using the service plan **free**

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
