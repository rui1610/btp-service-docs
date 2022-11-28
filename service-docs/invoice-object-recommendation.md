# invoice-object-recommendation (Invoice Object Recommendation)

The Invoice Object Recommendation services provides the functionality to train a machine learning model with customer specific data that can give recommendations on G/L Accounts for incoming invoices without a purchase order reference attached. The service therefore provides a training call as described and an inference call that gives back recommendations based on a trained model to semi-automate the invoice processing in the area of accounts payable.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Feature Scope Description](https://help.sap.com/doc/511418153a1248b58eeab0e7e336b03b/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [Help Portal Product Page](https://help.sap.com/ior)
- [What Is Invoice Object Recommendation?](https://help.sap.com/viewer/15074a8e9a1a4abf923460c93e89b409/SHIP/en-US)
- [Initial Setup](https://help.sap.com/viewer/15074a8e9a1a4abf923460c93e89b409/SHIP/en-US/23ada8f84b93413fa7c24c99f794ca60.html)
- [API Documentation](https://help.sap.com/viewer/15074a8e9a1a4abf923460c93e89b409/SHIP/en-US/2d0329f8650046c0a84eaacb0abe8f58.html)
- [What's New](https://help.sap.com/viewer/15074a8e9a1a4abf923460c93e89b409/SHIP/en-US/90ed9b272fe64badb90db59cc80698ea.html)
- [Concepts](https://help.sap.com/viewer/15074a8e9a1a4abf923460c93e89b409/SHIP/en-US/a0d0687c35bb4a3d9851ff56765df316.html)
- [Security](https://help.sap.com/viewer/15074a8e9a1a4abf923460c93e89b409/SHIP/en-US/b0f46c4e4a904ff3b49b8e0791a0260c.html)
- [Documentation](https://help.sap.com/viewer/product/Invoice_Object_Recommendation)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Invoice%20Object%20Recommendation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Invoice%20Object%20Recommendation)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/Invoice_Object_Recommendation/15074a8e9a1a4abf923460c93e89b409/0e5c2fbc9dde497195dc8a4165778b5c.html)

## Sample configuration of **Invoice Object Recommendation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **invoice-object-recommendation** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "invoice-object-recommendation",
      "plan": "standard"
    }
  ]
}
```
