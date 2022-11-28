# identity (SAP Cloud Identity Services)

Cloud Identity Services provide basic capabilities for user authentication.

## Service plan availability in regions

| Region | application |
|--------|-------------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **ch20** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-IAM-IDS

### API Hub

- [Overview | SAP Cloud Identity Services | SAP API Business Hub](https://api.sap.com/package/SCPIdentityServices/overview)

### Blog

- [How-To Guide: SAP Business Technology Platform Identity Authentication](https://blogs.sap.com/2015/08/12/sap-cloud-identity-how-to-guides/)

### Discovery Center

- [SAP Discovery Center - Identity Authentication](https://discovery-center.cloud.sap/serviceCatalog/identity-authentication)

### Documentation

- [Documentation](https://help.sap.com/IAS)
- [Feature Scope Description](https://help.sap.com/http.svc/rc/9eeb59b4bab04a289778bc1463fa181b/Cloud/en-US/FSD_for_IAS.pdf)
- [Documentation: Identity and Access Management](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e6b196abbb5710148c8ec6a698441b1e.html)
- [What is Identity Authentication](https://help.sap.com/docs/BTP/6d6d63354d1242d185ab4830fc04feb1/27882717f44b445fa287936c6f43dc1f.html)
- [Initial Setup](https://help.sap.com/docs/BTP/6d6d63354d1242d185ab4830fc04feb1/31af7da133874e199a7df1d42905241b.html)
- [Regional Availability](https://help.sap.com/docs/BTP/6d6d63354d1242d185ab4830fc04feb1/be600ca4258241789a3ab4adc05e4849.html)
- [API Documentation](https://help.sap.com/docs/BTP/6d6d63354d1242d185ab4830fc04feb1/cce8d64eed1c4d8d8311147336ffe2eb.html)
- [What's New](https://help.sap.com/docs/BTP/6d6d63354d1242d185ab4830fc04feb1/de21efe39e1442618388784891497067.html)
- [Help Portal Product Page](https://help.sap.com/docs/IDENTITY_AUTHENTICATION)
- [Documentation](https://help.sap.com/docs/IDENTITY_PROVISIONING)
- [SAP Community Wiki: SAP Business Technology Platform Identity Authentication](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=448474827)
- [SAP Community: Security](https://www.sap.com/community/topic/security.html)
- [Overview: SAP Business Technology Platform Identity Authentication](https://www.sap.com/documents/2015/07/e4803e8e-5b7c-0010-82c7-eda71af511fa.html)

### Learning

- [Learning Journey: SAP BTP Security](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/69aca66b45a74a73b4cc0efddd6ae63f.html)

### SAP Community

- [SAP Cloud Identity Services](https://community.sap.com/topics/cloud-identity-services)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Cloud%20Identity%20Services)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Cloud%20Identity%20Services)

### Support

- [Guided Answers](https://ga.support.sap.com/dtp/viewer/#/tree/2065/actions/26547:29111)
- [Get Support](https://help.sap.com/docs/BTP/6d6d63354d1242d185ab4830fc04feb1/06818b2e1d334950ad984ea997341d9c.html)

## Sample configuration of **SAP Cloud Identity Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **identity** by configuring your `usecase.json` file.

### Using the service plan **application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "identity",
      "plan": "application"
    }
  ]
}
```
