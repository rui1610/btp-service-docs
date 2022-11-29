# sdm-repository (SAP Document Management service)

Use a CMIS complaint repository provided internally with all SAP Document Management service capabilities.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
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
|  **eu30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details
### Documentation

- [Feature Scope Description](https://help.sap.com/doc/146a6693d3734dc58fbd8422dc5931da/)
- [What's New](https://help.sap.com/docs/BTP/42ccfedfbfe545bd821654a6a1cb6513/30aedee9e60547c9967c718e86ad76c1.html)
- [Managing a Repository with Console Client Commands](https://help.sap.com/docs/BTP/b0cc1109d03c4dc299c215871eed8c42/269aa860ed074550ada99cd89780c5cf.html)
- [Consuming the Document Service (HTML5 Applications)](https://help.sap.com/docs/BTP/b0cc1109d03c4dc299c215871eed8c42/c707d9ae9af54341908675d29e92d2f6.html)
- [Consuming the Document Service (Java)](https://help.sap.com/docs/BTP/b0cc1109d03c4dc299c215871eed8c42/e587c8d4bb57101494d980c9e41d0072.html)
- [What is Document Service](https://help.sap.com/docs/BTP/b0cc1109d03c4dc299c215871eed8c42/e60b7e45bb57101487a881c7c5487778.html)
- [Documentation](https://help.sap.com/docs/DOCUMENT_MANAGEMENT)
- [Help Portal Product Page](https://help.sap.com/docs/DOCUMENT_SERVICE)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Document%20Management%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Document%20Management%20service)

## Sample configuration of **SAP Document Management service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sdm-repository** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "sdm-repository",
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
      "name": "sdm-repository",
      "plan": "standard"
    }
  ]
}
```
