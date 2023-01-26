# abap (SAP BTP, ABAP environment)

Access an instance to build custom ABAP cloud apps, leveraging newest innovations powered by SAP HANA.

## Service plan availability in regions

| Region | 16_abap_64_db | abap_compute_unit | free | hana_compute_unit | standard |
|--------|---------------|-------------------|------|-------------------|----------|
|  **ap10** | | ✅ | ✅ | ✅ | ✅ |
|  **ap11** | | ✅ | ✅ | ✅ | ✅ |
|  **ap12** | | ✅ | ✅ | ✅ | ✅ |
|  **br10** | | ✅ | ✅ | ✅ | ✅ |
|  **ca10** | | ✅ | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **eu11** | | ✅ | ✅ | ✅ | ✅ |
|  **jp10** | ✅ | ✅ | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ | ✅ | ✅ |

## Additional details

### Support components

- BC-CP-ABA-LP

### API Hub

- [Overview | SAP BTP ABAP Environment | SAP API Business Hub](https://api.sap.com/package/SAPCPABAPENV/overview)

### Discovery Center

- [SAP Discovery Center - ABAP environment](https://discovery-center.cloud.sap/serviceCatalog/abap-environment)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/5e8107bf49684962b897217040398007/)
- [Security](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e129aa20c78c4a9fb379b9803b02e5f6.html)
- [Initial Setup](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/e34a329acc804c0e874496548183682f.html)
- [Documentation](https://help.sap.com/docs/BTP/3504ec5ef16548778610c7e89cc0eac3/11d62652aa2b4600a0fa136de0789648.html)
- [API Documentation](https://help.sap.com/docs/BTP/5371047f1273405bb46725a417f95433/272ad1b3b09948d6a86b52ffa21c55bb.html)
- [What is ABAP Environment](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/11d62652aa2b4600a0fa136de0789648.html)
- [Onboarding](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/2ffdd2412aff494dbf3de31089c965d4.html)
- [Documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/31367ef6c3e947059e0d7c1cbfcaae93.html)
- [What's New](https://help.sap.com/whats-new/cf0cb2cb149647329b5d02aa96303f56?Component=ABAP%2520Environment&Environment=ABAP)

### External

- [Developer Tools for the ABAP Environment](https://www.youtube.com/embed/VMww435AM48)

### Learning

- [Learning Journey](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/49047e7668844d419ccee567923a475e.html)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP BTP, ABAP Environment Community](https://community.sap.com/topics/cloud-platform-abap-environment)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20BTP%2C%20ABAP%20environment)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20BTP%2C%20ABAP%20environment)

### Support

- [Getting Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

### Tool

- [ABAP Development Tools](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/54dd7126d5b74efeb7a21f6b0bfe5f1a.html)
- [ABAP RESTful Application Programming Model](https://help.sap.com/docs/BTP/923180ddb98240829d935862025004d6/289477a81eec4d4e84c0302fb6835035.html)

### Tutorial

- [Tutorial Navigator](https://developers.sap.com/tutorial-navigator.html?tag=software-product%3Atechnology-platform%2Fsap-business-technology-platform%2Fsap-btp-abap-environment)
- [Tutorial: Get Started with ABAP Programming on SAP BTP](https://learning.sap.com/learning-journey/get-started-with-abap-programming-on-sap-btp)

## Sample configuration of **SAP BTP, ABAP environment** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **abap** by configuring your `usecase.json` file.

### Using the service plan **16_abap_64_db** (16_abap_64_db (DEPRECATED))

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "abap",
      "plan": "16_abap_64_db",
      "parameters" : {
        "admin_email": null,
        "description": null,
        "sapsystemname": "H01",
        "is_development_allowed": true,
        "size_of_persistence": 4,
        "size_of_runtime": 1
      }
    }
  ]
}
```

### Using the service plan **abap_compute_unit**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "abap",
      "plan": "abap_compute_unit"
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
      "category": "SERVICE",
      "name": "abap",
      "plan": "free",
      "parameters" : {
        "admin_email": null,
        "description": null,
        "sapsystemname": "H01"
      }
    }
  ]
}
```

### Using the service plan **hana_compute_unit**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "abap",
      "plan": "hana_compute_unit"
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
      "name": "abap",
      "plan": "standard",
      "parameters" : {
        "admin_email": null,
        "description": null,
        "sapsystemname": "H01",
        "is_development_allowed": true,
        "size_of_persistence": 4,
        "size_of_runtime": 1
      }
    }
  ]
}
```
