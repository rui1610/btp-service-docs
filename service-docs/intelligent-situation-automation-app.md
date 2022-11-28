# intelligent-situation-automation-app (Intelligent Situation Automation)

Intelligent Situation Automation is an extension of Situation Handling. It processes situations raised and resolves them automatically using business rules, thus reducing the time users spend on routine manual and repetitive tasks.

## Service plan availability in regions

| Region | beta | free | standard |
|--------|------|------|----------|
|  **eu10** | ✅ | ✅ | ✅ |

## Additional details

### Support components

- CA-SIT-ATM

### Discovery Center

- [SAP Discovery Center - Intelligent Situation Automation](https://discovery-center.cloud.sap/serviceCatalog/intelligent-situation-automation)

### Documentation

- [What is Intelligent Situation Automation](https://help.sap.com/viewer/2dff17d3732c422b99c02bba7101dde7/1.0/en-US)
- [Initial Setup](https://help.sap.com/viewer/2dff17d3732c422b99c02bba7101dde7/1.0/en-US/82fa362287604ccfbd771da042d14bfe.html)
- [Administration Guide for Intelligent Situation Automation](https://help.sap.com/viewer/64b367baf8b346b09702672666b0c0ae/1.0/en-US)
- [User Guide for Intelligent Situation Automation](https://help.sap.com/viewer/dd7bde0fac4e421bb79830f81df88c86/1.0/en-US)
- [Help Portal Product Page](https://help.sap.com/viewer/product/INTELLIGENT_SITUATION_AUT/1.0/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Intelligent%20Situation%20Automation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Intelligent%20Situation%20Automation)

## Sample configuration of **Intelligent Situation Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **intelligent-situation-automation-app** by configuring your `usecase.json` file.

### Using the service plan **beta** (Beta)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "intelligent-situation-automation-app",
      "plan": "beta"
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
      "category": "APPLICATION",
      "name": "intelligent-situation-automation-app",
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
      "category": "APPLICATION",
      "name": "intelligent-situation-automation-app",
      "plan": "standard"
    }
  ]
}
```
