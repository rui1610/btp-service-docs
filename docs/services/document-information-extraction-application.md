# document-information-extraction-application (Document Information Extraction UI)

UI Application to upload document for extraction to Document Information Extraction and correct the results.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **ap10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- CA-ML-BDP

### Documentation

- [Documentation](https://help.sap.com/viewer/product/DOCUMENT_INFORMATION_EXTRACTION)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Document%20Information%20Extraction%20UI)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Document%20Information%20Extraction%20UI)

## Sample configuration of **Document Information Extraction UI** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **document-information-extraction-application** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "document-information-extraction-application",
      "plan": "default"
    }
  ]
}
```
