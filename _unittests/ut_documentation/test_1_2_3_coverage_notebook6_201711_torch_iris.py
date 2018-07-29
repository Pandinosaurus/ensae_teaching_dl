# -*- coding: utf-8 -*-
"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


import src.ensae_teaching_dl


class TestNotebook1236Coverage201711torch_iris(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_torch_iris(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(src.ensae_teaching_dl is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "101")
        test_notebook_execution_coverage(__file__, "Perceptron_Iris", folder,
                                         this_module_name="ensae_teaching_dl", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
