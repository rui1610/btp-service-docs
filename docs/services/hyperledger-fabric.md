# hyperledger-fabric (Hyperledger Fabric on SAP BTP)

The Hyperledger Fabric service on SAP BTP lets you provision a Hyperledger Fabric node and join it to a network of nodes. Hyperledger Fabric supports Enterprise ready blockchain with smart contracts.

## Service plan availability in regions

| Region | backbone | channel | cyon | dev | node | testnet |
|--------|----------|---------|------|-----|------|---------|
|  **eu10** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Additional details
### API Hub

- [Overview | SAP Business Technology Platform - Blockchain Technologies | SAP API Business Hub](https://api.sap.com/package/SCPBlockchainTechnologies/overview)

### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Hyperledger%20Fabric)
- [Developing with Hyperledger Fabric](https://help.sap.com/viewer/81f693ad49a046cba506cc9bd51052d0/BLOCKCHAIN/en-US)
- [Initial Setup](https://help.sap.com/viewer/9d945c48156348aabea50a88d4661033/BLOCKCHAIN/en-US)
- [Provisioning a Node and Building a Hyperledger Fabric Network](https://help.sap.com/viewer/b45fb6803f784c0496b5ae7cd771e186/BLOCKCHAIN/en-US/0ab5eec6d51845f8849ef78dd6329a2c.html)
- [Understanding a Hyperledger Fabric Network](https://help.sap.com/viewer/b45fb6803f784c0496b5ae7cd771e186/BLOCKCHAIN/en-US/7700dfca1a9f4382823d197347acde87.html)
- [Creating and Managing Hyperledger Fabric Channels](https://help.sap.com/viewer/b45fb6803f784c0496b5ae7cd771e186/BLOCKCHAIN/en-US/d4456a38676b4c8e94c0588730010bfd.html)
- [Help Portal Product Page](https://help.sap.com/docs/HYPERLEDGER_FABRIC)
- [Documentation](https://help.sap.com/docs/MULTICHAIN)

### Learning

- [OpenSAP: An Introduction to Blockchain](https://open.sap.com/courses/leo4)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/product-info.Hyperledger-Fabric--on-SAP-Cloud-Platform.b9fb18ba-a2dc-485b-ad59-79c30c15ec93.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Hyperledger%20Fabric%20on%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Hyperledger%20Fabric%20on%20SAP%20BTP)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Hyperledger Fabric on SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hyperledger-fabric** by configuring your `usecase.json` file.

### Using the service plan **backbone**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan": "backbone"
    }
  ]
}
```

### Using the service plan **channel**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan": "channel",
      "parameters" : {
        "channelId": "\u003c the channel that should be imported \u003e",
        "channelSecret": "\u003c the channel secret \u003e",
        "comment": "\u003c user defined comment \u003e"
      }
    }
  ]
}
```

### Using the service plan **cyon**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan": "cyon",
      "parameters" : {
        "peerOrg": "\u003c peer org name \u003e",
        "peerAdmin": {"certificate": "\u003c peer user certificate\u003e ", "key": "\u003c peer user key \u003e"},
        "peers": ["\u003c peer url:port \u003e"],
        "peerTlsCaCertificate": "\u003c TLS CA certificate of the peer org \u003e",
        "peerCaCertificate": "\u003c (optional) peer ca certificate \u003e",
        "ordererOrg": "\u003c (optional) orderer org name \u003e",
        "ordererAdmin": {"certificate": "\u003c (optional) orderer user certificate\u003e ", "key": "\u003c (optional) orderer user key \u003e"},
        "orderers": ["\u003c (optional) orderer url:port \u003e"],
        "ordererTlsCaCertificate": "\u003c TLS CA certificate of the orderer org \u003e",
        "consortium": "\u003c name of the consortium \u003e",
        "peerCertificateAuthority": {"certificate": "\u003c (optional) certificate authority certificate\u003e ", "certificateChain": "\u003c (optional) certificate authority certificate chain \u003e", "key": "\u003c (optional) certificate authority private key \u003e"}
      }
    }
  ]
}
```

### Using the service plan **dev**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan": "dev"
    }
  ]
}
```

### Using the service plan **node**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan": "node"
    }
  ]
}
```

### Using the service plan **testnet**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hyperledger-fabric",
      "plan": "testnet"
    }
  ]
}
```
