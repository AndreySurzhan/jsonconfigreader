import unittest
import os

from jsonconfigreader.json_config_reader import JsonConfigReader


class TestJsonConfigParser(unittest.TestCase):

    def setUp(self):
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        self.file_name = '{}_hotfix_config.json'
        self.config_folder_path = os.path.join(self.project_path, 'data')
        self.qa_config_file_path = os.path.join(self.config_folder_path,
                                                self.file_name.format('qa'))
        self.dev_config_file_path = os.path.join(self.config_folder_path,
                                                self.file_name.format('dev'))
        self.json_config_reader = JsonConfigReader(self.qa_config_file_path)

    def test_get_config_file_path(self):
        expected_config_file_path = self.qa_config_file_path
        actual_config_file_path = self.json_config_reader.get_config_file_path()
        self.assertEqual(actual_config_file_path, expected_config_file_path)

    def test_is_default_value(self):
        default_value = '<test.test1.test2>'
        self.assertTrue(self.json_config_reader.is_default_value(default_value))

    def test_is_not_default_value(self):
        default_value = 'test.test1.test2'
        self.assertFalse(self.json_config_reader.is_default_value(default_value))

    def test_read_config_file(self):
        config = self.json_config_reader.read_json_file(self.qa_config_file_path)
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['defaults']['databaseConnection'], 'local_connection')

    def test_get_value_by_property_address(self):
        expected_value = 'local_connection'
        config = {
            'test': 1,
            'defaults': {'databaseConnection' : 'local_connection'}
            }
        actual_value = self.json_config_reader.get_value_by_property_address('defaults.databaseConnection', config)
        self.assertEqual(actual_value, expected_value)

    def test_get_parsed_config(self):
        config = self.json_config_reader.get()
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['databaseConnections']['local'], 'local_connection')
        self.assertEqual(config['databaseConnections']['app'], 'app_connection')
        self.assertEqual(config['branches']['hotfix']['databaseOverrides']['local'], 'local_hotfix')

    def test_get_parsed_config_by_full_file_path(self):
        config = JsonConfigReader(self.qa_config_file_path).get()
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['databaseConnections']['local'], 'local_connection')
        self.assertEqual(config['databaseConnections']['app'], 'app_connection')
        self.assertEqual(config['branches']['hotfix']['databaseOverrides']['local'], 'local_hotfix')

    def test_set_config_file_path(self):
        json_config_reader = JsonConfigReader(self.qa_config_file_path)
        json_config_reader.set_config_path(self.dev_config_file_path)
        new_path = json_config_reader.get_config_file_path()
        self.assertTrue(self.dev_config_file_path == new_path)
        config = json_config_reader.get()
        self.assertTrue(type(config) is dict)
        self.assertEqual(config['defaults']['baseUrl'], 'https:/devtest.com')
        self.assertEqual(config['databaseConnections']['app'], 'app_connection')
        self.assertEqual(config['branches']['hotfix']['databaseOverrides']['local'], 'local_hotfix')


if __name__ == '__main__':
    unittest.main()
