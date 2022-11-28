# jobscheduler (SAP Job Scheduling service)

The Job Scheduling Service allows you to define and manage jobs that run once or on recurring schedules. Use this runtime-agnostic service to schedule REST endpoint actions in your application or to schedule long-running processes using Cloud Foundry tasks. Use REST APIs to schedule your jobs, including long-running jobs asynchronously, and create multiple schedule formats for both simple and complex recurring schedules. The service dashboard is a web interface that lets you manage jobs and schedules.

## Service plan availability in regions

| Region | standard |
|--------|----------|
|  **ap10** | ✅ |
|  **ap11** | ✅ |
|  **ap12** | ✅ |
|  **ap20** | ✅ |
|  **ap21** | ✅ |
|  **br10** | ✅ |
|  **ca10** | ✅ |
|  **ch20** | ✅ |
|  **eu10** | ✅ |
|  **eu11** | ✅ |
|  **eu20** | ✅ |
|  **eu30** | ✅ |
|  **in30** | ✅ |
|  **jp10** | ✅ |
|  **jp20** | ✅ |
|  **us10** | ✅ |
|  **us20** | ✅ |
|  **us21** | ✅ |
|  **us30** | ✅ |

## Additional details

### Support components

- BC-XS-SRV-JBS

### Discovery Center

- [SAP Discovery Center - Job Scheduling Service](https://discovery-center.cloud.sap/serviceCatalog/job-scheduling-service)

### Documentation

- [Feature Scope Description](https://help.sap.com/doc/7f81b475a5aa43dcbea7baeb08171a02/)
- [What is SAP Job Scheduling Service](https://help.sap.com/docs/BTP/07b57c2f4b944bcd8470d024723a1631/22c2df4d22cb4a05af4c9502a67597ae.html)
- [Help Portal Product Page](https://help.sap.com/docs/JOB_SCHEDULER)
- [What's New](https://help.sap.com/whats-new/cf0cb2cb149647329b5d02aa96303f56?Component=Job%2520Scheduling%2520Service&Valid_as_Of=2022-01-01%253A2022-12-31)
- [Documentation](https://www.sapstore.com/solutions/40166/SAP-Cloud-Platform-Job-Scheduler)

### Onboarding

- [Tutorial: Onboarding](https://blogs.sap.com/2019/11/25/using-job-scheduler-in-sap-cloud-platform-0-intro-and-prep/)

### SAP Community

- [SAP Community Blog Posts](https://community.sap.com/search/?ct=blog&q=SAP%20Job%20Scheduling%20service)
- [SAP Community Questions and Answers](https://community.sap.com/search/?ct=qa&q=SAP%20Job%20Scheduling%20service)

### Support

- [Support](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/5dd739823b824b539eee47b7860a00be.html)

## Sample configuration of **SAP Job Scheduling service** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **jobscheduler** by configuring your `usecase.json` file.

### Using the service plan **standard**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "SERVICE",
      "name": "jobscheduler",
      "plan": "standard"
    }
  ]
}
```
