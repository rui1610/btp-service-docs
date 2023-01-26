# categorymanagement-o2-s2 (SAP Category Management)

SAP Category Management provides the fundamental tools and data insights across all the phases of the development, execution, and monitoring of the category strategy with seamless integration to the source-to-pay processes.

## Service plan availability in regions

| Region | CategoryManagement | OpportunityAnalysis |
|--------|--------------------|---------------------|
|  **eu10** | ✅ | ✅ |

## Additional details
## Sample configuration of **SAP Category Management** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **categorymanagement-o2-s2** by configuring your `usecase.json` file.

### Using the service plan **CategoryManagement**

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "categorymanagement-o2-s2",
      "plan": "CategoryManagement"
    }
  ]
}
```

### Using the service plan **OpportunityAnalysis** (Opportunity Analysis)

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "APPLICATION",
      "name": "categorymanagement-o2-s2",
      "plan": "OpportunityAnalysis"
    }
  ]
}
```
