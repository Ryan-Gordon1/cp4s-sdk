# cp4s-sdk
![logo](/assets/IBM_Security.png)
A Software Development Kit (SDK), command line tools (CLI) and helper modules all under one roof to streamline the developer ecosystem of Cloud Pak for Security

## Overview
The Cloud Pak for Security Software Development Kit (cp4s-sdk) is a suite of tools across the entire ecosystem of Cloud Pak for Security (cp4s) and intends to provide
a one-stop-shop for those who want to develop apps, integrations or other tools to work with cp4s. 

This SDK is designed such that each product has its own section where it may expose its own commands. 
## Installation 

### Get from Pypi : 
The package is currently available on the test Pypi in order to preserve the namespace for IBM on the main Pypi repo
To install this from the test Pypi :
```bash
pip install -i https://test.pypi.org/simple/cp4s-sdk
```
This SDK depends on other packages such as the resilient-sdk and cp4s-connector-sdk packages. If you encounter issues with these during installation, try to download them individually using Pypi.
```bash
pip install resilient resilient-sdk cp4s-connector-sdk
```


### Install locally
+ `git clone <url>`
+ `cd cp4s-sdk`
+ `python setup.py install` 

The above will install the SDK but if you want to make changes to the SDK and see those changes on next run rather than needing to reinstall the package use the develop flag:
`python setup.py develop` 

Below is an overview on how we can achieve the use case of having one thing to install which unlocks the entire ecosystem.
![install](/assets/install-flow.png)

#### Usage Examples:

##### Available Product SDKs 
```
$ cp4s-sdk -h
usage: cp4s-sdk [-h] {soar,connector,qradar,appx} ...

The Cloud Pak for Security (CP4S) SDK provides a gateway to developer focused
tools and functionalities for each of the products under the Ecosystem. The
cp4s-sdk provides a streamlined interface to all of the packages maintained by
each of the product teams in the Cloud Pak. Run cp4s-sdk -h to see the
commands And to see the command for each product try $cp4s-sdk soar -h or
$cp4s-sdk qradar -h

Available product SDKs:
  {soar,connector,qradar,appx}
    soar                Commands for developing Cases Apps
    connector           Commands for developing CAR or UDI Connectors
    qradar              Commands for developing QRadar Apps
    appx                Commands for working with the App Exchange

optional arguments:
  -h, --help            show this help message and exit
```
Below is a diagram showing how the CP4S SDK delegates to th appropriate SDK
![usage](/assets/usage-flow.png)

#### CLI Examples
##### SOAR
```bash
cp4s-sdk soar codegen -p package_name-m message_destination
```

```bash
cp4s-sdk soar clone -w workflow_name cloned_workflow_name
```
##### Connectors (CAR, UDI)
```bash
cp4s-sdk connector codegen -p my_new_connector
```

```bash
cp4s-sdk connector codegen -p my_new_connector --connectortype UDI
```

##### (Preview) QRadar App SDK
```bash
cp4s-sdk qradar create -p my_new_app
```

##### (Preview) App Exchange
```bash
cp4s-sdk appx publish -p /path/to/assets/
```

### Goals


- [:heavy_check_mark:]Implement a basic structure that is extensible for others  
- [:heavy_check_mark:]Begin working on integrating the resilient-sdk; the first citizen of this project  
- [:heavy_check_mark:]Work on implementing QRadar App SDK (No way to programmatically download SDK; Workaround with a POC of just one command)  
- [:heavy_check_mark:]Integrate the Connector SDK  
- []CI/CD system  
