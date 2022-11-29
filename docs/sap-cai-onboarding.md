# sap-cai-onboarding (SAP Conversational AI)

SAP Conversational AI is a collaborative end-to-end platform for creating chatbots. Along with conversational natural language processing (NLP) and dialog management features supported with detailed API documentation, SAP Conversational AI makes it easy to connect your bots to different messaging channels.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **us10** | ✅ |

## Additional details
### API Hub

- [API Hub](https://api.sap.com/package/SAPConversationalAI?section=Artifacts)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/conversational-ai)

### Documentation

- [Documentation](https://help.sap.com/docs/SAP_CONVERSATIONAL_AI)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Conversational%20AI)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Conversational%20AI)
- [SAP Community](https://community.sap.com/topics/conversational-ai)

### Support

- [Support](https://launchpad.support.sap.com)

## Sample configuration of **SAP Conversational AI** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-cai-onboarding** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sap-cai-onboarding",
      "plan": "standard"
    }
  ]
}
```
