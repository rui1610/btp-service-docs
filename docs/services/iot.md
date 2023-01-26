# iot (Internet of Things)

The SAP Business Technology Platform Internet of Things service for the Cloud Foundry environment connects devices to SAP Business Technology Platform to provide scalable ingestion of IoT data and device management. The respective services provide a secure connection to remote devices using a broad variety of IoT protocols and manage the device lifecycle from onboarding to decommissioning. 

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **eu10** | ✅ |
|  **us10** | ✅ |

## Additional details
### Discovery Center

- [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-iot)

### Documentation

- [Discuss with IoT developers and experts](https://developers.sap.com/topics/iot-application-enablement.html#community)
- [IoT Starter Kit](https://github.com/SAP/iot-starterkit/tree/master/cf)
- [Internet of Things](https://www.sap.com/community/topics/internet-of-things.html)
- [Feature Scope Description](https://help.sap.com/doc/f7254d7f9e0d4dc9b54a3f5f95987a2b/latest/en-US/leonardo_iot_fsd.pdf)
- [API Documentation](https://help.sap.com/viewer/080fabc6cae6423fb45fca7752adb61e/latest/en-US)
- [Initial Setup](https://help.sap.com/viewer/195126f4601945cba0886cbbcbf3d364/latest/en-US/bfe6a46a13d14222949072bf330ff2f4.html)
- [Rule-based IoT Data Processing](https://help.sap.com/viewer/1ab61090ec4c4c779cd4360372ab95b5/latest/en-US)
- [Introduction](https://help.sap.com/viewer/2f1daa938df84fd090fa2a4da6e4bc05/Cloud/en-US)
- [Tenant Administration](https://help.sap.com/viewer/500ea53fcd9a4974a338747cebf1d350/latest/en-US)
- [Internet of Things Service API Documentation](https://help.sap.com/viewer/6040fec3f22e4f9b8bf495f3789d66b5/Cloud/en-US)
- [Internet of Things Gateway](https://help.sap.com/viewer/643f531cbf50462c8cc45139ba2dd051/Cloud/en-US)
- [What's New](https://help.sap.com/viewer/81d9f9ab5a3b430f83430c9f41aacb27/latest/en-US)
- [Internet of Things Service Cockpit](https://help.sap.com/viewer/9a8cae62b9ab4278af1f39e188b11bc7/Cloud/en-US)
- [Release Notes](https://help.sap.com/viewer/a91b9b0c730241f99b6dd32fdc310a5b/Cloud/en-US)
- [Internet of Things Service SDK](https://help.sap.com/viewer/c4945853cc164aa385973d5938b385ac/Cloud/en-US)
- [Documentation](https://help.sap.com/viewer/ccc9cfa0ae70491ab359e5a414f9a1d9/Cloud)
- [Thing Modeler Apps](https://help.sap.com/viewer/e057ad687acc4d2d8f2893609aff248b/latest/en-US)
- [What is SAP IoT](https://help.sap.com/viewer/fffd6ca18e374c2e80688dab5c31527f/latest/en-US)
- [Documentation](https://help.sap.com/docs/SAP_CP_IOT_CF)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_I)

### External

- [Activating Innovation with SAP IoT](https://www.youtube.com/embed/T0y30QPe8jo)

### Marketing

- [Learn more about this service and how to purchase it.](https://cloudplatform.sap.com/capabilities/iot/iot-service.html)

### Onboarding

- [Enable the SAP IoT Services for Cloud Foundry](https://help.sap.com/viewer/c48328a1bee749da9902d52f080dba0d/Cloud/en-US)

### Support

- [Support ticket components for SAP IoT](https://help.sap.com/viewer/195126f4601945cba0886cbbcbf3d364/latest/en-US/60e9baa62230413b8870db44c741eef1.html)
- [Get Support](https://help.sap.com/viewer/5429aeb5a5dc40fab09b3ab74d0f6e45/Cloud/en-US)
- [FAQ](https://help.sap.com/viewer/91fd5e851c3549d9880f294977f098eb/Cloud/en-US)

### Tutorial

- [Tutorial Group: Get Started with SAP IoT Services for SAP BTP](https://developers.sap.com/group.iot-cf-get-started.html)
- [Tutorial: Develop your own Internet of Things (IoT) applications](https://developers.sap.com/topics/iot-application-enablement.html#tutorials)
- [Create a Device Model Using the API](https://help.sap.com/viewer/565d09b96468492aacee0f3f37282053/Cloud/en-US)
- [Send Commands with MQTT](https://help.sap.com/viewer/59a0d95c692d42f2bd149711ed22a547/Cloud/en-US)
- [Create User and Tenant](https://help.sap.com/viewer/78ac6b240a97447986e09b991d8a570a/Cloud/en-US)
- [Consume Measures](https://help.sap.com/viewer/7e269da75d024ef09bfb7a5986c47517/Cloud/en-US)
- [Send Data with REST](https://help.sap.com/viewer/d5f07bf9e1d646959a006f98d4cce321/Cloud/en-US)
- [Send Data with MQTT](https://help.sap.com/viewer/e765b2a5b99540ce84da397c20cc1993/Cloud/en-US)

## Sample configuration of **Internet of Things** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **iot** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "iot",
      "plan": "standard"
    }
  ]
}
```
