# service-ticket-intelligence (Service Ticket Intelligence)

With Service Ticket Intelligence, incoming customers service tickets are automatically classified into their categories, and routed to the right agent. The agent is then provided with recommended solutions to improve operational efficiency. Service Ticket Intelligence leverages deep learning neural networks trained on large amounts of historical data. The model understands the semantics of unstructured ticket messages, classifies the ticket into their most likely categories and recommends solutions or knowledge base articles from similar previously answered tickets for the agent. With more processed service tickets and users feedback, the model improves over time.

## Service plan availability in regions

| Region | blocks_of_100 | free | standard |
|--------|---------------|------|----------|
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-STI

### Discovery Center

- [SAP Discovery Center - Service Ticket Intelligence](https://discovery-center.cloud.sap/serviceCatalog/service-ticket-intelligence)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/9339d4045988460d955b1a09f22d3c09/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [Help Portal Product Page](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE)
- [What Is Service Ticket Intelligence?](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/2f0e49ac91c24d54acb694d967e0cfc0.html)
- [What's New](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/4fbe20662df24b66b798deb7e81781b5.html)
- [Integrating with SAP CRM On-Premise](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/84cd88025efd4812ad7454a9e1a799e0.html)
- [Initial Setup](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/a029ae39ae0c455b8f30d603253eb095.html)
- [API Documentation](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/cb422d6436504ad2b6efabd0945f6654.html)
- [Security](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/fc597030d6cc4fde98197189f7676046.html)
- [Documentation](https://help.sap.com/stint)
- [Documentation](https://help.sap.com/viewer/product/SERVICE_TICKET_INTELLIGENCE)

### External

- [SAP AI Business Services - Service Ticket Intelligence Categories and Similar Tickets](https://www.youtube.com/embed/Tx7jBawli64)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Service%20Ticket%20Intelligence)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Service%20Ticket%20Intelligence)
- [SAP Community Topic Page](https://community.sap.com/topics/service-ticket-intelligence)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/SERVICE_TICKET_INTELLIGENCE/934ccff77ddb4fa2bf268a0085984db0/82e2f597a179421296edcf46931131b6.html)
- [Support](https://help.sap.com/viewer/934ccff77ddb4fa2bf268a0085984db0/LATEST/en-US/76a77fbf8d3645978d98711450f0b8bc.html)

### Tutorial

- [Use Machine Learning to Process Service Requests](https://developers.sap.com/mission.cp-aibus-sti-service-requests.html)

## Sample configuration of **Service Ticket Intelligence** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **service-ticket-intelligence** by configuring your `usecase.json` file.

### Using the service plan **blocks_of_100**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
      "plan": "blocks_of_100"
    }
  ]
}
```

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "service-ticket-intelligence",
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
      "name": "service-ticket-intelligence",
      "plan": "standard"
    }
  ]
}
```
