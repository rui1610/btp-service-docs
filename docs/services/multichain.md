# multichain (MultiChain on SAP BTP)

The MultiChain service lets you create, delete, monitor and maintain individual MultiChain nodes and connect them to a blockchain network.

## Service plan availability in regions

| Region | cyon | large | medium | small |
|--------|------|-------|--------|-------|
|  **eu10** | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=MultiChain)
- [Initial Setup](https://help.sap.com/viewer/15cb4580694c4d119793f0d3e9b8a32b/BLOCKCHAIN/en-US)
- [Creating a MultiChain Service Instance](https://help.sap.com/viewer/215f45a9aee1419095188f35ab7aaf38/BLOCKCHAIN/en-US/0183c6479c47427ab6257bd37ab8bee3.html)
- [Creating MultiChain Service Keys and Accessing APIs](https://help.sap.com/viewer/215f45a9aee1419095188f35ab7aaf38/BLOCKCHAIN/en-US/23819474549a4257975d482ed24c7e04.html)
- [Building a MultiChain Network](https://help.sap.com/viewer/215f45a9aee1419095188f35ab7aaf38/BLOCKCHAIN/en-US/2c0cc96ae73346d190581dad4e1c0e0e.html)
- [Help Portal Product Page](https://help.sap.com/docs/MULTICHAIN)

### Learning

- [openSAP: An Introduction to Blockchain](https://open.sap.com/courses/leo4)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/dmp/capabilities/us/product/MultiChain-on-SAP-Cloud-Platform/c091cbd8-bb96-447a-81ca-5f5555996b02)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=MultiChain%20on%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=MultiChain%20on%20SAP%20BTP)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

### Tutorial

- [Hands on Example: Asset Transfer Scenario Using Multiple Adddresses on your Node](https://help.sap.com/viewer/191c314034324f75b9e783fbb4fe9858/BLOCKCHAIN/en-US)
- [Hands on Example: Data Storage and Retrieval Scenario Using MultiChain Streams](https://help.sap.com/viewer/a420aed7df4343c29ce7587bbed77f11/BLOCKCHAIN/en-US)

## Sample configuration of **MultiChain on SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **multichain** by configuring your `usecase.json` file.

### Using the service plan **cyon**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "cyon"
    }
  ]
}
```

### Using the service plan **large**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "large"
    }
  ]
}
```

### Using the service plan **medium**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "medium"
    }
  ]
}
```

### Using the service plan **small**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "multichain",
      "plan": "small"
    }
  ]
}
```
