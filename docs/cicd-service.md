# cicd-service (SAP Continuous Integration and Delivery)

SAP Continuous Integration and Delivery lets you configure and run predefined continuous integration and delivery (CI/CD) pipelines that automatically test, build, and deploy your code changes to speed up your development and delivery cycles.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |

## Additional details

### Support components

- BC-CP-CF-CICD

### API Hub

- [Overview | SAP Continuous Integration and Delivery | SAP API Business Hub](https://api.sap.com/package/SAPContinuousIntegrationandDelivery/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/continuous-integration--delivery?region=all)
- [SAP Discovery Center - Continuous Integration & Delivery](https://discovery-center.cloud.sap/serviceCatalog/continuous-integration-delivery)

### Documentation

- [Documentation](https://help.sap.com/docs/CONTINUOUS_DELIVERY)
- [Documentation](https://help.sap.com/docs/CONTINUOUS_DELIVERY/99c72101f7ee40d0b2deb4df72ba1ad3/618ca03fdca24e56924cc87cfbb7673a.html)
- [What Is SAP Continuous Integration and Delivery](https://help.sap.com/docs/BTP/99c72101f7ee40d0b2deb4df72ba1ad3/618ca03fdca24e56924cc87cfbb7673a.html)
- [Initial Setup](https://help.sap.com/docs/BTP/99c72101f7ee40d0b2deb4df72ba1ad3/719acaf61e4b4bf0a496483155c52570.html)
- [Continuous Integration and Delivery by SAP](https://help.sap.com/docs/CICD_OVERVIEW)

### Learning

- [Learning Journey: Continuous Integration and Delivery by SAP](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/b76f0b2e5d534c449c1f3b0fa84ab697.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Continuous%20Integration%20and%20Delivery)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Continuous%20Integration%20and%20Delivery)

### Support

- [Support](https://help.sap.com/docs/CONTINUOUS_DELIVERY/99c72101f7ee40d0b2deb4df72ba1ad3/6e10ad426e434180a0c62d4e7b6115bc.html)

## Sample configuration of **SAP Continuous Integration and Delivery** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **cicd-service** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "cicd-service",
      "plan": "default"
    }
  ]
}
```
