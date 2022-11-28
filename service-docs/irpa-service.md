# irpa-service (SAP Intelligent Robotic Process Automation)

SAP Intelligent Robotic Process Automation (SAP Intelligent RPA) lets you automate enterprise business processes. Design process automations with the Desktop Studio by creating end-to-end scenarios. Import these scenarios into the cloud Factory powered by SAP Business Technology Platform to configure and execute them with Agents. Agents running on workstations can work as a Digital Assistant (attended automation) or as a Digital Worker (unattended automation).	

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **jp10** | ✅ |
|  **us10** | ✅ |

## Additional details
### API Hub

- [Overview | SAP Intelligent Robotic Process Automation | SAP API Business Hub](https://api.sap.com/package/SAPIntelligentRoboticProcessAutomation/overview)

### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-intelligent-rpa)

### Documentation

- [Documentation](https://help.sap.com/docs/IRPA)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Intelligent%20Robotic%20Process%20Automation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Intelligent%20Robotic%20Process%20Automation)

## Sample configuration of **SAP Intelligent Robotic Process Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **irpa-service** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "irpa-service",
      "plan": "standard"
    }
  ]
}
```
