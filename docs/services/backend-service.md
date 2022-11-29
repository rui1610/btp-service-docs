# Backend-service (SAP Backend service)

With SAP Business Technology Platform Backed service you can build robust, scalable and enterprise-ready APIs/services to serve your applications and extensions in a serverless environment. It is a fully managed API service that helps you build, run, and manage APIs in a serverless environment [BETA]

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details
### Documentation

- [Documentation](https://help.sap.com/viewer/70dea311943a4ab99f903ccc584225f6/Cloud/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Backend%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Backend%20service)

## Sample configuration of **SAP Backend service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **Backend-service** by configuring your `usecase.json` file.

### Using the service plan **standard** (SAP Cloud Platform Backend service)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "Backend-service",
      "plan": "standard"
    }
  ]
}
```
