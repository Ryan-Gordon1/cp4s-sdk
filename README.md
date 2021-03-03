# cp4s-sdk

A Software Development Kit (SDK), command line tools (CLI) and helper modules all under one roof to streamline the developer ecosystem of Cloud Pak for Security

## Overview
The Cloud Pak for Security Software Development Kit (cp4s-sdk) is a suite of tools across the entire ecosystem of Cloud Pak for Security (cp4s) and intends to provide
a one-stop-shop for those who want to develop apps, integrations or other tools to work with cp4s. 

This SDK is designed such that each product has its own section where it may expose its own commands. 

## Quickstart 

### Installation
#### Get it from Pypi:

#### Install locally: 

#### Usage Examples:
```bash
cp4s-sdk cases codegen <-p package_name> <-m message_destination>
```

```bash
cp4s-sdk cases clone <-w workflow_name cloned_workflow_name> 
```

### Goals
+ Implement a basic structure that is extensible for others
+ Begin working on integrating the resilient-sdk; the first citizen of this project
+ Work on implementing QRadar App SDK (Blocked: No way to programatically download SDK)
+ CI/CD system 
