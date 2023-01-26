# ai-launchpad (SAP AI Launchpad)

SAP AI Launchpad is an application layer for AI Foundation. It is a one-stop-shop to access tooling around ML lifecycle management & Data Science activity. It is a container to access both SAP and open sourced integrated apps and tools. It is connected to a number of ML runtimes with an AI API. It allows users to get an overview over all ML Scenarios in all connected ML runtimes and manage the lifecycle of these.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-AILP

### Blog

- [SAP AI Launchpad Blogs](https://blogs.sap.com/tags/73555000100800003283/)

### Discovery Center

- [SAP Discovery Center - SAP AI Launchpad](https://discovery-center.cloud.sap/serviceCatalog/sap-ai-launchpad)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/91f0266b09a04484be6b68e9a7802b7e/CLOUD/en-US/7f4faf6764d249fc862714dac919532f.pdf)
- [What is SAP AI Launchpad?](https://help.sap.com/viewer/92d77f26188e4582897b9106b9cb72e0/CLOUD/en-US)
- [Initial Setup](https://help.sap.com/viewer/92d77f26188e4582897b9106b9cb72e0/CLOUD/en-US/5d8adb6f43ea4eeca97c9a2b2bb93c6b.html)
- [What's New](https://help.sap.com/viewer/92d77f26188e4582897b9106b9cb72e0/CLOUD/en-US/8910a9b993f840278c8afb0e4f39f4fc.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/AI_LAUNCHPAD/CLOUD/en-US)
- [Documentation](https://help.sap.com/viewer/product/AI_LAUNCHPAD/INTERNAL/en-US)

### Legal

- [Business Technology Platform Supplemental Terms and Conditions](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20AI%20Launchpad)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20AI%20Launchpad)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/viewer/92d77f26188e4582897b9106b9cb72e0/CLOUD/en-US/7a0e5a53d32c462bab4e56adc2397623.html)

### Tutorial

- [Get Started: Create Your First Machine Learning Project using SAP AI Core](https://developers.sap.com/group.ai-core-get-started-basics.html)

## Sample configuration of **SAP AI Launchpad** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ai-launchpad** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "ai-launchpad",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **standard** (Standard)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "ai-launchpad",
      "plan": "standard"
    }
  ]
}
```
