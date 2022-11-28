# document-classification (Document Classification)

Document Classification helps you to automate the management and processing of large amounts of business documents by applying machine learning. Based on customer specific classification models, Document Classification can be utilized in a wide range of business scenarios and adapted to special requirements. Document Classification is targeting organizations and business units struggling with the fast, economic, high quality and efficient processing of documents used in critical business processes like Enterprise Mail-Inbox Processing, Contract Management or Invoice Processing.

## Service plan availability in regions

| Region | blocks_of_100 | default |
|--------|---------------|---------|
|  **eu10** | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-BDP

### Blog

- [Blog Posts](https://blogs.sap.com/tags/73555000100800002353/)

### Discovery Center

- [SAP Discovery Center - Document Classification](https://discovery-center.cloud.sap/serviceCatalog/document-classification)

### Documentation

- [Help Portal Product Page](https://help.sap.com/dc)
- [Feature Scope Description](https://help.sap.com/doc/1a40d554babe4497ab789f3217263703/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [What Is Document Classification?](https://help.sap.com/viewer/ca60cd2ed44f4261a3ae500234c46f37/SHIP/en-US)
- [Security](https://help.sap.com/viewer/ca60cd2ed44f4261a3ae500234c46f37/SHIP/en-US/2d0ee48527ba4621bc77e2e0e55aaa3d.html)
- [API Documentation](https://help.sap.com/viewer/ca60cd2ed44f4261a3ae500234c46f37/SHIP/en-US/c1045a561faf4ba0ae2b0e7713f5e6c4.html)
- [What's New](https://help.sap.com/viewer/ca60cd2ed44f4261a3ae500234c46f37/SHIP/en-US/d674818c609e4a61a138d94c1b82f6ed.html)
- [Initial Setup](https://help.sap.com/viewer/ca60cd2ed44f4261a3ae500234c46f37/latest/en-US/88bdee94c7c94bc99de8484f5c2db04a.html)
- [Blueprint Guide](https://www.sap.com/documents/2020/10/64576205-b97d-0010-87a3-c30de2ffd8ff.html)

### External

- [SAP AI Business Services - Document Classification](https://www.youtube.com/embed/2VSYHBRBJzo)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Document%20Classification)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Document%20Classification)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/viewer/ca60cd2ed44f4261a3ae500234c46f37/SHIP/en-US/7030780277ff4ec9a3145f07a3ccd5c7.html)

### Tutorial

- [Use Machine Learning to Classify Documents (Enterprise Account)](https://developers.sap.com/group.cp-aibus-classify-documents-enterprise.html)

## Sample configuration of **Document Classification** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-classification** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "document-classification",
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
      "name": "document-classification",
      "plan": "default"
    }
  ]
}
```
