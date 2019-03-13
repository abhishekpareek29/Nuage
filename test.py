import unittest
import nuage

class TestMergeYaml(unittest.TestCase):
    # Test if merge succesful.
    def test_main(self):
        path = './dir1/dir2/dir3/dir4/input.yaml'
        test_yaml = nuage.main(path)
        actual_yaml = {'size': 8, 'count': 2, 'wishlist': ['car', 'pony', 'worldpeace'], 'todo': {'dishes': {'priority': 'high'}, 'laundry': {'priority': 'low'}, 'vacuum': {'priority': 'very_very_high'}}, 'color': 'blue'}
        self.assertDictEqual(test_yaml, actual_yaml)

    def test_read_yaml(self):
        path = './dir1/dir2/dir3/dir4/input.yaml'
        test_yaml = nuage.read_yaml(path)
        read_actual_yaml = {'size': 8, 'count': 2, 'wishlist': ['car', 'pony'], 'todo': {'dishes': {'priority': 'high'}, 'laundry': {'priority': 'low'}}}
        self.assertDictEqual(test_yaml, read_actual_yaml)

if __name__ == '__main__':
    unittest.main()
