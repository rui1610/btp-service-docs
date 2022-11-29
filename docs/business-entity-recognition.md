# business-entity-recognition (Business Entity Recognition)

Business Entity Recognition helps you to detect and highlight any given type of named entity in unstructured text into pre-defined categories. You can use Business Entity Recognition, for example, to automatically extract the context from incoming emails with invoice inquiries, automating recurring tasks of answering to status and payment of invoices.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-BER

### Blog

- [Blog Posts](https://blogs.sap.com/tags/73555000100800002423/)

### Discovery Center

- [SAP Discovery Center - Business Entity Recognition](https://discovery-center.cloud.sap/serviceCatalog/business-entity-recognition)

### Documentation

- [Documentation](https://help.sap.com/ber)
- [Feature Scope Description](https://help.sap.com/doc/2df6cb90c5a44c8781400f4f58363448/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [Help Portal Product Page](https://help.sap.com/docs/Business_Entity_Recognition)
- [What's New](https://help.sap.com/docs/Business_Entity_Recognition/b43f8f61368d455793a241d2b10baeb2/44bba2ad2e5a44a0a986602082d88725.html)
- [Security](https://help.sap.com/docs/Business_Entity_Recognition/b43f8f61368d455793a241d2b10baeb2/45bd37e66b384732ba251bfffc268dff.html)
- [What Is Business Entity Recognition?](https://help.sap.com/docs/Business_Entity_Recognition/b43f8f61368d455793a241d2b10baeb2/894afc838ee54c0f8c7f7381a9dae27a.html)
- [API Documentation](https://help.sap.com/docs/Business_Entity_Recognition/b43f8f61368d455793a241d2b10baeb2/a04020d2bfb547988d75dd1e1a7fc20f.html)
- [Initial Setup](https://help.sap.com/docs/Business_Entity_Recognition/b43f8f61368d455793a241d2b10baeb2/dff15b3813b6459a92d4374eea695d9f.html)

### External

- [SAP AI Business Services - Business Entity Recognition](https://www.youtube.com/embed/VAZKt5kSeBY)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Business%20Entity%20Recognition)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Business%20Entity%20Recognition)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/Business_Entity_Recognition/b43f8f61368d455793a241d2b10baeb2/cd325febb97340848082c5c1349dc222.html)

### Tutorial

- [Use Custom Machine Learning Models to Process Unstructured Text](https://developers.sap.com/group.cp-aibus-business-entity-custom.html)
- [Use Pre-trained Machine Learning Models to Process Unstructured Text](https://developers.sap.com/group.cp-aibus-business-entity-detect.html)

## Sample configuration of **Business Entity Recognition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **business-entity-recognition** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "business-entity-recognition",
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
      "category": "SERVICE",
      "name": "business-entity-recognition",
      "plan": "standard"
    }
  ]
}
```
