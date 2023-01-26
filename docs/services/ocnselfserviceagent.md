# ocnselfserviceagent (Open Connectors)

Open Connectors provides pre-built and feature-rich connectors to simplify the connectivity and seamless integration with over 150 non-SAP cloud applications. Customers benefit from connectivity to third-party APIs via harmonized RESTful APIs and can develop and map canonical data models to extend pre-built connectors. Furthermore customers can easily build API compositions across the different connectors.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **eu10** | ✅ |
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

- LOD-OCN-SRV

### API Hub

- [Overview | Platform - Open Connectors | SAP API Business Hub](https://api.sap.com/package/PlatformAPI/overview)
- [Overview | Analytics - Open Connectors | SAP API Business Hub](https://api.sap.com/package/analytics/overview)
- [Overview | Billing - Open Connectors | SAP API Business Hub](https://api.sap.com/package/billing/overview)
- [Overview | Collaboration - Open Connectors | SAP API Business Hub](https://api.sap.com/package/collaboration/overview)
- [Overview | Conferencing - Open Connectors | SAP API Business Hub](https://api.sap.com/package/conferencing/overview)
- [Overview | Customer Relationship Management - Open Connectors | SAP API Business Hub](https://api.sap.com/package/crm/overview)
- [Overview | Datawarehouse - Open Connectors | SAP API Business Hub](https://api.sap.com/package/datawarehouse/overview)
- [Overview | Database - Open Connectors | SAP API Business Hub](https://api.sap.com/package/db/overview)
- [Overview | Cloud Storage & Documents - Open Connectors | SAP API Business Hub](https://api.sap.com/package/documents/overview)
- [Overview | eCommerce - Open Connectors | SAP API Business Hub](https://api.sap.com/package/ecommerce/overview)
- [Overview | EDI - Open Connectors | SAP API Business Hub](https://api.sap.com/package/edi/overview)
- [Overview | Employee - Open Connectors | SAP API Business Hub](https://api.sap.com/package/employee/overview)
- [Overview | ERP - Open Connectors | SAP API Business Hub](https://api.sap.com/package/erp/overview)
- [Overview | eSignature - Open Connectors | SAP API Business Hub](https://api.sap.com/package/esignature/overview)
- [Overview | Finance - Open Connectors | SAP API Business Hub](https://api.sap.com/package/finance/overview)
- [Overview | Field Service - Open Connectors | SAP API Business Hub](https://api.sap.com/package/fsa/overview)
- [Overview | Help Desk - Open Connectors | SAP API Business Hub](https://api.sap.com/package/helpdesk/overview)
- [Overview | Human Capital - Open Connectors | SAP API Business Hub](https://api.sap.com/package/humancapital/overview)
- [Overview | Marketing - Open Connectors | SAP API Business Hub](https://api.sap.com/package/marketing/overview)
- [Overview | Messaging - Open Connectors | SAP API Business Hub](https://api.sap.com/package/messaging/overview)
- [Overview | Payments and Billing - Open Connectors | SAP API Business Hub](https://api.sap.com/package/payment/overview)
- [Overview | Productivity - Open Connectors | SAP API Business Hub](https://api.sap.com/package/productivity/overview)
- [Overview | Rewards - Open Connectors | SAP API Business Hub](https://api.sap.com/package/rewards/overview)
- [Overview | Scheduling - Open Connectors | SAP API Business Hub](https://api.sap.com/package/scheduling/overview)
- [Overview | Screening - Open Connectors | SAP API Business Hub](https://api.sap.com/package/screening/overview)
- [Overview | Social - Open Connectors | SAP API Business Hub](https://api.sap.com/package/social/overview)

### Documentation

- [Documentation](https://help.openconnectors.ext.hana.ondemand.com/home/catalog)
- [What's New](https://help.openconnectors.ext.hana.ondemand.com/home/whats-new)
- [Help Portal Product Page](https://help.sap.com/docs/OPEN_CONNECTORS)

### Onboarding

- [Tutorial: Onboarding](https://developers.sap.com/tutorials/cp-apim-openconnectors-enable.html)

### Tool

- [Open Connectors - Take a Tour](https://help.openconnectors.ext.hana.ondemand.com/home/take-a-tour)

## Sample configuration of **Open Connectors** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ocnselfserviceagent** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "ocnselfserviceagent",
      "plan": "standard"
    }
  ]
}
```
