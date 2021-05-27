#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from resilient import ensure_unicode
# Resilient SDK imports to reuse code and achieve a consistency across the SDKs
from resilient_sdk.cmds.base_cmd import BaseCmd
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util.sdk_exception import SDKException

LOG = logging.getLogger(__name__)
DEFAULT_CONNECTOR = "CAR"


class QRadarCreateCmd(BaseCmd):
    """
    TODO:
    Note this command may one day be removed once we can directly import the QRadar App SDK

    As a point of note, this design could be used as a template
    of how each of the QRadar App SDK'd commands can be broken into its
    own class to keep each source file leaner
    """

    CMD_NAME = "create"
    CMD_HELP = "Instantiate a new QRadar app workspace"
    CMD_USAGE = """
    $ cp4s-sdk qradar create -p <package_name>
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
        LOG.debug("called: QRadarCreateCmd.execute_command()")
        if args.package:
            SDKException.command_ran = "{0} {1}".format(
                self.CMD_NAME, "--package | -p")
            LOG.info("%s" %
                     ("Starting to create a package for QRadar"))

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
                     ("QRadarCreateCmd run finished for ", args.package))
        else:
            self.parser.print_help()
