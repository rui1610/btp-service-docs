# kymaruntime (SAP BTP, Kyma runtime)

SAP Business Technology Platform, Kyma runtime is a fully managed Kubernetes runtime based on the open-source project Kyma. This cloud-native solution allows the developers to extend SAP solutions with serverless Functions and combine them with containerized microservices. The offered functionality ensures smooth consumption of SAP and non-SAP applications, running workloads in a highly scalable environment, and building event- and API-based extensions.

## Service plan availability in regions

| Region | aws | azure | free | gcp |
|--------|-----|-------|------|-----|
|  **ap10** | ✅ | | ✅ | |
|  **ap11** | ✅ | | ✅ | |
|  **ap12** | ✅ | | ✅ | |
|  **ap21** | | ✅ | | |
|  **br10** | ✅ | | ✅ | |
|  **ca10** | ✅ | | ✅ | |
|  **eu10** | ✅ | | ✅ | |
|  **eu20** | | ✅ | | |
|  **eu30** | | | | ✅ |
|  **in30** | | | | ✅ |
|  **jp10** | ✅ | | ✅ | |
|  **jp20** | | ✅ | | |
|  **us10** | ✅ | | ✅ | |
|  **us20** | | ✅ | | |
|  **us21** | | ✅ | | |
|  **us30** | | | | ✅ |

## Additional details
### Discovery Center

- [SAP Discovery Center - Kyma Runtime](https://discovery-center.cloud.sap/serviceCatalog/kyma-runtime)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/5e8107bf49684962b897217040398007/)
- [What is Kyma Environment](https://help.sap.com/docs/BTP/3504ec5ef16548778610c7e89cc0eac3/468c2f3c3ca24c2c8497ef9f83154c44.html)
- [What is SAP BTP, Kyma runtime](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/468c2f3c3ca24c2c8497ef9f83154c44.html)
- [Administration and Operations in the Kyma Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/b8e16869e64a4abe93cc194aa6fdacf5.html)
- [Security in the Kyma Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/ee08fdfc9af8483b924e9ea9827f3ded.html)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20BTP%2C%20Kyma%20runtime)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20BTP%2C%20Kyma%20runtime)

### Tutorial

- [Tutorial: Enable Kyma Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/09dd313bf6644250a14f8f38c3d644c0.html)
- [Tutorial: Extending SAP S/4HANA Products in the Kyma Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/40b9e6c3cc43498b92472da13e88c7bf.html)

## Sample configuration of **SAP BTP, Kyma runtime** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **kymaruntime** by configuring your `usecase.json` file.

### Using the service plan **aws** (Kyma Runtime AWS)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan": "aws"
    }
  ]
}
```

### Using the service plan **azure** (Kyma Runtime Azure)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan": "azure"
    }
  ]
}
```

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **gcp** (Kyma Runtime GCP)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan": "gcp"
    }
  ]
}
```
