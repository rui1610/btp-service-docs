import os
import shutil
from pathlib import Path
from utils import renderTemplateWithJson
from constants import FOLDER_OUTPUT_DOCS, TEMPLATE_DEVELOPERS_MD, CATEGORIES
from re import sub
from copy import deepcopy


def createDocsForServiceDetails(services):

    # remove complete folder if it already exists
    if os.path.exists(FOLDER_OUTPUT_DOCS):
        shutil.rmtree(FOLDER_OUTPUT_DOCS)

    serviceList = convertToServiceListByCategory(services)

    # Create a detailed page for each service
    for category in serviceList:
        for service in category.get("list"):
            markdownName = normalize_id(service.get("name")) + ".md"
            targetFile = Path(FOLDER_OUTPUT_DOCS, markdownName).resolve()
            templateFile = Path(TEMPLATE_DEVELOPERS_MD).resolve()
            renderTemplateWithJson(templateFile, targetFile, {"service": service, "category": category, "plansInRegions": getSupportedPlansInRegions(service)})


def normalize_id(id: str) -> str:
    return sub(r"[\s-]+", "-", id.lower())


def getSupportedPlansInRegions(service):
    allSupportedRegions = []
    for plan in service.get("servicePlans"):
        for dataCenter in plan.get("dataCenters"):
            region = dataCenter.get("region")
            if region not in allSupportedRegions:
                allSupportedRegions.append(region)
    allSupportedRegions.sort()
    result = []
    for supportedRegion in allSupportedRegions:
        thisResult = {"region": supportedRegion, "plans": []}

        for plan in service.get("servicePlans"):
            for dataCenter in plan.get("dataCenters"):
                region = dataCenter.get("region")
                if region == supportedRegion:
                    thisResult["plans"].append(plan)
        result.append(thisResult)

    return result


def convertToServiceListByCategory(rawData):

    result = []
    for category in CATEGORIES:
        list = {"name": category, "list": getBtpCategory(category, rawData)}
        result.append(list)

    return result


def getBtpCategory(category, rawData):

    services = None

    if category in CATEGORIES["SERVICE"]:
        services = getServicesForCategory("SERVICE", rawData)
    if category in CATEGORIES["APPLICATION"]:
        services = getServicesForCategory("APPLICATION", rawData)
    if category in CATEGORIES["ENVIRONMENT"]:
        services = getServicesForCategory("ENVIRONMENT", rawData)
    if services is None:
        print("ERROR: the category >" + category +
              "< can't be assigned to one of the defined service categories")

    return services


def getServicesForCategory(category, rawData):
    result = []

    for service in rawData:
        servicePlans = getServicePlansForCategory(service, category)
        thisService = None
        if servicePlans:
            thisService = deepcopy(service)
            thisService["servicePlans"] = servicePlans
            result.append(thisService)
    sortedResult = sorted(result, key=lambda d: (d['name'].lower()), reverse=False)

    return sortedResult


def getServicePlansForCategory(service, category):
    result = []

    for plan in service.get("servicePlans"):
        thisCategory = plan.get("category")
        if thisCategory in CATEGORIES.get(category):
            alreadyExistsInResult = False
            for temp in result:
                if temp.get("name") == plan.get("name"):
                    alreadyExistsInResult = True
            if not alreadyExistsInResult:
                # result.append(getBtpServicePlan(plan))
                result.append(plan)

    return result
