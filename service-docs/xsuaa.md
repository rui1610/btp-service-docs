# xsuaa (SAP Authorization and Trust Management service)

The Authorization and Trust Management service lets you manage user authorizations and trust to identity providers. Identity providers are the user base for applications. You can use an identity authentication tenant, an SAP on-premise system, or a custom corporate identity provider. User authorizations are managed using technical roles at the application level, which can be aggregated into business-level groups and role collections for large-scale cloud scenarios.

## Service plan availability in regions

| Region | apiaccess | application | broker | space |
|--------|-----------|-------------|--------|-------|
|  **ap10** | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ | ✅ |
|  **in30** | ✅ | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ | ✅ |

## Additional details

### Support components

- BC-XS-SEC

### API Hub

- [Overview | SAP Authorization and Trust Management Service | SAP API Business Hub](https://api.sap.com/package/authtrustmgmnt/overview)

### Discovery Center

- [SAP Discovery Center - Authorization and Trust Management Service](https://discovery-center.cloud.sap/serviceCatalog/authorization-and-trust-management-service)

### Documentation

- [API Documentation](https://api.sap.com/package/authtrustmgmnt/rest)
- [Feature Scope Description](https://help.sap.com/doc/9ee30e4e471041ec9437c5a6866554ce/)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/6d3ef5260f4a4232ad43542ab1441694.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/d203e2d41df1455d8fdc2334844a60d4.html)
- [Documentation](https://help.sap.com/docs/CP_AUTHORIZ_TRUST_MNG)
- [What is the SAP Authorization and Trust Managment Service in the Cloud Foundry Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/6373bb7a96114d619bfdfdc6f505d1b9.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/dbea343ebe184c26b6067daaabaa9ac6.html)
- [What's New](https://help.sap.com/whats-new/cf0cb2cb149647329b5d02aa96303f56?Component=Authorization%20and%20Trust%20Management%20Service)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Authorization%20and%20Trust%20Management%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Authorization%20and%20Trust%20Management%20service)

### Support

- [Troubleshooting for the SAP Authorization and Trust Management Service](https://ga.support.sap.com/dtp/viewer/index.html#/tree/2212/actions/28290)

### Tutorial

- [Tutorials (Cloud Foundry Environment)](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/902ae800c1d04c7388e407b7815e5cc8.html)

## Sample configuration of **SAP Authorization and Trust Management service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **xsuaa** by configuring your `usecase.json` file.

### Using the service plan **apiaccess**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "xsuaa",
      "plan": "apiaccess"
    }
  ]
}
```

### Using the service plan **application**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "xsuaa",
      "plan": "application"
    }
  ]
}
```

### Using the service plan **broker**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "xsuaa",
      "plan": "broker"
    }
  ]
}
```

### Using the service plan **space**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "xsuaa",
      "plan": "space"
    }
  ]
}
```
