# INFRA (SAP Custom Domain service)

The SAP Business Technology Platform Custom Domain service lets you configure your own custom domain to expose publicly your SAP Business Technology Platform application instead of using the default subdomain.

## Service plan availability in regions

| Region | custom_domains |
|--------|----------------|
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
|  **eu30** | ✅ |
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-CP-CF-SEC-DOM

### Discovery Center

- [SAP Discovery Center - Custom Domain](https://discovery-center.cloud.sap/serviceCatalog/custom-domain)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/25be0de155024c609b4158de858cbf94/)
- [Help Portal Product Page](https://help.sap.com/docs/CUSTOM_DOMAINS)
- [Initial Setup](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/108177aea2a04d1b9006d96173bfa99a.html)
- [Custom Domain Plugin for the Cloud Foundry Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/1832fcd1eec9415694de50f620e5a522.html)
- [Using Custom Domains](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/2291aea5e22440f7a161bdeb9c16b664.html)
- [Prerequisites](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/48cdbe7a64f3475586dc2f4d11c5603c.html)
- [What's New](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/da61add5a0274134a0c7502da8cb57cf.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Custom%20Domain%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Custom%20Domain%20service)

### Support

- [Guided Answers](https://ga.support.sap.com/dtp/viewer/index.html#/tree/2437/actions/32393)
- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **SAP Custom Domain service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **INFRA** by configuring your `usecase.json` file.

### Using the service plan **custom_domains**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "INFRA",
      "plan": "custom_domains"
    }
  ]
}
```
