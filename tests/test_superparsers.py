
from cp4s_sdk.subparsers.i_subparser import ISubParser
from cp4s_sdk.subparsers.soar_subparser import SoarSubParser
from argparse import ArgumentParser, HelpFormatter
import argparse

import pytest

class TestSubParserInterface():
    def test_interface_with_impl_methods(self):
        class MyParser(ISubParser):
            def register_subparser(self, *args, **kwargs):
                pass

            def is_registered(self, *args, **kwargs):
                pass

            def handle_command_invocation(self, product_args):
                pass

        parser = MyParser()
        assert not parser.is_registered()

    def test_interface_without_std_methods(self):
        class MyParser(ISubParser):
            def handle_register_subparser(self, *args, **kwargs):
                pass

            def doa_command_invocation(self, product_args):
                pass
        with pytest.raises(NotImplementedError):
            parser = MyParser()
            assert not parser.is_registered()

class TestSoarSubparser():

    def test_soar_product_name(self):
        p = SoarSubParser()
        assert p.product == "soar"

    def test_initial_status(self):
        p = SoarSubParser()
        assert not p.is_registered()
    
    def test_registration_status(self):
        app = argparse.ArgumentParser(description="MOCKED CLI")
        # Add the top level parser; this will be purely navigational
        root_sp = app.add_subparsers(dest='product')
        p = SoarSubParser()
        p.register_subparser(parent_parser=root_sp)
        assert p.is_registered()

    def test_registration_without_parent(self):
        app = argparse.ArgumentParser(description="MOCKED CLI")
        # Add the top level parser; this will be purely navigational
        root_sp = app.add_subparsers(dest='product')
        p = SoarSubParser()
        with pytest.raises(ValueError):
            p.register_subparser()

        with pytest.raises(ValueError):
            p.register_subparser(parent_parser=None)
        
