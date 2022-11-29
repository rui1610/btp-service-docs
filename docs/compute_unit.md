# COMPUTE_UNIT (SAP BTP, Java server)

Java Quota

## Service plan availability in regions

| Region | PREMIUM | PREMIUM_PLUS | PRO |
|--------|---------|--------------|-----|
|  **ae1** | ✅ | ✅ | ✅ |
|  **ap1** | ✅ | ✅ | ✅ |
|  **br1** | ✅ | ✅ | ✅ |
|  **ca1** | ✅ | ✅ | ✅ |
|  **cn1** | ✅ | ✅ | ✅ |
|  **eu1** | ✅ | ✅ | ✅ |
|  **eu2** | ✅ | ✅ | ✅ |
|  **eu3** | ✅ | ✅ | ✅ |
|  **jp1** | ✅ | ✅ | ✅ |
|  **sa1** | ✅ | ✅ | ✅ |
|  **us1** | ✅ | ✅ | ✅ |
|  **us2** | ✅ | ✅ | ✅ |
|  **us3** | ✅ | ✅ | ✅ |
|  **us4** | ✅ | ✅ | ✅ |

## Additional details
### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Java%20Server)
- [Application Runtime Container](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/7613bd28711e1014839a8273b0e91070.html)
- [Java: Development](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/9bd4dd19aef947b58eadf688ccc90de7.html)
- [Java: Getting Started - Set up your Java development environment and deploy your first application in the cloud.](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e66f3eecbb5710148397a19b46c4979b.html)
- [Documentation](https://help.sap.com/docs/VIRTUAL_MACHINES)

### External

- [SAP BTP, Java Server](https://www.youtube.com/embed/-7rJdGq3G0U)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20BTP%2C%20Java%20server)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20BTP%2C%20Java%20server)

## Sample configuration of **SAP BTP, Java server** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **COMPUTE_UNIT** by configuring your `usecase.json` file.

### Using the service plan **PREMIUM** (Premium Edition for VMs: 4 CPUs, 8192 MB Memory)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "COMPUTE_UNIT",
      "plan": "PREMIUM"
    }
  ]
}
```

### Using the service plan **PREMIUM_PLUS** (Premium Plus Edition for VMs: 8 CPUs, 16384 MB Memory)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "COMPUTE_UNIT",
      "plan": "PREMIUM_PLUS"
    }
  ]
}
```

### Using the service plan **PRO** (Professional Edition for VMs: 2 CPUs, 4096 MB Memory)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "COMPUTE_UNIT",
      "plan": "PRO"
    }
  ]
}
```
