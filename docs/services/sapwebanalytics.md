# SAPWebAnalytics (SAP Web Analytics)

SAP Web Analytics enables the collection and analysis of website data for understanding and optimizing web usage to measure organizational goals, drive strategy and improve the user's experience.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap21** | ✅ |
|  **eu10** | ✅ |
|  **eu20** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Web Analytics | SAP API Business Hub](https://api.sap.com/package/SAPWebAnalytics/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/web-analytics)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/8ebb4ffdfabb460e9591c60015f71d37/)
- [What's New](https://help.sap.com/docs/BTP/e342b49c78c74d4e8ebc00700a791aee/54d8cb9ae92f4597b85237fb54fd2a39.html)
- [What is SAP Web Analytics](https://help.sap.com/docs/BTP/e342b49c78c74d4e8ebc00700a791aee/e90c64af5dc04a238b324b359558cd48.html)
- [Documentation](https://help.sap.com/viewer/product/SAP_WEB_ANALYTICS/1.0/en-US)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_WEB_ANALYTICS)

### External

- [SAP Web Analytics](https://www.youtube.com/embed/bXMtor_AmPE)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### Onboarding

- [Tutorial: Onboarding](https://developers.sap.com/mission.cp-web-analytics-get-started.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Web%20Analytics)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Web%20Analytics)

### Tool

- [SAp Web Analytics Dashboard](https://help.sap.com/docs/BTP/e342b49c78c74d4e8ebc00700a791aee/70cbc79762c34409ba6b56c883a695a3.html)

## Sample configuration of **SAP Web Analytics** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **SAPWebAnalytics** by configuring your `usecase.json` file.

### Using the service plan **standard** (SAP Web Analytics)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "SAPWebAnalytics",
      "plan": "standard"
    }
  ]
}
```
