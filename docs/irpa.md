# IRPA (SAP Intelligent Robotic Process Automation)

SAP Intelligent Robotic Process Automation lets you automate enterprise business processes. Design process automations with the Desktop Studio by creating end-to-end scenarios. Import these scenarios into the cloud Factory to configure and execute them with Agents. An Agent can work as a Digital Assistant (attended automation) or as a Digital Worker (unattended automation).

## Service plan availability in regions

| Region | concurrent | default | free |
|--------|------------|---------|------|
|  **ap10** | ✅ | ✅ | ✅ |
|  **eu10** | ✅ | ✅ | ✅ |
|  **eu11** | ✅ | | ✅ |
|  **jp10** | ✅ | ✅ | ✅ |
|  **us10** | ✅ | ✅ | ✅ |
|  **us20** | ✅ | | ✅ |

## Additional details

### Support components

- CA-ML-IPA

### API Hub

- [Overview | SAP Intelligent Robotic Process Automation | SAP API Business Hub](https://api.sap.com/package/SAPIntelligentRoboticProcessAutomation/overview)

### Discovery Center

- [SAP Discovery Center - SAP Intelligent RPA](https://discovery-center.cloud.sap/serviceCatalog/sap-intelligent-rpa)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/7d0be7dad2854adb9e7f6d440254d090/)
- [What's New](https://help.sap.com/viewer/0f258aabfbdb476b9bebbc636a1ca5cc/Cloud/en-US)
- [SAP Intelligent RPA Security Guide](https://help.sap.com/viewer/2df9d6a452f84f8a8be2739e1bfea259/Cloud/en-US)
- [SAP Intelligent RPA Installation Guide](https://help.sap.com/viewer/6b9c8e86a0be43539b670de962834562/Cloud/en-US)
- [SAP Intelligent RPA Desktop Studio Developer Guide](https://help.sap.com/viewer/8ecea00c1f854fd0a433c4aef5da1ea2/Cloud/en-US)
- [SAP Intelligent RPA Factory User Guide](https://help.sap.com/viewer/c836fab4182e45548b6c6c6d0d0a9146/Cloud/en-US)
- [Help Portal Product Page](https://help.sap.com/docs/IRPA)

### External

- [https://www.youtube.com/embed/9wjBgFePoYk](https://www.youtube.com/embed/9wjBgFePoYk)

### Learning

- [SAP Intelligent RPA Store](https://irpa.store.sap.com/#/explore/order=last-updated%2Cdesc)

### SAP Community

- [SAP Intelligent Robotic Process Automation Community](https://community.sap.com/topics/intelligent-rpa)
- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Intelligent%20Robotic%20Process%20Automation)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Intelligent%20Robotic%20Process%20Automation)

## Sample configuration of **SAP Intelligent Robotic Process Automation** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **IRPA** by configuring your `usecase.json` file.

### Using the service plan **concurrent** (Concurrent)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "concurrent"
    }
  ]
}
```

### Using the service plan **default** (SAP Intelligent Robotic Process Automation)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "default"
    }
  ]
}
```

### Using the service plan **free** (Free)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "IRPA",
      "plan": "free"
    }
  ]
}
```
