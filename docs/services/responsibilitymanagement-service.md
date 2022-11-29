# responsibilitymanagement-service (SAP Responsibility Management service)

As we move toward an intelligent enterprise, intelligent systems need to determine agents who are responsible for business processes and objects, and automatically notify them. It is essential to define and manage these responsibilities for various contexts and retrieve responsible agents who can respond to tasks and activities.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **eu11** | ✅ |

## Additional details

### Support components

- CA-GTF-RM-SCP

### API Hub

- [Overview | SAP Responsibility Management Service on SAP Business Technology Platform | SAP API Business Hub](https://api.sap.com/package/ResponsibilityManagementOnSAPBTP/overview)

### Discovery Center

- [SAP Discovery Center - Responsibility Management Service](https://discovery-center.cloud.sap/serviceCatalog/responsibility-management-service)

### Documentation

- [API Documentation](https://api.sap.com/package/ResponsibilityManagementOnSAPBTP/rest)
- [Documentation](https://help.sap.com/viewer/8308e6d301d54584a33cd04a9861bc52/1809.000/en-US/a4a31dc3e2824cb1afc7be8eafc07f5c.html?q=Responsibility%20Management)
- [User Guide](https://help.sap.com/viewer/a8ad1b81adf945e1a5412b77e529548c/SHIP/en-US)
- [Administration Guide](https://help.sap.com/viewer/b0ae433f989940e1abdbaf45ec7f299b/SHIP/en-US)
- [Initial Setup](https://help.sap.com/viewer/b0ae433f989940e1abdbaf45ec7f299b/SHIP/en-US/dc11a8a73b1c43fe921135020234c662.html)
- [What is SAP Responsibility Management service](https://help.sap.com/viewer/e8006c3a6395426291c07b3e6f7ce78b/SHIP/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/RESPONSIBILITY_MANAGEMENT_SCP/SHIP/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Responsibility%20Management%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Responsibility%20Management%20service)

## Sample configuration of **SAP Responsibility Management service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **responsibilitymanagement-service** by configuring your `usecase.json` file.

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "responsibilitymanagement-service",
      "plan": "standard"
    }
  ]
}
```
