import unittest
from unittest.mock import MagicMock

class MockCallsTest(unittest.TestCase):
    def test_mock_called(self):
        mock = MagicMock()
        mock()
        mock.assert_called()
    
    def test_mock_not_called(self):
        mock1 = MagicMock()
        mock1.assert_not_called()

    def test_called_with(self):
        mock2 = MagicMock()
        mock2("Nonesense")
        mock2.assert_called_with("Nonesense")

    def test_called_ammount(self):
        mock3 = MagicMock()
        mock3(1, 2)
        mock3()
        print(mock3.mock_calls)
        


if __name__ == "__main__":
    unittest.main()