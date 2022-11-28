# credstore (SAP Credential Store)

The Credential Store provides a secure repository for passwords and keys to applications that are running on SAP Business Technology Platform. It enables the applications to retrieve credentials and use them for authentication to external services, or to perform cryptographic operations and TLS communication. 

## Service plan availability in regions

| Region | free | proxy | standard |
|--------|------|-------|----------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **ap11** | ✅ | ✅ | ✅ |
|  **ap12** | ✅ | ✅ | ✅ |
|  **ap20** | ✅ | ✅ | ✅ |
|  **ap21** | ✅ | ✅ | ✅ |
|  **br10** | ✅ | ✅ | ✅ |
|  **ca10** | ✅ | ✅ | ✅ |
|  **ch20** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | ✅ | ✅ |
|  **eu20** | ✅ | ✅ | ✅ |
|  **eu30** | ✅ | ✅ | ✅ |
|  **in30** | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **jp20** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | ✅ | ✅ |
|  **us21** | ✅ | ✅ | ✅ |
|  **us30** | ✅ | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-CF-SEC-CPG

### API Hub

- [Overview | SAP Credential Store | SAP API Business Hub](https://api.sap.com/package/CredentialStore/overview)

### Discovery Center

- [SAP Discovery Center - Credential Store](https://discovery-center.cloud.sap/serviceCatalog/credential-store)

### Documentation

- [API Documentation](https://api.sap.com/package/CredentialStore?section=Artifacts)
- [Feature Scope Description](https://help.sap.com/http.svc/rc/2ff85d34e0504248a2b145899afd84d8/Cloud/en-US/Credential_Store_FSD.pdf)
- [What is SAP Credential Store](https://help.sap.com/docs/BTP/601525c6e5604e4192451d5e7328fa3c/02e8f7d1016740b8adf68690f36df142.html)
- [What's New](https://help.sap.com/docs/BTP/601525c6e5604e4192451d5e7328fa3c/6a37641afec9497bb76e1063ee73f536.html)
- [Documentation](https://help.sap.com/docs/BTP/601525c6e5604e4192451d5e7328fa3c/ad63368e8e6f44a1b3ac336e8d1c32b8.html)
- [Initial Setup](https://help.sap.com/docs/BTP/601525c6e5604e4192451d5e7328fa3c/d5f1ce7bd8c041bb8cf4b328e06938a2.html)
- [Help Portal Product Page](https://help.sap.com/docs/CREDENTIAL_STORE)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Credential%20Store)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Credential%20Store)

### Support

- [Getting Support](https://help.sap.com/docs/BTP/601525c6e5604e4192451d5e7328fa3c/c6ebd580c0a642e9a99dbb8ae5c6c562.html)

## Sample configuration of **SAP Credential Store** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **credstore** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "credstore",
      "plan": "free"
    }
  ]
}
```

### Using the service plan **proxy**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "credstore",
      "plan": "proxy"
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
      "category": "SERVICE",
      "name": "credstore",
      "plan": "standard"
    }
  ]
}
```
