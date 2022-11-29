# cis (SAP Cloud Management service for SAP BTP)

Manage the control plane, account model, and product resources in SAP BTP using supported API interfaces provided by the SAP Cloud Management service for SAP BTP.

## Service plan availability in regions

| Region | central | local |
|--------|---------|-------|
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
### Blog

- [Introducing Cloud Management Tools – CLI and APIs for SAP BTP (Blog: Part 1)](https://blogs.sap.com/2020/09/15/introducing-cloud-management-tools-cli-and-apis-for-sap-cloud-platform-part-1/https://blogs.sap.com/2020/09/15/introducing-cloud-management-tools-cli-and-apis-for-sap-cloud-platform-part-1/)
- [Introducing Cloud Management Tools – CLI and APIs for SAP BTP (Blog: Part 2)](https://blogs.sap.com/2020/09/15/introducing-cloud-management-tools-cli-and-apis-for-sap-cloud-platform-part-2/)
- [The easy way to work with Cloud Management APIs on SAP BTP](https://blogs.sap.com/2020/12/30/the-easy-way-to-work-with-cloud-management-apis-on-sap-cloud-platform/)

### Discovery Center

- [SAP Discovery Center - Cloud Management Service](https://discovery-center.cloud.sap/serviceCatalog/cloud-management-service)

### Documentation

- [API Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/17b6a171552544a6804f12ea83112a3f.html)
- [Get an Access Token for SAP Cloud Management Service APIs](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/3670474a58c24ac2b082e76cbbd9dc19.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)
- [Account Administration Using the SAP BTP Command-Line Interface (btp CLI)](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/7c6df2db6332419ea7a862191525377c.html)

### External

- [Hands-On SAP Dev Ep.77 - Exploring btp CLI - the CLI for SAP BTP (Video by DJ Adams)](https://www.youtube.com/watch?v=U3azydhcIss)
- [Hands-On SAP Dev Ep.79 - A first look at the core service APIs for SAP BTP (Video by DJ Adams)](https://www.youtube.com/watch?v=yY3pXcw4e7c)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Cloud%20Management%20service%20for%20SAP%20BTP)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Cloud%20Management%20service%20for%20SAP%20BTP)

### Tutorial

- [Tutorial: Get Started with the Command-Line Interface for SAP BTP (btp CLI)](https://developers.sap.com/tutorials/cp-cli-automate-operations.html)

## Sample configuration of **SAP Cloud Management service for SAP BTP** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **cis** by configuring your `usecase.json` file.

### Using the service plan **central**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "cis",
      "plan": "central",
      "parameters" : {
        "grantType": "password"
      }
    }
  ]
}
```

### Using the service plan **local**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "cis",
      "plan": "local",
      "parameters" : {
        "grantType": "password"
      }
    }
  ]
}
```
