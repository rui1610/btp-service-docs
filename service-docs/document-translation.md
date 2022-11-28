# document-translation (Document Translation)

Provides an API that allows you to translate documents of various formats into multiple languages.

## Service plan availability in regions

| Region | default | free |
|--------|---------|------|
|  **eu10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- LOD-TH

### API Hub

- [Document translation @SAP API Business Hub](https://api.sap.com/api/documenttranslation/overview)
- [Overview | SAP Translation Hub | SAP API Business Hub](https://api.sap.com/package/SAPTranslationHub/overview)

### Blog

- [Blogs in the Community](https://blogs.sap.com/tags/73555000100800000086/)

### Discovery Center

- [SAP Discovery Center - Document Translation service](https://discovery-center.cloud.sap/serviceCatalog/document-translation-service)
- [SAP Discovery Center - SAP Translation Hub](https://discovery-center.cloud.sap/serviceCatalog/sap-translation-hub)

### Documentation

- [Translation Workflow Scenarios](https://help.sap.com/docs/SAP_TRANSLATION_HUB/cf5f2b0b615b469095f8eaa7772d5c1e/da544d140f39451eae992d1b1246f98b.html)
- [Integration Scenarios](https://help.sap.com/docs/SAP_TRANSLATION_HUB/ed6ce7a29bdd42169f5f0d7868bce6eb/0e5c4dff1edd47569300327d71e19e62.html)
- [Feature Scope Description](https://help.sap.com/http.svc/rc/d9793b3d4a0b4d56af33efd7c4fe9eb0/Cloud/en-US/FeatureScopeDescription_en.pdf)
- [Initial Setup](https://help.sap.com/docs/BTP/9f73362817cd48339dd8a6acba160f7f/100d41cc6ea94876ae95d6a6a584e9f7.html)
- [What is Document Translation service](https://help.sap.com/docs/BTP/9f73362817cd48339dd8a6acba160f7f/a2dedd7861624a1a82d7ec7ea431a8e4.html)
- [When to use what: SAP Translation Hub and Document Translation service](https://help.sap.com/docs/BTP/9f73362817cd48339dd8a6acba160f7f/c043634dee1541ca90875b67c551e715.html)
- [Documentation](https://help.sap.com/docs/BTP/9f73362817cd48339dd8a6acba160f7f/c07bd4ee447b477b9ccb31b3abf5dae3.html)
- [API Documentation](https://help.sap.com/docs/BTP/9f73362817cd48339dd8a6acba160f7f/eae71b1e255a4e11abdb7a42436cfd3f.html)
- [What is SAP Translation Hub](https://help.sap.com/viewer/ed6ce7a29bdd42169f5f0d7868bce6eb/Cloud/en-US)
- [Getting Started](https://help.sap.com/docs/BTP/ed6ce7a29bdd42169f5f0d7868bce6eb/2ef95bf1a22a42bc90fc757bec701db0.html)
- [API Documentation](https://help.sap.com/docs/BTP/ed6ce7a29bdd42169f5f0d7868bce6eb/9ce1acde6ee04f08a06239a881f42b54.html)
- [Documentation](https://help.sap.com/docs/BTP/ed6ce7a29bdd42169f5f0d7868bce6eb/b33a4ed0f6914c7291cf788752a977ac.html)
- [What's New](https://help.sap.com/docs/BTP/ed6ce7a29bdd42169f5f0d7868bce6eb/fdf5bca0d7fc45a8896f401dd391043f.html)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_TRANSLATION_HUB)
- [Documentation](https://news.sap.com/2018/05/sap-translation-hub-helps-companies-address-global-markets-more-easily/)

### Learning

- [openSAP Course: SAP Translation Hub in a Nutshell](https://open.sap.com/courses/sth1)
- [Learning Journey: SAP Translation Hub on SAP Business Technology Platform](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/ed7acf8ccec846fb8ba50a4f74b94928.html)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Document%20Translation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Document%20Translation)

### Tutorial

- [Tutorials](https://help.sap.com/docs/SAP_TRANSLATION_HUB/cf5f2b0b615b469095f8eaa7772d5c1e/72f9d25fb8cd4168a912af5e0cf75df9.html)

## Sample configuration of **Document Translation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-translation** by configuring your `usecase.json` file.

### Using the service plan **default** (Default)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-translation",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-translation",
      "plan": "free"
    }
  ]
}
```
