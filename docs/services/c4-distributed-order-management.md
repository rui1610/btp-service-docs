# c4-distributed-order-management (SAP Order Management foundation)

The SAP Order Management foundation solution, including the application and service, provides order management functionality along with business configuration settings that allow you to create a customized solution. You can also integrate various systems and solutions to support your order management processes. This allows you to leverage, for example, your existing master data, order capture, and fulfillment systems while consolidating all of your orders and order-related data in a convenient cloud-based solution.

## Service plan availability in regions

| Region | default |
|--------|---------|
|  **eu10** | ✅ |
|  **eu20** | ✅ |

## Additional details

### Support components

- CEC-BAF-DOM

### API Hub

- [Overview | SAP Order Management Foundation | SAP API Business Hub](https://api.sap.com/package/SAPOrderManagementFoundation/overview)
- [Overview | SAP Order Management Foundation Business Events | SAP API Business Hub](https://api.sap.com/package/SAPOrderManagementFoundationBusinessEvents/overview)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/65309ba6056d4d6c8dc40195ec4b3074/)
- [Documentation](https://help.sap.com/docs/SAP_EM)
- [Integration Guide](https://help.sap.com/docs/SAP_Order_Management_Foundation/95fb0d8e21b9460b8e4690ebbc667d92/0c2255104eb549069933a925dfe71503.html)
- [Initial Setup](https://help.sap.com/docs/SAP_Order_Management_Foundation/d91676a7fa624c31b7b1c526d7787e2f/227cf2f493d74fd6a996a88f29c82bee.html)
- [What is SAP Order Management Foundation?](https://help.sap.com/docs/SAP_Order_Management_Foundation/d91676a7fa624c31b7b1c526d7787e2f/4ad3e8588fb84c2db3bc0efa8bc88866.html)
- [Documentation](https://help.sap.com/docs/SAP_Order_Management_Foundation/d91676a7fa624c31b7b1c526d7787e2f/ca6630612cf741ed8927d60fabe13929.html)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_Order_Management_Foundation)
- [Documentation](https://help.sap.com/viewer/032cde7eac274695897645010260f636/latest/en-US/ca6630612cf741ed8927d60fabe13929.html)
- [Documentation](https://help.sap.com/viewer/product/C4_OrdMgmt/latest/en-US)
- [Documentation](https://help.sap.com/viewer/product/SAP_Order_Management_Foundation/)
- [What's New](https://help.sap.com/whats-new/255d859bc7ea47dfbdf4274b73cacc17)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Order%20Management%20foundation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Order%20Management%20foundation)

## Sample configuration of **SAP Order Management foundation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **c4-distributed-order-management** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "c4-distributed-order-management",
      "plan": "default"
    }
  ]
}
```
