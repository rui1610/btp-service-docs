# hana-cloud (SAP HANA Cloud)

SAP HANA Cloud provides a single place to access, store, and process all enterprise data in real time. It is a cloud-native platform that reduces the complexity of multi-cloud or hybrid system landscapes. SAP HANA Cloud provides all of the advanced SAP HANA technologies for multi-model data processing in-memory or on disk. You can benefit from cloud qualities such as automatic software updates, elasticity, and low total cost of ownership by using SAP HANA Cloud either as a stand-alone solution or as an extension to your existing on-premise environment.

## Service plan availability in regions

| Region | adaptive-server-enterprise | adaptive-server-enterprise-replication | hana | hana-cloud-connection | hana-cloud-connection-free | hana-free | relational-data-lake | relational-data-lake-free |
|--------|----------------------------|----------------------------------------|------|-----------------------|----------------------------|-----------|----------------------|---------------------------|
|  **ap10** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap21** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **br10** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ch20** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu10** | | | ✅ | ✅ | | | ✅ | |
|  **eu11** | | | ✅ | ✅ | | | ✅ | |
|  **eu20** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu30** | | | ✅ | ✅ | | | ✅ | |
|  **in30** | | | ✅ | ✅ | | | ✅ | |
|  **jp10** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **jp20** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us10** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us20** | | | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us30** | | | ✅ | ✅ | | | ✅ | |

## Additional details

### Support components

- HAN-CLS-HC

### Discovery Center

- [SAP Discovery Center - SAP HANA Cloud](https://discovery-center.cloud.sap/serviceCatalog/sap-hana-cloud)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/eef71122810d4aa18d8eb6c37031f98a/latest/en-US/Feature_Scope_Description_SAP_HANA_Cloud_en.pdf)
- [SAP HANA Cloud Getting Started Guide](https://help.sap.com/viewer/db19c7071e5f4101837e23f06e576495/cloud/en-US/d0aa0ec935c1401e8deb3be35d49730b.html)
- [SAP HANA Cloud Overview Guide](https://help.sap.com/viewer/f4997718ff9d45f49f90f5d01d16d5a0/hanacloud/en-US/2f0c5e3dc11d4eb8a1d6cb878a311f43.html)
- [Help Portal Product Page](https://help.sap.com/docs/HANA_CLOUD)
- [SAP HANA Cloud, Data Lake (Help Portal Product Page)](https://help.sap.com/viewer/product/SAP_HANA_DATA_LAKE/latest/en-US)

### External

- [Top New Features in SAP HANA Cloud](https://www.youtube.com/embed/N1irItqyNco)
- [What's New in SAP HANA Cloud](https://www.youtube.com/embed/c21ug2CG0CM)
- [SAP HANA Cloud: Getting Started - Overview](https://www.youtube.com/embed/oF9Occg1bfg)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### Marketing

- [Learn more about this service and how to purchase it.](https://www.sap.com/products/cloud-platform/capabilities/data-driven-insights.hana-cloud.html)

### Onboarding

- [SAP HANA Cloud Onboarding Guide](https://www.sap.com/documents/2021/09/7476f8c4-f77d-0010-bca6-c68f7e60039b.html)

### SAP Community

- [SAP HANA Cloud Community](https://community.sap.com/topics/hana-cloud)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20HANA%20Cloud)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20HANA%20Cloud)

### Support

- [Support](https://help.sap.com/viewer/db19c7071e5f4101837e23f06e576495/cloud/en-US/4f8dabb4d8214d5d93b98dd5f2ad76c9.html)

### Tutorial

- [SAP HANA Cloud tutorials provided by SAP HANA Academy](https://www.youtube.com/playlist?list=PLkzo92owKnVzONfsNdQNmpPQvUT54UUAL)

## Sample configuration of **SAP HANA Cloud** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **hana-cloud** by configuring your `usecase.json` file.

### Using the service plan **adaptive-server-enterprise**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "adaptive-server-enterprise",
      "parameters" : {
        "data": null,
        "metadata": null
      }
    }
  ]
}
```

### Using the service plan **adaptive-server-enterprise-replication**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "adaptive-server-enterprise-replication",
      "parameters" : {
        "data": null
      }
    }
  ]
}
```

### Using the service plan **hana**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "hana",
      "parameters" : {
        "data": null,
        "metadata": null
      }
    }
  ]
}
```

### Using the service plan **hana-cloud-connection**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "hana-cloud-connection",
      "parameters" : {
        "data": null
      }
    }
  ]
}
```

### Using the service plan **hana-cloud-connection-free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "hana-cloud-connection-free",
      "parameters" : {
        "data": null
      }
    }
  ]
}
```

### Using the service plan **hana-free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "hana-free",
      "parameters" : {
        "data": null,
        "metadata": null
      }
    }
  ]
}
```

### Using the service plan **relational-data-lake**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "relational-data-lake",
      "parameters" : {
        "data": null,
        "metadata": null
      }
    }
  ]
}
```

### Using the service plan **relational-data-lake-free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "hana-cloud",
      "plan": "relational-data-lake-free",
      "parameters" : {
        "data": null,
        "metadata": null
      }
    }
  ]
}
```
