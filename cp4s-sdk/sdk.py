# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.

""" entrypoint for cp4s-sdk Python Module """

# Python std lib deps
from subparsers.soar_subparser import SoarSubParser
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
# Add the top level parser; this will be purely navigational
root_sp = app.add_subparsers(dest='product')

# Add the cases parser
cases_subparser = SoarSubParser()
cases_subparser.register_subparser(kwargs={
    "parent_parser": root_sp
})

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
else:
    app.print_help()
