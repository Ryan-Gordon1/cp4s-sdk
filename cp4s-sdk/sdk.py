# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.

""" entrypoint for cp4s-sdk Python Module """

# Python std lib deps
from argparse import ArgumentParser, HelpFormatter
import argparse

DESCRIPTION = """The Cloud Pak for Security (CP4S) SDK 
provides a gateway to developer focused tools and functionalities for
each of the products under the Ecosystem.

The cp4s-sdk provides a streamlined interface to all
of the packages maintained by each of the product teams in
the Cloud Pak.

Run cp4s-sdk -h to see the commands
And to see the command for each product try

$cp4s-sdk cases -h
or
$cp4s-sdk qradar -h
"""

app = argparse.ArgumentParser(description=DESCRIPTION)
