# c4-distributed-order-management-app (SAP Order Management Foundation)

The SAP Order Management foundation solution, including the application and service, provides order management functionality along with business configuration settings that allow you to create a customized solution. You can also integrate various systems and solutions to support your order management processes. This allows you to leverage, for example, your existing master data, order capture, and fulfillment systems while consolidating all of your orders and order-related data in a convenient cloud-based solution.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **eu20** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Order Management Foundation | SAP API Business Hub](https://api.sap.com/package/SAPOrderManagementFoundation/overview)

### Documentation

- [Documentation](https://help.sap.com/docs/SAP_Order_Management_Foundation)

### Support

- [Support](https://help.sap.com/docs/SAP_Order_Management_Foundation/d91676a7fa624c31b7b1c526d7787e2f/ca6630612cf741ed8927d60fabe13929.html)

## Sample configuration of **SAP Order Management Foundation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **c4-distributed-order-management-app** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "c4-distributed-order-management-app",
      "plan": "default"
    }
  ]
}
```
