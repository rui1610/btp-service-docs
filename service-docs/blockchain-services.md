# blockchain-services (Blockchain Application Enablement)

Deliver blockchain-based services on any connected blockchain network.

## Service plan availability in regions

| Region | blockchain-hana-integration | blockchain-proof-of-history | blockchain-proof-of-state | blockchain-timestamp |
|--------|-----------------------------|-----------------------------|---------------------------|----------------------|
|  **eu10** | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ |

## Additional details

### Support components

- BC-BCS-VAS

### API Hub

- [Overview | SAP Blockchain Application Enablement | SAP API Business Hub](https://api.sap.com/package/SCPBlockchainServices/overview)

### Discovery Center

- [SAP Discovery Center - Blockchain Application Enablement](https://discovery-center.cloud.sap/serviceCatalog/blockchain-application-enablement)

### Documentation

- [What are Blockchain Application Enablement services?](https://help.sap.com/viewer/0a3ff4e76504461f91d0a6319904b8ca/BLOCKCHAIN/en-US)
- [Initial Setup](https://help.sap.com/viewer/13450f5d403d4a9b810fa50ec6665110/BLOCKCHAIN/en-US)
- [SAP Business Technology Platform Blockchain Application Enablement Help Portal Page](https://help.sap.com/docs/BLOCKCHAIN_APPLICATION_ENABLEMENT)
- [SAP Leonardo Blockchain Website](https://www.sap.com/products/leonardo/blockchain.html)

### Learning

- [OpenSAP: An Introduction to Blockchain](https://open.sap.com/courses/leo4)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/product-info.Hyperledger-Fabric--on-SAP-Cloud-Platform.b9fb18ba-a2dc-485b-ad59-79c30c15ec93.html)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **Blockchain Application Enablement** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **blockchain-services** by configuring your `usecase.json` file.

### Using the service plan **blockchain-hana-integration** (Blockchain Services)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-hana-integration",
      "parameters" : {
        "instructions": "Replace this JSON object with the SERVICE KEY for the blockchain technology to which this service must bind.",
        "documentation": "https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT",
        "type": "\u003c Used blockchain technology (hyperledger-fabric|multichain|quorum) \u003e"
      }
    }
  ]
}
```

### Using the service plan **blockchain-proof-of-history**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-proof-of-history",
      "parameters" : {
        "instructions": "Replace this JSON object with the SERVICE KEY for the blockchain technology to which this service must bind.",
        "documentation": "https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT",
        "type": "\u003c Used blockchain technology (hyperledger-fabric|multichain|quorum) \u003e"
      }
    }
  ]
}
```

### Using the service plan **blockchain-proof-of-state**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-proof-of-state",
      "parameters" : {
        "instructions": "Replace this JSON object with the SERVICE KEY for the blockchain technology to which this service must bind.",
        "documentation": "https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT",
        "type": "\u003c Used blockchain technology (hyperledger-fabric|multichain|quorum) \u003e"
      }
    }
  ]
}
```

### Using the service plan **blockchain-timestamp**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "blockchain-services",
      "plan": "blockchain-timestamp",
      "parameters" : {
        "instructions": "Replace this JSON object with the SERVICE KEY for the blockchain technology to which this service must bind.",
        "documentation": "https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT",
        "type": "\u003c Used blockchain technology (hyperledger-fabric|multichain|quorum) \u003e"
      }
    }
  ]
}
```
