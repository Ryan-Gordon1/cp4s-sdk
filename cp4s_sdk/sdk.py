# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.

""" entrypoint for cp4s-sdk Python Module """

# Python std lib deps
from cp4s_sdk.subparsers.soar_subparser import SoarSubParser
from cp4s_sdk.subparsers.connector_subparser import ConnectorSubParser
from cp4s_sdk.subparsers.appx_subparser import AppExchangeSubParser
from cp4s_sdk.subparsers.qradar_subparser import QRadarSubParser

import argparse

DESCRIPTION = """The Cloud Pak for Security (CP4S) SDK
provides a gateway to developer focused tools and functionalities for
each of the products under the Ecosystem.
The cp4s-sdk provides a streamlined interface to all
of the packages maintained by each of the product teams in
the Cloud Pak.

Run cp4s-sdk -h to see the commands
And to see the command for each product try
\n
$cp4s-sdk cases -h
\n
or
\n
$cp4s-sdk qradar -h
"""


def main():
    app = argparse.ArgumentParser(description=DESCRIPTION)
    # Add the top level parser; this will be purely navigational
    root_sp = app.add_subparsers(dest='product')
    app._positionals.title = 'Available product SDKs, tools and Command Line Interfaces'

    # Add the cases parser
    cases_subparser = SoarSubParser()
    cases_subparser.register_subparser(parent_parser=root_sp)
    connector_subparser = ConnectorSubParser()
    connector_subparser.register_subparser(parent_parser=root_sp)
    qradar_subparser = QRadarSubParser()
    qradar_subparser.register_subparser(parent_parser=root_sp)
    appx_subparser = AppExchangeSubParser()
    appx_subparser.register_subparser(parent_parser=root_sp)

    # TODO: Exploring looping instantiation
    # products = [CasesSubParser]
    # parser_dict = dict()
    # for p in products:
    #     p.__init__()
    #     p.register_subparser(p, kwargs={"parent_parser": root_sp})
    #     parser_dict.update({p.product: p})

    # After handling all the instantiation and setup. Parse the args so we can delagate the workload to the right product
    args = app.parse_args()

    # To minimize on code needed in this entrypoint
    # each product is defined as a class with common methods we can depend on here
    if args.product == 'soar':
        cases_subparser.handle_command_invocation(product_args=args)
    elif args.product == 'connector':
        connector_subparser.handle_command_invocation(product_args=args)
    elif args.product == 'qradar':
        qradar_subparser.handle_command_invocation(product_args=args)
    elif args.product == 'appx':
        appx_subparser.handle_command_invocation(product_args=args)
    else:
        app.print_help()
