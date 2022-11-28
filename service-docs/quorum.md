# quorum (Quorum on SAP BTP)

The Quorum service lets you create, delete, monitor and maintain individual Quorum nodes and connect them to a blockchain network.

## Service plan availability in regions

| Region | cyon | dev | testnet |
|--------|------|-----|---------|
|  **eu10** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [Initial Setup](https://help.sap.com/viewer/3b2854f7840e420ab5a121e2a4d420c3/BLOCKCHAIN/en-US)
- [Help Portal Product Page](https://help.sap.com/docs/QUORUM)

### Learning

- [OpenSAP: An Introduction to Blockchain](https://open.sap.com/courses/leo4)

### Marketing

- [Learn more about this service and how to purchase it.]()

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Quorum%20on%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Quorum%20on%20SAP%20BTP)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

### Tool

- [Quorum Dashboard](https://help.sap.com/viewer/3b2854f7840e420ab5a121e2a4d420c3/BLOCKCHAIN/en-US/635384f96cc04f1a9ee8e0dcf04d586c.html)

## Sample configuration of **Quorum on SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **quorum** by configuring your `usecase.json` file.

### Using the service plan **cyon**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "quorum",
      "plan": "cyon",
      "parameters" : {
        "dashboard": "",
        "enode": "",
        "rpc": "\u003c RPC URL (required, https only)\u003e"
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
      "name": "quorum",
      "plan": "dev"
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
      "name": "quorum",
      "plan": "testnet",
      "parameters" : {
        "nodeSecret": ""
      }
    }
  ]
}
```
