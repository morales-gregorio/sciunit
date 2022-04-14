import unittest

from sciunit.utils import TmpTestFolder

tmp_folder = TmpTestFolder()

class BaseCase(unittest.TestCase):
    """Unit tests for config files"""

    @classmethod
    def setUpClass(cls):
        tmp_folder.create()

    @classmethod
    def tearDownClass(cls):
        tmp_folder.delete()

    def test_deep_exclude(self):
        from sciunit.base import deep_exclude

        test_state = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
        test_exclude = [("a", "b"), ("c", "d")]
        deep_exclude(test_state, test_exclude)

    def test_default(self):
        # TODO
        pass

    def test_SciUnit(self):
        from sciunit.base import SciUnit

        sciunitObj = SciUnit()
        self.assertIsInstance(sciunitObj.properties(), dict)
        self.assertIsInstance(sciunitObj.__getstate__(), dict)
        self.assertIsInstance(sciunitObj.json(), str)
        sciunitObj.json(string=False)
        self.assertIsInstance(sciunitObj._class, dict)
        sciunitObj.testState = "testState"
        SciUnit.state_hide.append("testState")
        self.assertFalse("testState" in sciunitObj.__getstate__())

if __name__ == "__main__":
    unittest.main()
