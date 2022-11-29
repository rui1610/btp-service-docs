# iotae (SAP IoT)

SAP IoT business services allow you to put raw sensor data into business object context and then use query models, rules, events and actions to leverage the data near real-time in analytical or transactional business applications.

## Service plan availability in regions

| Region | default | standard |
|--------|---------|----------|
|  **eu10** | ✅ | ✅ |
|  **eu20** | ✅ | ✅ |
|  **us10** | ✅ | |
|  **us20** | ✅ | |

## Additional details
### Documentation

- [Documentation](https://answers.sap.com/tags/73554900100800002247)
- [Enterprise Architecture Explorer Product Page](https://eaexplorer.hana.ondemand.com/_item.html?id=12351#!/facet/18)
- [From Things to Outcomes Presentation](https://eaexplorer.hana.ondemand.com/rest/mimeRepositories/12412/file/L1_IoT_app_services_August_2016.pdf)
- [Documentation ](https://help.sap.com/docs/SAP_IOT_APPLICATION_SERVICES)
- [Documentation](https://help.sap.com/docs/SAP_I)
- [Documentation](https://help.sap.com/docs/SAP_L)
- [Open SAP Course ](https://open.sap.com/courses/iot3)
- [Tutorials ](https://www.sap.com/developer/topics/iot-application-enablement.tutorials.html#tutorials)
- [Authorization Guide](https://www.sap.com/documents/2017/12/aa0c7165-e67c-0010-82c7-eda71af511fa.html)

### External

- [SAP IoT Application Enablement - Thing Modeler](https://www.youtube.com/embed/KQJqkhary08)
- [SAP IoT Application Enablement - Developer Experience & Web IDE](https://www.youtube.com/embed/x5S6t6XNUxE)
- [SAP Leonardo IoT Training Sessions](https://www.youtube.com/playlist?list=PLWV533hWWvDnP5S4PLiC1d-J7hj1sjZn6)

### Marketing

- [To learn more about the service and the purchasing options please contact your account executive or visit our SAP Store.](https://www.sapstore.com/solutions/40108/SAP-Leonardo-IoT-Foundation%2C-express-edition)

## Sample configuration of **SAP IoT** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **iotae** by configuring your `usecase.json` file.

### Using the service plan **default**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "iotae",
      "plan": "default"
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
      "name": "iotae",
      "plan": "standard"
    }
  ]
}
```
