# alert-notification (SAP Alert Notification service for SAP BTP)

SAP Business Technology Platform Alert Notification offers a common API for providers to publish alerts and for consumers to subscribe to these alerts. It is designed to send automatically real-time notifications and alerts about SAP Cloud events that may be of interest to the business and operations.<br/><br/>SAP does not support EU Access for this service. By activating the service, you are accepting this limitation.

## Service plan availability in regions

| Region | free | standard |
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

- LOD-HCI-PI

### API Hub

- [Overview | SAP Alert Notification Service for SAP BTP | SAP API Business Hub](https://api.sap.com/package/AlertNotification/overview)
- [API Hub](https://api.sap.com/package/AlertNotification?section=Artifacts)

### Blog

- [Receive Notifications for Failed Integration Flows](https://blogs.sap.com/2019/10/14/receive-notifications-for-failed-sap-cloud-platform-integration-flows-via-any-channel-with-alert-notification/)
- [Alerts from your Solution on SAP BTP to SAP Solution Manager](https://blogs.sap.com/2019/11/04/alerts-from-your-sap-cloud-platform-solution-to-sap-solution-manager-via-sap-cloud-platform-alert-notification/)
- [https://blogs.sap.com/2020/04/02/automatic-alert-remediation-with-alert-notification-automation-pilot-and-servicenow/](https://blogs.sap.com/2020/04/02/automatic-alert-remediation-with-alert-notification-automation-pilot-and-servicenow/)
- [More…](https://blogs.sap.com/tag/sap-cloud-platform-alert-notification/)
- [Blog](https://blogs.sap.com/tags/73555000100800001401/)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/alert-notification)
- [SAP Discovery Center - Alert Notification](https://discovery-center.cloud.sap/serviceCatalog/alert-notification)

### Documentation

- [Documentation](https://help.sap.com/docs/ALERT_NOTIFICATION)

### External

- [https://www.youtube.com/embed/_DInhi4Skn4](https://www.youtube.com/embed/_DInhi4Skn4)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Alert%20Notification%20service%20for%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Alert%20Notification%20service%20for%20SAP%20BTP)

## Sample configuration of **SAP Alert Notification service for SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **alert-notification** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "alert-notification",
      "plan": "free"
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
      "name": "alert-notification",
      "plan": "standard"
    }
  ]
}
```
