# connectivity (SAP Connectivity service)

SAP BTP Connectivity service allows you to establish secure and reliable connectivity between your cloud applications and on-premise systems running in isolated networks.

## Service plan availability in regions

| Region | connectivity_proxy | lite |
|--------|--------------------|------|
|  **ap10** | ✅ | ✅ |
|  **ap11** | ✅ | ✅ |
|  **ap12** | ✅ | ✅ |
|  **ap20** | ✅ | ✅ |
|  **ap21** | ✅ | ✅ |
|  **br10** | ✅ | ✅ |
|  **ca10** | ✅ | ✅ |
|  **ch20** | ✅ | ✅ |
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **eu30** | ✅ | ✅ |
|  **in30** | ✅ | ✅ |
|  **jp10** | ✅ | ✅ |
|  **jp20** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | ✅ |
|  **us21** | ✅ | ✅ |
|  **us30** | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CON
- OPU-API-OD-DT

### API Hub

- [Overview | Connect to SAP Cloud Foundry Services | SAP API Business Hub](https://api.sap.com/package/SAPCloudFoundryConnectivity/overview)
- [Overview | Connect to SAP Business Technology Platform Services | SAP API Business Hub](https://api.sap.com/package/SAPCloudPlatformConnectivity/overview)
- [Overview | SAP Connectivity Service | SAP API Business Hub](https://api.sap.com/package/scpconnectivity/overview)

### Blog

- [Blog: How to use SAP Connectivity and Cloud Connector in the Cloud Foundry environment](https://blogs.sap.com/2017/07/09/how-to-use-the-sap-cloud-platform-connectivity-and-the-cloud-connector-in-the-cloud-foundry-environment-part-1/)
- [Blog: Using the Destination service in the Cloud Foundry Environment](https://blogs.sap.com/2018/10/08/using-the-destination-service-in-the-cloud-foundry-environment/)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/#/serviceCatalog/connectivity-service)
- [SAP Discovery Center - Connectivity Service](https://discovery-center.cloud.sap/serviceCatalog/connectivity-service)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/5e8107bf49684962b897217040398007/)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e54cc8fbbb571014beb5caaf6aa31280.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e6c7616abb5710148cfcf3e75d96d596.html)
- [Documentation](https://help.sap.com/viewer/66d066d903c2473f81ec33acfe2ccdb4/Cloud/en-US)
- [API Documentation](https://help.sap.com/docs/BTP/b865ed651e414196b39f8922db2122c7/e69bc863bb571014b358e2947e36d475.html)
- [Connectivity in the Cloud Foundry Environment](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/34010ace6ac84574a4ad02f5055d3597.html)
- [Initial Setup](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/78198e8b58f949af977e579b5de42299.html)
- [What's New](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/7882854691ec46f98fa012c46f3fc3a1.html)
- [Documentation](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/c731a6d16db644e393e6cbfd7367558e.html)
- [Cloud Connector: Security](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/cb50b6191615478aa11d2050dada467d.html)
- [What is SAP Connectivity Service](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/e54cc8fbbb571014beb5caaf6aa31280.html)
- [Cloud Connector](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/e6c7616abb5710148cfcf3e75d96d596.html)
- [Help Portal Product Page](https://help.sap.com/docs/CP_CONNECTIVITY)
- [Documentation](https://www.sap.com/products/business-technology-platform/use-cases.html)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/integration/cloud-connector.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Connectivity%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Connectivity%20service)

### Support

- [Connectivity: Guided Answers](https://ga.support.sap.com/dtp/viewer/#/tree/2065/actions/26547:26556)
- [Connectivity: Support](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/e5580c5dbb5710149e53c6013301a9f2.html)
- [Cloud Connector: FAQ](https://help.sap.com/docs/BTP/cca91383641e40ffbe03bdc78f00f681/f8d6f9ab43c14e52a9e8036515a472e9.html)

### Tutorial

- [Tutorials: SAP Connectivity Service](https://developers.sap.com/tutorial-navigator.html?tag=products:technology-platform/sap-cloud-platform/sap-cloud-platform-connectivity)

## Sample configuration of **SAP Connectivity service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **connectivity** by configuring your `usecase.json` file.

### Using the service plan **connectivity_proxy**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "connectivity",
      "plan": "connectivity_proxy"
    }
  ]
}
```

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "connectivity",
      "plan": "lite"
    }
  ]
}
```
