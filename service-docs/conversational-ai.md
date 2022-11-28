# conversational-ai (SAP Conversational AI)

SAP Conversational AI is a collaborative end-to-end platform for creating chatbots. Along with conversational natural language processing (NLP) and dialog management features supported with detailed API documentation, SAP Conversational AI makes it easy to connect your bots to different messaging channels.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details

### Support components

- CA-ML-CAI

### API Hub

- [Overview | SAP Conversational AI | SAP API Business Hub](https://api.sap.com/package/SAPConversationalAI/overview)
- [API Hub](https://api.sap.com/package/SAPConversationalAI?section=Artifacts)

### Discovery Center

- [SAP Discovery Center - Conversational AI](https://discovery-center.cloud.sap/serviceCatalog/conversational-ai)

### Documentation

- [API Documentation](https://cai.tools.sap/docs/api-reference/)
- [Help Portal Product Page](https://help.sap.com/cai)
- [Feature Scope Description](https://help.sap.com/doc/5befc39ddee84fe681d565cadd98ce05/latest/en-US/KeyFeaturesOfSAPConversationalAI.pdf)
- [What is SAP Conversational AI](https://help.sap.com/viewer/3aab817a03be4432abbfd00c42b23cb8/latest/en-US)
- [Initial Setup](https://help.sap.com/viewer/3aab817a03be4432abbfd00c42b23cb8/latest/en-US/e676f11574434ad984a335ad1f4b0bf5.html)
- [Documentation](https://help.sap.com/viewer/7a8f56b0db554075a940d4b12019eb6f/latest/en-US/475bfc62d8e34d84b2983b376fcca6ea.html)
- [Documentation](https://help.sap.com/viewer/7a8f56b0db554075a940d4b12019eb6f/latest/en-US/a517600a3c3f472396ba4cb7ad91f8bf.html)
- [Onboarding](https://help.sap.com/viewer/b2541bd8032b403c9c083ca20682dd3b/latest/en-US/f3b39a2e106a495d8324d98cb38a3e1a.html)
- [Documentation](https://help.sap.com/docs/SAP_CONVERSATIONAL_AI)

### Learning

- [Learning Journey](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/72ff4b1e30414104ac9c315da1ecc6b5.html?collapse=)

### SAP Community

- [SAP Community](https://community.sap.com/topics/conversational-ai)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Conversational%20AI)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Conversational%20AI)

### Support

- [SAP Answers](https://answers.sap.com/tags/73555000100800001301)
- [Support](https://launchpad.support.sap.com)

### Tutorial

- [Blogs from SAP Community](https://blogs.sap.com/tags/73555000100800001301/)

## Sample configuration of **SAP Conversational AI** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **conversational-ai** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "conversational-ai",
      "plan": "standard"
    }
  ]
}
```
