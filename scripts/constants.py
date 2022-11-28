from pathlib import Path


ROOT = Path(__file__, "..", "..").resolve()
DATA_VERSION_V0 = "v0"
METADATA_REPO = Path(ROOT, "btp-service-metadata", DATA_VERSION_V0).resolve()
METADATA_REPO_DEVELOPERS = Path(METADATA_REPO, "developer").resolve()

FOLDER_TEMPLATES = Path(ROOT, "templates").resolve()

FOLDER_OUTPUT_DOCS = Path(ROOT, "service-docs").resolve()
TEMPLATE_DEVELOPERS_MD = Path(FOLDER_TEMPLATES, "SERVICE-DETAILS.MD").resolve()

# service categories
CATEGORIES = {}
CATEGORIES["SERVICE"] = ["SERVICE", "ELASTIC_SERVICE", "PLATFORM"]
CATEGORIES["APPLICATION"] = ["APPLICATION", "QUOTA_BASED_APPLICATION"]
CATEGORIES["ENVIRONMENT"] = ["ENVIRONMENT"]
