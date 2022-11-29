# feature-flags (SAP Feature Flags service)

The Feature Flags service allows you to enable or disable new features at runtime without redeploying or restarting the application. You can use feature flags to control code delivery, synchronized rollout, direct shipment, and fast rollback of features.

## Service plan availability in regions

| Region | lite | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **ch20** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CF-FEATUREFLG

### API Hub

- [Overview | SAP Feature Flags Service | SAP API Business Hub](https://api.sap.com/package/SAPFeatureFlagsService/overview)

### Discovery Center

- [SAP Discovery Center - Feature Flags Service](https://discovery-center.cloud.sap/serviceCatalog/feature-flags-service)

### Documentation

- [Feature Flags Service Demo Application](https://github.com/SAP/cloud-cf-feature-flags-sample)
- [Feature Scope Description](https://help.sap.com/doc/c318354b6484417c922a9451b2ab6c88/)
- [Documentation](https://help.sap.com/viewer/2250efa12769480299a1acd282b615cf/Cloud/en-US/)
- [API Documentation](https://help.sap.com/docs/BTP/2250efa12769480299a1acd282b615cf/57bd5a2dfe4e4b2e93ff87e06ded2d3c.html)
- [What's New](https://help.sap.com/docs/BTP/2250efa12769480299a1acd282b615cf/5869d68f44fb48e68614287858b511f3.html)
- [What is SAP Feature Flags service?](https://help.sap.com/docs/BTP/2250efa12769480299a1acd282b615cf/d485374a71a149a7ba96b7403985a1a6.html)
- [Documentation](https://help.sap.com/docs/BTP/2250efa12769480299a1acd282b615cf/e432bfb1493c4da286e5981aee540688.html)
- [Help Portal Product Page](https://help.sap.com/docs/FEATURE_FLAGS)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Feature%20Flags%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Feature%20Flags%20service)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **SAP Feature Flags service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **feature-flags** by configuring your `usecase.json` file.

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "feature-flags",
      "plan": "lite"
    }
  ]
}
```

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "feature-flags",
      "plan": "standard"
    }
  ]
}
```
