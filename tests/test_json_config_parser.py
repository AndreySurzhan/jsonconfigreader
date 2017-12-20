import unittest
import os

from jsonconfigparser.json_config_parser import JsonConfigParser


class Test_test_json_config_parser(unittest.TestCase):

    def setUp(self):
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        self.file_name = 'qa_hotfix_config.json'
        self.congif_folder_path = os.path.join(self.project_path, 'data')
        self.congif_file_path = os.path.join(self.congif_folder_path, self.file_name)
        self.json_config_parser = JsonConfigParser(self.congif_folder_path, 
                                                   options={'env': {'name': 'qa', 'branch': 'hotfix'},
                                                            'file_pattern': '{env[name]}_{env[branch]}_config'})

    def test_get_config_file_path(self):
        expected_config_file_path = self.congif_file_path
        actual_config_file_path = self.json_config_parser.get_config_file_path()
        self.assertEqual(actual_config_file_path, expected_config_file_path)

    def test_is_default_value(self):
        default_value = '<test.test1.test2>'
        self.assertTrue(self.json_config_parser.is_default_value(default_value))

    def test_is_not_default_value(self):
        default_value = 'test.test1.test2'
        self.assertFalse(self.json_config_parser.is_default_value(default_value))

    def test_read_config_file(self):
        config = self.json_config_parser.read_json_file(self.congif_file_path)
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['defaults']['databaseConnection'], 'local_connection')

    def test_get_value_by_property_address(self):
        expected_value = 'local_connection'
        config = {
            'test': 1,
            'defaults': {'databaseConnection' : 'local_connection'}
            }
        actual_value = self.json_config_parser.get_value_by_property_address('defaults.databaseConnection', config)
        self.assertEqual(actual_value, expected_value)

    def test_get_parsed_config(self):
        config = self.json_config_parser.get()
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['databaseConnections']['local'], 'local_connection')
        self.assertEqual(config['databaseConnections']['app'], 'app_connection')
        self.assertEqual(config['branches']['hotfix']['databaseOverrides']['local'], 'local_hotfix')

    def test_get_parsed_config_by_full_file_path(self):
        config = JsonConfigParser(self.congif_file_path).get()
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['databaseConnections']['local'], 'local_connection')
        self.assertEqual(config['databaseConnections']['app'], 'app_connection')
        self.assertEqual(config['branches']['hotfix']['databaseOverrides']['local'], 'local_hotfix')

if __name__ == '__main__':
    unittest.main()
