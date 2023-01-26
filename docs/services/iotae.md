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

- [Discuss with IoT developers and experts](https://developers.sap.com/topics/iot-application-enablement.html#community)
- [Documentation](https://answers.sap.com/tags/73554900100800002247)
- [Enterprise Architecture Explorer Product Page](https://eaexplorer.hana.ondemand.com/_item.html?id=12351#!/facet/18)
- [From Things to Outcomes Presentation](https://eaexplorer.hana.ondemand.com/rest/mimeRepositories/12412/file/L1_IoT_app_services_August_2016.pdf)
- [Feature Scope Description](https://help.sap.com/doc/f7254d7f9e0d4dc9b54a3f5f95987a2b/latest/en-US/leonardo_iot_fsd.pdf)
- [API Documentation](https://help.sap.com/viewer/080fabc6cae6423fb45fca7752adb61e/latest/en-US)
- [Initial Setup](https://help.sap.com/viewer/195126f4601945cba0886cbbcbf3d364/latest/en-US/bfe6a46a13d14222949072bf330ff2f4.html)
- [Rule-based IoT Data Processing](https://help.sap.com/viewer/1ab61090ec4c4c779cd4360372ab95b5/latest/en-US)
- [Tenant Administration](https://help.sap.com/viewer/500ea53fcd9a4974a338747cebf1d350/latest/en-US)
- [What's New](https://help.sap.com/viewer/81d9f9ab5a3b430f83430c9f41aacb27/latest/en-US)
- [Thing Modeler Apps](https://help.sap.com/viewer/e057ad687acc4d2d8f2893609aff248b/latest/en-US)
- [What is SAP IoT](https://help.sap.com/viewer/fffd6ca18e374c2e80688dab5c31527f/latest/en-US)
- [Documentation ](https://help.sap.com/docs/SAP_IOT_APPLICATION_SERVICES)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_I)
- [Documentation](https://help.sap.com/docs/SAP_L)
- [Open SAP Course ](https://open.sap.com/courses/iot3)
- [Tutorials ](https://www.sap.com/developer/topics/iot-application-enablement.tutorials.html#tutorials)
- [Authorization Guide](https://www.sap.com/documents/2017/12/aa0c7165-e67c-0010-82c7-eda71af511fa.html)

### External

- [SAP IoT Application Enablement - Thing Modeler](https://www.youtube.com/embed/KQJqkhary08)
- [Activating Innovation with SAP IoT](https://www.youtube.com/embed/T0y30QPe8jo)
- [SAP IoT Application Enablement - Developer Experience & Web IDE](https://www.youtube.com/embed/x5S6t6XNUxE)
- [SAP Leonardo IoT Training Sessions](https://www.youtube.com/playlist?list=PLWV533hWWvDnP5S4PLiC1d-J7hj1sjZn6)

### Marketing

- [To learn more about the service and the purchasing options please contact your account executive or visit our SAP Store.](https://www.sapstore.com/solutions/40108/SAP-Leonardo-IoT-Foundation%2C-express-edition)

### Support

- [Support ticket components for SAP IoT](https://help.sap.com/viewer/195126f4601945cba0886cbbcbf3d364/latest/en-US/60e9baa62230413b8870db44c741eef1.html)

### Tutorial

- [Tutorial: Develop your own Internet of Things (IoT) applications](https://developers.sap.com/topics/iot-application-enablement.html#tutorials)

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
