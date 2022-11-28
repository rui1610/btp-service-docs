# it-prod (Process Integration)

The SAP Cloud Integration connects cloud applications with other SAP and non-SAP cloud and on-premise apps.

## Service plan availability in regions

| Region | enterprise |
|--------|------------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Cloud Integration | SAP API Business Hub](https://api.sap.com/package/CloudIntegrationAPI/overview)
- [Prepackaged Integration Content](https://api.sap.com/shell/integration)

### Documentation

- [SAP Cloud Integration](https://www.sap.com/community/topics/cloud-integration.html)
- [Feature Scope Description](https://help.sap.com/doc/3da469f299514f25a00ade689a11ef2c/)
- [Initial Setup](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/0a556d5599ec4495ae1fb2ada6369744.html)
- [Security Guide](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/4b3bb3b1f4784cdbaf6ab103c18ea4a8.html)
- [API Documentation](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/72ef31d2739a4b079f0d297ffa684ec8.html)
- [SAP Business Technology Platform Integration - Adapter Development Kit](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/7392cc44de7c4450a65b8cd8f1042420.html)
- [Connecting a System to SAP Business Technology Platform Integration](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/7cfe913ba85d463a9c5fce101c3ae460.html)
- [What is SAP Cloud Integration](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/e12c09cc8e9b4574b092d8964b049ce6.html)
- [Accessing Cloud Platform Integration Web Application](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/e6b43b4c5a5042fda30a9dfdab97eff3.html)
- [SAP Business Technology Platform Integration for Data Services](https://help.sap.com/docs/SAP_CLOUD_PLATFORM_INTEGRATION_FOR_DATA_SERVICES)
- [Documentation](https://help.sap.com/viewer/product/CLOUD_INTEGRATION/Cloud)
- [Help Portal - SAP Cloud Integration Product Page](https://help.sap.com/docs/CLOUD_INTEGRATION)

### External

- [SAP Business Technology Platform Integration - SAP API Business Hub: Where to find what](https://www.youtube.com/embed/CqvppOT_Iro)
- [SAP Business Technology Platform Integration - Prepackaged Integration Content](https://www.youtube.com/embed/DwemZB0F7Zs)
- [SAP Business Technology Platform Integration - Overview](https://www.youtube.com/embed/Nl9LVn32pK8)
- [SAP Business Technology Platform Integration - Business-to-Business Integration](https://www.youtube.com/embed/cQZsq97SEmc)
- [SAP Business Technology Platform Integration - Service Level Agreements](https://www.youtube.com/embed/lZsqP9F7oac)
- [SAP Business Technology Platform Integration - Latest Integration Packages](https://www.youtube.com/embed/xnxekfCxhrw)

### Learning

- [Learning Journey: SAP Cloud Integration Basics](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/f4a390d6ee7147aa89ba587102702677.html)
- [Integration Flow Design Guidelines](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/6803389050a0487ca16d534583414d2b.html)

### Onboarding

- [Tutorial: Onboarding](https://developers.sap.com/mission.cp-starter-integration-cpi.html)

### Support

- [SAP Cloud Integration Troubleshooting Guide](https://ga.support.sap.com/dtp/viewer/#/tree/2065/actions/26547:26549:28901:28748)

### Tool

- [SAP Business Technology Platform Integration Web UI](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/9af2f05c7eb04457aee5906fd8553e00.html)

### Tutorial

- [Get Started with Integration Flow Development](https://help.sap.com/docs/BTP/368c481cd6954bdfa5d0435479fd4eaf/e5724cd84b854719973afe0356ea128b.html)

## Sample configuration of **Process Integration** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **it-prod** by configuring your `usecase.json` file.

### Using the service plan **enterprise** (Process Integration)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "it-prod",
      "plan": "enterprise"
    }
  ]
}
```
