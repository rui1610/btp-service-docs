# intercompany-reconciliation (SAP S/4HANA Cloud for intelligent intercompany reconciliation)

Intelligent Intercompany Reconciliation is introduced to speed up your intercompany reconciliation process from company close to corporate close. The service is based on Artificial Intelligence in order to reconcile your financial data with high accuracy.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |

## Additional details

### Support components

- FIN-CS-ICR

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/)
- [SAP Discovery Center - Intelligent intercompany reconciliation](https://discovery-center.cloud.sap/serviceCatalog/intelligent-intercompany-reconciliation)

### Documentation

- [Documentation](https://help.sap.com/viewer/0fa84c9d9c634132b7c4abb9ffdd8f06/2108.501/en-US/b0b3b968f7c943c88ebc6e94d114564e.html)
- [Feature Description in SAP S/4HANA Documentation](https://help.sap.com/viewer/4ebf1502064b406c964b0911adfb3f01/latest/en-US/b0b3b968f7c943c88ebc6e94d114564e.html)
- [Feature Description in SAP S/4HANA Cloud Documentation](https://help.sap.com/viewer/90c07e91c7a64f328be3fd6b48955b13/latest/en-US/b0b3b968f7c943c88ebc6e94d114564e.html)

### External

- [Intelligent Intercompany Reconciliation with Machine Learning](https://www.youtube.com/embed/3-5rZikNi-I)

### Onboarding

- [Tutorial: Onboarding](https://help.sap.com/viewer/90c07e91c7a64f328be3fd6b48955b13/latest/en-US/300483fa78a841728499f25fbaceee14.html)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20S/4HANA%20Cloud%20for%20intelligent%20intercompany%20reconciliation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20S/4HANA%20Cloud%20for%20intelligent%20intercompany%20reconciliation)

## Sample configuration of **SAP S/4HANA Cloud for intelligent intercompany reconciliation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **intercompany-reconciliation** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "intercompany-reconciliation",
      "plan": "standard"
    }
  ]
}
```
