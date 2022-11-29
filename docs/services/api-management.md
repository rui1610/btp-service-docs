# api-management (SAP API Management)

API Management

## Service plan availability in regions

| Region | preview |
|--------|---------|
|  **eu10** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |

## Additional details

### Support components

- OPU-API-OD-DT

### API Hub

- [Overview | API Content - Recipes | SAP API Business Hub](https://api.sap.com/package/APIContentRecipes/overview)
- [Overview | SAP API Management | SAP API Business Hub](https://api.sap.com/package/APIMgmt/overview)
- [Overview | SAP API Management Debugging and Traceability | SAP API Business Hub](https://api.sap.com/package/DebuggingandTraceability/overview)

### Blog

- [Blogs](https://blogs.sap.com/tags/73554900100700000774/)
- [SAP API Management FAQ](https://blogs.sap.com/2017/08/18/sap-api-management-faq/)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/55b4cf1c4ea04d4bbd6178c3d0ea75de/)
- [What's New](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/0734f8fa6b3a477181b54a8d319accdf.html)
- [Documentation](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/2ceab71343704de0bfce2145f97c85b1.html)
- [Onboarding](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/5a4b9fd9c26c49109a70cb9a221c7149.html)
- [Build APIs](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/74c042b9710e4970ae51ec58b749fb4f.html)
- [Publish APIs](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/75a4a11ed5294ec89b69fb40dba36308.html)
- [Analyze APIs](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/7712c611015045afb47d7c244fffee63.html)
- [API Management as a Service on SAP Cloud Foundry](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/7d8514b4ab46455e8416723003b414d7.html)
- [What is SAP API Management](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/adcbc07b031b4ac285b22867a1216306.html)
- [Consume APIs](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/dd6d58c1586a4a0a8ffca46a1a019d38.html)
- [Initial Setup](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/f9ebf02b2ca5456db8ce6ea2556afb88.html)
- [Monetize APIs](https://help.sap.com/docs/BTP/66d066d903c2473f81ec33acfe2ccdb4/fcdc89b5c4884d5e8cfb32c5914943ab.html)
- [Documentation](https://help.sap.com/viewer/66d066d903c2473f81ec33acfe2ccdb4/Cloud/en-US?)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_CLOUD_PLATFORM_API_MANAGEMENT)
- [Enable the SAP Business Technology Platform, API Management Service](https://www.sap.com/developer/tutorials/hcp-apim-enable-service.html)
- [Explore SAP APIs Infographic ](https://www.sap.com/documents/2017/11/962aa5f1-df7c-0010-82c7-eda71af511fa.html)
- [Documentation](https://www.sap.com/india/products/api-management.html#support)

### Learning

- [Learning Journey](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/70d719fe34e74dd68afd01a4274341ea.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20API%20Management)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20API%20Management)
- [SAP Community](https://help.hana.ondemand.com/apim_od/frameset.htm)

### Tutorial

- [Get Started with API Management](https://developers.sap.com/group.cp-apim-code-1.html)

## Sample configuration of **SAP API Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **api-management** by configuring your `usecase.json` file.

### Using the service plan **preview** (Expose your data and processes as APIs for omni-channel consumption and manage the lifecycle of those APIs)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "api-management",
      "plan": "preview"
    }
  ]
}
```
