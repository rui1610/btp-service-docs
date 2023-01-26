# eadesigner (SAP Enterprise Architecture Designer, cloud edition)

SAP Enterprise Architecture Designer, Cloud Edition (SAP EA Designer) lets you capture, analyze, and present your organization's landscapes, strategies, requirements, processes, data, and other artifacts in a shared environment. Using industry-standard notations and techniques, organizations can leverage rich metadata and use models and diagrams to drive understanding and promote shared outcomes in creating innovative systems, information sets, and processes to support goals and capabilities.

## Service plan availability in regions

| Region | eadesigner |
|--------|------------|
|  **eu10** | ✅ |

## Additional details

### Support components

- BC-EAD

### Documentation

- [Feature Scope Description](https://help.sap.com/http.svc/rc/cb79879167bd42008e388e8c56155ea9/Cloud/en-US/fsd_ead_ce_en.pdf)
- [Onboarding](https://help.sap.com/docs/BTP/6e09b4f06bc94553995ecdcc84f245ef/b4f2236afd49409fa0d24c95fa2a974d.html)
- [Initial Setup](https://help.sap.com/docs/BTP/6e09b4f06bc94553995ecdcc84f245ef/e00e548b8f4347f6bb70651710b27717.html)
- [What is SAP Enterprise Architecture Designer, cloud edition](https://help.sap.com/viewer/c50a2057f35a4731838910588f247f4a/Internal/en-US)
- [What's New](https://help.sap.com/viewer/f34e7843098846e0b912841a378b426e/Cloud/en-US)
- [Help Portal Product Page](https://help.sap.com/docs/EAD_CLOUD)

### External

- [SAP Enterprise Architecture Designer](https://www.youtube.com/embed/Y9Z-BuDc5Fo)

### Learning

- [openSAP Introduction to SAP Enterprise Architecture Designer](https://open.sap.com/courses/hsead1)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Enterprise%20Architecture%20Designer%2C%20cloud%20edition)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Enterprise%20Architecture%20Designer%2C%20cloud%20edition)

## Sample configuration of **SAP Enterprise Architecture Designer, cloud edition** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **eadesigner** by configuring your `usecase.json` file.

### Using the service plan **eadesigner** (SAP Enterprise Architecture Designer, cloud edition)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "eadesigner",
      "plan": "eadesigner"
    }
  ]
}
```
