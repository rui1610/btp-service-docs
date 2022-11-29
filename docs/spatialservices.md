# spatialservices (SAP HANA spatial services)

SAP HANA spatial services provides a unified access layer for location-based services, including maps for visualization, geocoding and routing capabilities. It integrates location-based content and services from external providers into SAP products and customer applications.

## Service plan availability in regions

| Region | lite | standard |
|--------|------|----------|
|  **ap10** | ✅ | |
|  **eu10** | ✅ | ✅ |
|  **us10** | ✅ | |

## Additional details

### Support components

- BC-CP-CF-HSS

### API Hub

- [Overview | SAP HANA Spatial Services | SAP API Business Hub](https://api.sap.com/package/SAPHANASpatialServices/overview)

### Discovery Center

- [SAP Discovery Center - SAP HANA spatial services](https://discovery-center.cloud.sap/serviceCatalog/sap-hana-spatial-services)

### Documentation

- [Solution Brief](https://d.dam.sap.com/a/j8RQzaL/75866_SB_57839_enUS.pdf)
- [What's New](https://help.sap.com/viewer/ac0c08cc6e0a48ad9182f6c080043c80/Cloud/en-US)
- [What are SAP HANA Spatial Services](https://help.sap.com/viewer/c7837a0d78e24fb5b9f66a058ab9f730/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/product/SAP_HANA_SPATIAL_SERVICES)
- [Documentation](https://help.sap.com/viewer/product/SAP_HANA_SPATIAL_SERVICES/Cloud)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_HANA_SPATIAL_SERVICES)
- [Documentation](https://help.sap.com/viewer/product/SAP_HANA_SPATIAL_SERVICES/latest/)
- [Introduction to SAP HANA Spatial Services](https://www.sap.com/documents/2022/02/da29c9cc-197e-0010-bca6-c68f7e60039b.html)

### Onboarding

- [Tutorial: Onboarding](https://help.sap.com/viewer/4e2337c5371a4ac18195cfe751514735/Cloud/en-US)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20HANA%20spatial%20services)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20HANA%20spatial%20services)

## Sample configuration of **SAP HANA spatial services** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **spatialservices** by configuring your `usecase.json` file.

### Using the service plan **lite**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "spatialservices",
      "plan": "lite"
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
      "name": "spatialservices",
      "plan": "standard"
    }
  ]
}
```
