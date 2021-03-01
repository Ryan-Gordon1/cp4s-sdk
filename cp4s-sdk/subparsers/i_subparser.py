# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.

""" a generic interface which subparsers inherit from
Interfaces are not needed in python; all this ensures is that
each implementation of a subparser exposes the minimum set of
methods that the rest of the application expects to be available.
"""
import sys
import abc

# There is a difference between have abstract base classes are handled in py 2 and 3
# In python 3 we can directly access abc.ABC and inherit from that
# In python 2 we must create the ABC class using abc.ABCMeta
if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta


class ISubParser(ABC):

    def register_subparser(self, *args, **kwargs):
        raise NotImplementedError

    def is_registered(self, *args, **kwargs):
        raise NotImplementedError

    def handle_command_invocation(self, product_args):
        raise NotImplementedError
