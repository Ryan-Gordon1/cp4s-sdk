# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.
from .i_subparser import ISubParser
from resilient_sdk.app import get_main_app_parser, get_main_app_sub_parser
from resilient_sdk.util.sdk_argparse import SDKArgHelpFormatter
from resilient_sdk.cmds import CmdDocgen, CmdCodegen, CmdClone, CmdExtract
import argparse

class CarSubParser(ISubParser):
    """CarSubParser is an ArgumentParser
    which delagates work to the Car Framework
    python module.
    When a user targets the 'car' product on the cp4s-sdk
    this CarSubParser handles it and invokes the appropriate car command.

    :param ISubParser: A generic type that represents the contract a subparser must uphold
    :type ISubParser: Interface
    """

    product = "car"
    registered = False

    def register_subparser(self, *args, **kwargs):
        if not kwargs.get("parent_parser", False):
            raise ValueError(
                "No Parent Parser was found in kwargs, this is needed to ensure we can attach the {} commands".format(self.product))

        parent = kwargs.get("parent_parser")
        # Top level product name
        car_parser = parent.add_parser(self.product, help="Commands for developing Cases Apps and Integrations",
                                        formatter_class=SDKArgHelpFormatter,
                                        conflict_handler='resolve')
        subparsers = car_parser.add_subparsers()
        parser = subparsers.add_parser('run', help='Run a CAR Connector',
                                          formatter_class=argparse.RawTextHelpFormatter)
        parser_codegen = subparsers.add_parser('codegen', help='Generate a CAR Connector based on the Reference Connector',
                                          formatter_class=argparse.RawTextHelpFormatter)


        parser.add_argument('-car-service-url', dest='car_service_apikey_url', type=str, required=False, help='URL of the CAR ingestion service if API key is used for authorization')
        parser.add_argument('-car-service-key', dest='api_key', type=str, required=False, help='API key for CAR ingestion service')
        parser.add_argument('-car-service-password', dest='api_password', type=str, required=False, help='Password for CAR ingestion service')

        parser.add_argument('-car-service-url-for-token', dest='car_service_token_url', type=str, required=False, help='URL of the CAR ingestion service if Auth token is used for authorization')
        parser.add_argument('-car-service-token', dest='api_token', type=str, required=False, help='Auth token for CAR ingestion service')

        # source id to uniquely identify each data source
        parser.add_argument('-source', dest='source', type=str, required=True, help='Unique source id for the data source')

        parser.add_argument('-d', dest='debug', action='store_true', help='Enables DEBUG level logging')


        return parser

    def is_registered(self, *args, **kwargs):
        return self.registered

    def handle_command_invocation(self, product_args):
        # Evaluate the cmd and link to a piece of functionality
        # Handle what subcommand was called
        pass
