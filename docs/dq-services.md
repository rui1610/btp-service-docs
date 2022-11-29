# dq-services (data quality service)

SAP Data Quality Management offers cloud-based services that let you embed address cleansing, geocoding, and reverse geocoding within any business process orapplication,so that you can reap the value of complete and accurate address data.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **eu10** | ✅ | ✅ |

## Additional details

### Support components

- EIM-DQM-SVS

### API Hub

- [Overview | SAP Data Quality Management, microservices for location data | SAP API Business Hub](https://api.sap.com/package/SAPCPDataQualityManagementmicroservices/overview)

### Discovery Center

- [SAP Discovery Center - Data Quality Services](https://discovery-center.cloud.sap/serviceCatalog/data-quality-services)
- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-data-quality-management)

### Documentation

- [What's New](https://help.sap.com/doc/43b304f99a8145809c78f292bfc0bc58/Cloud/en-US/98bf747111574187a7c76f8ced51cfeb.html?Component=Data%20Quality%20Services)
- [Feature Scope Description for Data Quality Management, Microservices for Location Data](https://help.sap.com/doc/dfe5f4c1b3294036a8a5f3baad7311d3/)
- [Documentation](https://help.sap.com/viewer/d95546360fea44988eb614718ff7e959/Cloud/)
- [What is Data Quality Management, Microservices for Location Data](https://help.sap.com/viewer/d95546360fea44988eb614718ff7e959/Cloud/en-US)
- [Documentation](https://help.sap.com/docs/BTP/d95546360fea44988eb614718ff7e959/746b418f655840179a99cbdf9073324f.html)
- [Help Portal Product Page](https://help.sap.com/viewer/product/SAP_Data_Quality_Management_microservices_for_location_data/Cloud/en-US)
- [Documentation](https://www.sap.com/documents/2019/08/7a08c953-607d-0010-87a3-c30de2ffd8ff.html)
- [Documentation](https://www.sapstore.com/solutions/41227/SAP-Data-Quality-Management%2C-microservices-for-location-data)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)
- [Legal](https://www.sap.com/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?tag=agreements:product-use-support-terms/on-premise-software/software-use-rights/)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=data%20quality%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=data%20quality%20service)

## Sample configuration of **data quality service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **dq-services** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "dq-services",
      "plan": "free"
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
      "name": "dq-services",
      "plan": "standard"
    }
  ]
}
```
