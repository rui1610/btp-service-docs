# ml-foundation (SAP Leonardo ML Foundation)

SAP Leonardo Machine Learning Foundation enables you to enhance business processes and software applications with intelligence. Unlock knowledge from structured and unstructured data such as images, text, time series and tabular data. By consuming easy-to-use APIs you can detect the content of pictures, extract keywords from natural language texts or analyze and forecast time-series data. All this can be done without prior investmentintospecial hardware or expertise in machine learning. Besides using pre-trained ML services you can also deploy custom ML models or tune existing models with your own training data. This allows you to easily serve customized ML models for critical business processes in a scalable and secure manner.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |
|  **us30** | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/machine-learning-foundation)

### Documentation

- [Documentation](http://help.sap.com/mlf)
- [Feature Scope Description](https://help.sap.com/doc/690e5969eec141579ba0afce0170e7b0/latest/en-US/loio0e40a39a3b27468f9c95fe3705a36dec.pdf)
- [Help Portal Product Page](https://help.sap.com/mlf)
- [What's New](https://help.sap.com/viewer/2e6173bf645243bb9a88f0269250f3a2/latest/en-US/b2fd7c3da7d9445283cb6407e2616e7d.html)
- [Documentation](https://help.sap.com/docs/SAP_LEONARDO_MACHINE_LEARNING_FOUNDATION)

### Learning

- [Learning Journey: SAP Leonardo Machine Learning](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/5004c04c7a261014806dd6ca0b4c6cbb.html)

## Sample configuration of **SAP Leonardo ML Foundation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **ml-foundation** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "ml-foundation",
      "plan": "standard"
    }
  ]
}
```
