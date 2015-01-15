#!/usr/bin/env python
import xmostest
import argparse

import helpers

if __name__ == "__main__":
    global trace
    argparser = argparse.ArgumentParser(description="XMOS lib_ethernet tests")
    argparser.add_argument('--trace', action='store_true', help='Run tests with simulator and VCD traces')
    helpers.args = xmostest.init(argparser)

    xmostest.register_group("lib_ethernet",
                            "basic_tests",
                            "Ethernet basic tests",
    """
Tests are performed by running the ethernet library connected to a
simulator model (written as a python plugin to xsim). Basic functioanlity is tested such as basic sending and receiving of packets, rejection of bad packets, interframe gap testing.
""")

    xmostest.build('test_rx')

    xmostest.runtests()

    xmostest.finish()
