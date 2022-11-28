# sap-document-information-extraction (Document Information Extraction)

Document Information Extraction helps you to process various documents that have content in headers and tables. You can use the extracted information, for example, to automatically process payables, invoices, or payment notes while making sure that invoices and payables match.

## Service plan availability in regions

| Region | blocks_of_100 | default | free |
|--------|---------------|---------|------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-BDP

### Discovery Center

- [SAP Discovery Center - Document Information Extraction](https://discovery-center.cloud.sap/serviceCatalog/document-information-extraction)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/a08fc1abaa294506afafb3f7c890cf87/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [Help Portal Product Page](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION)
- [Initial Setup](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/0d68dc0002f0484ba25f85f3170166e0.html)
- [Using the Document Information Extraction UI](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/817f7747eac94ec7b1f271ed203e24d1.html)
- [Security](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/8ce36ec689c94df2a6806e4648f7cd94.html)
- [What Is Document Information Extraction?](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/dc933b03badd406086fd1dee7708cc9d.html)
- [API Reference](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/ded7d34e60f1422ba2e04e892a7f0e25.html)
- [What's New](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/e6d1122300d3440bb3277f18adca0557.html)
- [Documentation](https://help.sap.com/dox)

### External

- [SAP AI Business Services - Document Information Extraction](https://www.youtube.com/embed/Gj4KS3xKBC0)
- [Document Information Extraction from SAP – Taking Document Processing to the Next Level](https://www.youtube.com/embed/Ojg447dM66E)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Document%20Information%20Extraction)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Document%20Information%20Extraction)
- [SAP Community Topic Page](https://community.sap.com/topics/document-information-extraction)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/DOCUMENT_INFORMATION_EXTRACTION/5fa7265b9ff64d73bac7cec61ee55ae6/7ddd52320bae4d539393a4365b9f6aa6.html)
- [Support](https://help.sap.com/viewer/5fa7265b9ff64d73bac7cec61ee55ae6/SHIP/en-US/7ddd52320bae4d539393a4365b9f6aa6.html)

### Tutorial

- [Shape Machine Learning to Process Custom Business Documents](https://developers.sap.com/mission.btp-aibus-shape-ml-custom.html)
- [Shape Machine Learning to Process Standard Business Documents](https://developers.sap.com/mission.btp-aibus-shape-ml.html)
- [Use Machine Learning to Extract Information from Business Documents and Enrich Data](https://developers.sap.com/mission.cp-aibus-extract-document-enrich-data.html)
- [Use Machine Learning to Process Business Documents](https://developers.sap.com/mission.cp-aibus-extract-document-service.html)

## Sample configuration of **Document Information Extraction** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-document-information-extraction** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-document-information-extraction",
      "plan": "blocks_of_100"
    }
  ]
}
```

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sap-document-information-extraction",
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
      "name": "sap-document-information-extraction",
      "plan": "free"
    }
  ]
}
```
