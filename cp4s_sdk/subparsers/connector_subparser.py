# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.
from .i_subparser import ISubParser
from resilient_sdk.app import get_main_app_sub_parser
from cp4s_connector_sdk.cmds.codegen_connector import ConnectorCodegenCmd
from argparse import HelpFormatter


class ConnectorSubParser(ISubParser):
    """ConnectorSubParser is an ArgumentParser
    which delagates work to the cp4s_connector_sdk
    python module.
    When a user targets the 'soar' product on the cp4s-sdk
    this ConnectorSubParser handles it and invokes the appropriate sdk command.

    It is not intended to use this class programatically. Instead if you have use
    cases where you must interact with soar in such a way consider if you can get
    help from the helper functions in resilient_sdk.util or cp4s_connector_sdk.

    :param ISubParser: A generic type that represents the contract a subparser must uphold
    :type ISubParser: Interface
    """

    product = "connector"
    registered = False

    def register_subparser(self, *args, **kwargs):
        if not kwargs.get("parent_parser", False):
            raise ValueError(
                "No Parent Parser was found in kwargs, this is needed to ensure we can attach the {} commands".format(
                    self.product))

        parent = kwargs.get("parent_parser")
        # Top level product name
        self.parser = parent.add_parser(self.product, help="Commands for developing CAR or UDI Connectors",
                                        formatter_class=HelpFormatter,
                                        conflict_handler='resolve')

        # Get sub_parser object which will attach the available commands for the product SDK
        soar_sub_parser = get_main_app_sub_parser(self.parser)
        self.registered = True
        # By instantiating each command and passing the subparser we register each subcommand of the soar product
        self.cmd_codegen = ConnectorCodegenCmd(soar_sub_parser)
        return soar_sub_parser

    def is_registered(self, *args, **kwargs):
        return self.registered

    def handle_command_invocation(self, product_args):
        # Evaluate the cmd and link to a piece of functionality
        # Handle what subcommand was called
        if product_args.cmd == self.cmd_codegen.CMD_NAME:
            self.cmd_codegen.execute_command(product_args)
        else:
            self.parser.print_help()
