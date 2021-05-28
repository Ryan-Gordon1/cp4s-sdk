# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.
from .i_subparser import ISubParser
from resilient_sdk.app import get_main_app_sub_parser
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util.sdk_argparse import SDKArgHelpFormatter
from resilient_sdk.cmds import CmdDocgen, CmdCodegen, CmdClone, CmdExtract, CmdExtPackage, CmdDev


class SoarSubParser(ISubParser):
    """SoarSubParser is an ArgumentParser
    which delagates work to the resilient_sdk
    python module.
    When a user targets the 'soar' product on the cp4s-sdk
    this SoarSubParser handles it and invokes the appropriate sdk command.

    It is not intended to use this class programatically. Instead if you have use
    cases where you must interact with soar in such a way consider if you can get
    help from the helper functions in resilient_sdk.util.

    :param ISubParser: A generic type that represents the contract a subparser must uphold
    :type ISubParser: Interface
    """

    product = "soar"
    registered = False

    def register_subparser(self, *args, **kwargs):
        if not kwargs.get("parent_parser", False):
            raise ValueError(
                "No Parent Parser was found in kwargs, this is needed to ensure we can attach the {} commands".format(
                    self.product))

        parent = kwargs.get("parent_parser")

        # See if RES_SDK_DEV environment var is set
        self.sdk_dev = sdk_helpers.is_env_var_set(sdk_helpers.ENV_VAR_DEV)
        # Top level product name
        self.parser = parent.add_parser(self.product, help="Commands for developing Cases Apps and Integrations",
                                        formatter_class=SDKArgHelpFormatter,
                                        conflict_handler='resolve')

        # Get sub_parser object which will attach the available commands for the product SDK
        soar_sub_parser = get_main_app_sub_parser(self.parser)
        self.registered = True
        # By instantiating each command and passing the subparser we register each subcommand of the soar product
        self.cmd_codegen = CmdCodegen(soar_sub_parser)
        self.cmd_clone = CmdClone(soar_sub_parser)
        self.cmd_docgen = CmdDocgen(soar_sub_parser)
        self.cmd_extract = CmdExtract(soar_sub_parser)
        self.cmd_ext_package = CmdExtPackage(soar_sub_parser)
        self.cmd_dev = CmdDev(soar_sub_parser)
        return soar_sub_parser

    def is_registered(self, *args, **kwargs):
        return self.registered

    def handle_command_invocation(self, product_args):
        # Evaluate the cmd and link to a piece of functionality
        # Handle what subcommand was called
        if product_args.cmd == self.cmd_docgen.CMD_NAME:
            self.cmd_docgen.execute_command(product_args)

        elif product_args.cmd == self.cmd_codegen.CMD_NAME:
            self.cmd_codegen.execute_command(product_args)

        elif product_args.cmd == self.cmd_clone.CMD_NAME:
            self.cmd_clone.execute_command(product_args)

        elif product_args.cmd == self.cmd_extract.CMD_NAME:
            self.cmd_extract.execute_command(product_args)

        elif product_args.cmd == self.cmd_ext_package.CMD_NAME:
            self.cmd_ext_package.execute_command(product_args)

        elif self.sdk_dev and product_args.cmd == self.cmd_dev.CMD_NAME:
            self.cmd_dev.execute_command(product_args)
        else:
            self.parser.print_help()
