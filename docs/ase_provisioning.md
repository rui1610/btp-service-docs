# ASE_PROVISIONING (SAP ASE service)

The SAP ASE service on SAP Business Technology Platform lets you consume SAP ASE databases from your applications running on SAP Business Technology Platform or on-premise via Java APIs. It offers variousself-services, for example, that let you create or update databases, whileSAPis providing infrastructure and database platform operations.

## Service plan availability in regions

| Region | LARGE | MEDIUM | SMALL | XLARGE | XSMALL |
|--------|-------|--------|-------|--------|--------|
|  **ae1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ap1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **br1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **ca1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **cn1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu2** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu3** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **jp1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **sa1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us1** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us2** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us3** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us4** | ✅ | ✅ | ✅ | ✅ | ✅ |

## Additional details
### Discovery Center

- [SAP Discovery Center - SAP ASE Service](https://discovery-center.cloud.sap/serviceCatalog/sap-ase-service)

### Documentation

- [Feature Scope Description](https://help.sap.com/http.svc/rc/4ee2da29013642dd82163b5d57e6d04b/Cloud/en-US/en_fsd_sap_ase.pdf)
- [What Is SAP ASE Service?](https://help.sap.com/docs/BTP/3fa880aa54b74110ae99ad01503fcd60/72cce348772749e7bdeea5db36a38a8f.html)
- [Initial Setup](https://help.sap.com/docs/BTP/3fa880aa54b74110ae99ad01503fcd60/8652a7bd712349458f7d016389277f61.html)
- [Help Portal Product Page](https://help.sap.com/docs/ASE_SERVICE)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/data-storage/ase-dbaas.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20ASE%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20ASE%20service)

## Sample configuration of **SAP ASE service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ASE_PROVISIONING** by configuring your `usecase.json` file.

### Using the service plan **LARGE** (ASE 320GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "LARGE"
    }
  ]
}
```

### Using the service plan **MEDIUM** (ASE 160GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "MEDIUM"
    }
  ]
}
```

### Using the service plan **SMALL** (ASE 80GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "SMALL"
    }
  ]
}
```

### Using the service plan **XLARGE** (ASE 640GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "XLARGE"
    }
  ]
}
```

### Using the service plan **XSMALL** (ASE 40GB)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ASE_PROVISIONING",
      "plan": "XSMALL"
    }
  ]
}
```
