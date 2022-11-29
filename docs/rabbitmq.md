# rabbitmq (RabbitMQ)

RabbitMQ on SAP BTP includes a message broker that implements message queues for application-to-application messaging. Supports Advanced Message Queuing Protocol (AMQP).

## Service plan availability in regions

| Region | large | medium | small | virtualhost | xsmall |
|--------|-------|--------|-------|-------------|--------|
|  **ap10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ | | ✅ |
|  **ap20** | ✅ | ✅ | ✅ | | ✅ |
|  **ap21** | ✅ | ✅ | ✅ | | ✅ |
|  **br10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ | | ✅ |
|  **eu10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ | | ✅ |
|  **eu20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ | | ✅ |
|  **in30** | ✅ | ✅ | ✅ | | ✅ |
|  **jp10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ | | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ | | ✅ |
|  **us30** | ✅ | ✅ | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [Feature Scope Description](https://help.sap.com/doc/7b0fc537dd794cc3abf113ee99936799/)
- [The RabbitMQ Cluster](https://help.sap.com/docs/BTP/15a22358e1984002b6b8ecd55960f49f/47ad9ecf5b734622b0af7bf6cbf04a31.html)
- [What is RabbitMQ Service](https://help.sap.com/docs/BTP/15a22358e1984002b6b8ecd55960f49f/9b68fdd62c064fe99d7bcce7f5f77a8c.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/bf757994794445ed904b97bf1907812a.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/RabbitMQ/Cloud/en-US)

### External

- [RabbitMQ Official Website](https://www.rabbitmq.com/)
- [External](https://www.rabbitmq.com/community.html)

### Marketing

- [Learn more about this service and how to purchase it. RabbitMQ 3.6 plans are reaching end of life soon. Support to upgrade the existing RabbitMQ 3.6 instances to the new 3.7 plans would be provided soon.](https://cloudplatform.sap.com/capabilities/integration/rabbitmq.html)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

### Tutorial

- [Tutorial: RabbitMQ](https://help.sap.com/docs/BTP/15a22358e1984002b6b8ecd55960f49f/bf757994794445ed904b97bf1907812a.html)

## Sample configuration of **RabbitMQ** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **rabbitmq** by configuring your `usecase.json` file.

### Using the service plan **large**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan": "large"
    }
  ]
}
```

### Using the service plan **medium**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan": "medium"
    }
  ]
}
```

### Using the service plan **small**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan": "small"
    }
  ]
}
```

### Using the service plan **virtualhost**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan": "virtualhost"
    }
  ]
}
```

### Using the service plan **xsmall**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "rabbitmq",
      "plan": "xsmall"
    }
  ]
}
```
