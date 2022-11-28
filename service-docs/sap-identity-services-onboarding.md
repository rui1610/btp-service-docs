# sap-identity-services-onboarding (Cloud Identity Services)

Cloud Identity Services provide basic capabilities for user authentication.

## Service plan availability in regions

| Region | additional-tenant | connectivity | default |
|--------|-------------------|--------------|---------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | | ✅ |
|  **ap21** | ✅ | | ✅ |
|  **br10** | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | | ✅ |
|  **eu20** | ✅ | | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ |
|  **us21** | ✅ | | ✅ |
|  **us30** | ✅ | | ✅ |

## Additional details

### Support components

- BC-IAM-IDS

### Discovery Center

- [SAP Discovery Center - Identity Provisioning](https://discovery-center.cloud.sap/serviceCatalog/identity-provisioning)

### Documentation

- [API Documentation](https://api.sap.com/api/IPS_Proxy/resource)
- [Feature Scope Description](https://help.sap.com/http.svc/rc/a64e4891b68a40db95ef9785446e174a/Cloud/en-US/FSD_for_IPS.pdf)
- [Onboarding](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/431ba4e8b9704848aec3aea97fcbfd8b.html)
- [Transformations](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/81f5204a5829429781d9ecc8b171f287.html)
- [What's New](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/b2cddb90224d4330a0fbf74573adc395.html)
- [Initial Setup](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/bd214dcbdd824834b34045c13f1508e2.html)
- [Systems](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/e59ae54bc2074f699be8768403eee46a.html)
- [Properties](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/e92c1aa0bb634ec1a35f353f0a4588ec.html)
- [What is Identity Provisioning](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/f2b2df8a273642a1bf801e99ecc4a043.html)
- [Documentation](https://help.sap.com/docs/IDENTITY_AUTHENTICATION)
- [Help Portal Product Page](https://help.sap.com/docs/IDENTITY_PROVISIONING)

### SAP Community

- [SAP Cloud Identity Services](https://community.sap.com/topics/cloud-identity-services)

### Support

- [Guided Answers](https://ga.support.sap.com/dtp/viewer/#/tree/2065/actions/26547:29111:29114:27412)
- [Get Support](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/50c693d6062843ef90c09e435eb424f2.html)
- [Troubleshooting](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/c6aa07e59c8343aab6ca995b551d114b.html)

### Tutorial

- [Hybrid Scenario: SAP IDM](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/6fa419a1901a464ea7dd214bcf476468.html)
- [Real-Time Provisioning: Identity Authentication](https://help.sap.com/docs/BTP/f48e822d6d484fa5ade7dda78b64d9f5/70afd909734842b08ff8f1be5b01bc2a.html)

## Sample configuration of **Cloud Identity Services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **sap-identity-services-onboarding** by configuring your `usecase.json` file.

### Using the service plan **additional-tenant**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sap-identity-services-onboarding",
      "plan": "additional-tenant"
    }
  ]
}
```

### Using the service plan **connectivity**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sap-identity-services-onboarding",
      "plan": "connectivity"
    }
  ]
}
```

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "sap-identity-services-onboarding",
      "plan": "default"
    }
  ]
}
```
