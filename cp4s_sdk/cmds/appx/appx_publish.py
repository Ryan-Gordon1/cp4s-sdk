#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from resilient import ensure_unicode
# Resilient SDK imports to reuse code and achieve a consistency across the SDKs
from resilient_sdk.cmds.base_cmd import BaseCmd
from resilient_sdk.cmds.codegen import CmdCodegen
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util.sdk_exception import SDKException

LOG = logging.getLogger(__name__)
DEFAULT_CONNECTOR = "CAR"


class AppXPublishCmd(BaseCmd):
    """
    AppXPublishCmd - A command that allows a customer to 'publish' a content package to the appx
    It's important to note that publish here really means submit and any submission to the appx will
    require a final review by stakeholders.

    This command shows how we can provide a functionality similar to
    Ansible Galaxy but for AppX

    Maybe we could even integrate some form of galaxy like Ansible section.
    """

    CMD_NAME = "publish"
    CMD_HELP = "Attempt to publish a package to the App Exchange. The publish process will either start a new App Submission or begin an Update of an App Submission"
    CMD_USAGE = """
    $ cp4s-sdk appx publish
    $ cp4s-sdk appx publish -p <package_name>
    """
    CMD_ADD_PARSERS = ["io_parser"]

    def setup(self):
        # Define codegen usage and description
        self.parser.usage = self.CMD_USAGE
        self.parser.description = self.CMD_DESCRIPTION

        # Add any positional or optional arguments here
        self.parser.add_argument("-p", "--package",
                                 type=ensure_unicode,
                                 help="(required) Name of new or path to existing package")

    def execute_command(self, args):
        LOG.debug("called: AppXPublishCmd.execute_command()")
        if args.package:
            SDKException.command_ran = "{0} {1}".format(
                self.CMD_NAME, "--package | -p")
            LOG.info("%s" %
                     ("Starting to publish a package to the AppX"))

            ###
            # Perform checks
            ###
            if os.path.exists(args.package):
                raise SDKException(
                    u"'{0}' already exists. Add --reload flag to regenerate it".format(args.package))

            if not sdk_helpers.is_valid_package_name(args.package):
                raise SDKException(
                    u"'{0}' is not a valid package name".format(args.package))

            ###
            # Attempt to upload to the AppX
            ###
            LOG.info("%s %s" %
                     ("AppX Publish run finished for ", args.package))
        else:
            self.parser.print_help()
