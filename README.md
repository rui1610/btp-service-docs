# btp-service-docs

This repository provides examples on how to make use of the [btp-service-metadata](https://github.com/SAP-samples/btp-service-metadata) repository.

This repository runs on a daily basis via a defined [Github action](.github/workflows/get-btp-service-metadata.yml). It crawls through the service metadata it fetches from the [btp-service-metadata](https://github.com/SAP-samples/btp-service-metadata) repository and transforms it into markdown files stored in the [docs](docs/) folder.
