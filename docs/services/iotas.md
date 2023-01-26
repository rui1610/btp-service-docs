# iotas (SAP IoT)

SAP IoT business services allow you to put raw sensor data into business object context and then use query models, rules, events and actions to leverage the data near real-time in analytical or transactional business applications.

## Service plan availability in regions

| Region | oneproduct | standard |
|--------|------------|----------|
|  **eu10** | ✅ | ✅ |
|  **eu20** | ✅ | |
|  **us10** | ✅ | ✅ |
|  **us20** | ✅ | |

## Additional details

### Support components

- IOT-BSV-OPS-ONB
- LOD-HCI-PI

### Discovery Center

- [SAP Discovery Center - SAP IoT](https://discovery-center.cloud.sap/serviceCatalog/sap-iot)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/f7254d7f9e0d4dc9b54a3f5f95987a2b/latest/en-US/leonardo_iot_fsd.pdf)
- [Onboarding](https://help.sap.com/viewer/195126f4601945cba0886cbbcbf3d364/latest/en-US/bfe6a46a13d14222949072bf330ff2f4.html)
- [Rule-based IoT Data Processing](https://help.sap.com/viewer/1ab61090ec4c4c779cd4360372ab95b5/latest/en-US)
- [Tenant Administration](https://help.sap.com/viewer/500ea53fcd9a4974a338747cebf1d350/latest/en-US)
- [What's New](https://help.sap.com/viewer/81d9f9ab5a3b430f83430c9f41aacb27/latest/en-US)
- [Thing Modeler Apps](https://help.sap.com/viewer/e057ad687acc4d2d8f2893609aff248b/latest/en-US)
- [What is SAP IoT](https://help.sap.com/viewer/fffd6ca18e374c2e80688dab5c31527f/latest/en-US/3c61bd1bedc4473fbd952e92b5e7cf8d.html)
- [Help Portal Product Page](https://help.sap.com/docs/SAP_I)
- [Documentation](https://help.sap.com/docs/SAP_L)

### External

- [SAP IoT Jam Page](https://jam4.sapjam.com/groups/798dvYCPdNyqZMskeFof8j/overview_page/l6ZtC0kGqLcxghEV7m2lN4)
- [Automate Replenishment Processes with SAP IoT](https://www.youtube.com/embed/1CPBpXW6Ls8)
- [Monitor Delivery Conditions in Real-Time with SAP IoT](https://www.youtube.com/embed/R53ut4RdznM)
- [Quality Control for Goods Receipt](https://www.youtube.com/embed/ROnhz4sQd54)
- [SAP IoT-enabled Handling Unit Management](https://www.youtube.com/embed/ch0YyHl3g3c)
- [SAP IoT-enabled Machine Monitoring](https://www.youtube.com/embed/rA74qjdcQ1M)
- [SAP IoT-Enabled Kanban + Goods Movement](https://www.youtube.com/embed/wVPUDaVuvkA)

### Support

- [Support ticket components for SAP IoT](https://help.sap.com/viewer/195126f4601945cba0886cbbcbf3d364/latest/en-US/60e9baa62230413b8870db44c741eef1.html)

## Sample configuration of **SAP IoT** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **iotas** by configuring your `usecase.json` file.

### Using the service plan **oneproduct**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "iotas",
      "plan": "oneproduct"
    }
  ]
}
```

### Using the service plan **standard** (Leonardo IoT)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "iotas",
      "plan": "standard"
    }
  ]
}
```
