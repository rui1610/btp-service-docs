# recommendation-systems-production (Personalized Recommendation)

Personalized Recommendation is a generic reusable service. It uses state-of-the-art machine learning techniques to give visitors to your website highly personalized recommendations based on their browsing history and/or item description. Train and use machine learning models to deliver these recommendations across a wide range of business scenarios. Personalized Recommendation is part of the SAP AI Business Services portfolio.

## Service plan availability in regions

| Region | free | standard |
|--------|------|----------|
|  **eu10** | ✅ | ✅ |
|  **eu11** | ✅ | ✅ |
|  **us10** | ✅ | ✅ |

## Additional details

### Support components

- CA-ML-PR

### Discovery Center

- [SAP Discovery Center - Personalized Recommendation](https://discovery-center.cloud.sap/serviceCatalog/personalized-recommendation)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/a035e3f437c1451089e1d7d7e45f08bb/SHIP/en-US/Feature_Scope_Description_EN.pdf)
- [Help Portal Product Page](https://help.sap.com/docs/Personalized_Recommendation)
- [Security](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/240283ac032146b6829db7ca7f203370.html)
- [What Is Personalized Recommendation?](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/65078007342241bea72c2cdc9c61e6a7.html)
- [What's New](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/7ab16629782f4f5eb897b23856f61024.html)
- [API Documentation](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/b2cae121437c48778469741d978afece.html)
- [Initial Setup](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/e7aa8c29cffc403a9a3b68f236ec9f61.html)
- [Concepts](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/f7e79f6a86b2407eb135f1ca9905b56f.html)
- [Documentation](https://help.sap.com/pr)

### External

- [SAP AI Business Services - Personalized Recommendation](https://www.youtube.com/embed/AfhFxJex6iI)

### Legal

- [Legal](https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html?tag=language:english&search=Supplement%20Business%20Technology%20Platform&sort=latest_desc)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=Personalized%20Recommendation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=Personalized%20Recommendation)
- [SAP Community Topic Page](https://community.sap.com/topics/personalized-recommendation)

### Support

- [Monitoring and Troubleshooting](https://help.sap.com/docs/Personalized_Recommendation/2c2078b9efa84566ac19d44df9625c65/c9cb13e6510248bdbb60ab0ea799d046.html)

### Tutorial

- [Use Machine Learning to Get Recommendations Based on Users' Browsing History](https://developers.sap.com/mission.cp-aibus-get-recommendations.html)

## Sample configuration of **Personalized Recommendation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **recommendation-systems-production** by configuring your `usecase.json` file.

### Using the service plan **free**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "recommendation-systems-production",
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
      "name": "recommendation-systems-production",
      "plan": "standard"
    }
  ]
}
```
