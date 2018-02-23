import json
import os
import logging

import logging


class JsonConfigReader(object):

    def __init__(self, config_path):
        """Class constructor.

        Args:
            config_path (str): configuration file absolute path with *.json extension.
            
        Returns:
            void
        """
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._config_path = config_path

    def read_json_file(self, file_path):
        """Class method reads the data from json file and returs dictionary.

        Returns:
            dict: Config file content.

        Raises:
            IOError: If methods fails reading data from file exaption will be risen
        """
        config = None
        try:
            with open(file_path, 'r') as f:
                config = json.load(f)
        except IOError as e:
            self.logger.error('Cannot read config file "{}"'.format(file_path))
            self.logger.error(e.strerror)
        return config

    def get_config_file_path(self):
        """Class method that returns full config file path.

        Returns:
            srt: full config file path
        """
        return self._config_path

    def get(self):
        """Class method that returns parsed config content in dict format.

        Returns:
            dict: Configuration file content
        """
        config = self.read_json_file(self._config_path)
        return self._parse_config(config)

    def set_config_path(self, config_path):
        """Class method that sets config file path.

        Returns:
            dict: Configuration file content
        """
        self._config_path = config_path

    def _parse_config(self, config, original_config=None):
        """Class method parse config file, replace default variables with appropriate values and return condig.

        Args:
            config (dict): Config file content.
            original_config (dict): Optional parameter that represents original config file content

        Returns:
            void
        """
        keys_list = config.keys()
        for key in keys_list:
            value = config[key]
            if self.is_default_value(value):
                original_config = config if None else original_config
                address = self.get_default_address(value)
                config[key] = self.get_value_by_property_address(address, original_config)
                continue
            if type(value) is dict:
                self._parse_config(value, config)
                continue
            if type(value) is list:
                for element in value:
                    self._parse_config(element, config)
        return config

    @staticmethod
    def get_default_address(address):
        """Class method format default address variable string into regular property address string.

        Args:
            address (srt): default address variable string.

        Returns:
            srt: Regular property address string.

        Example:
            >> _get_default_address('<defaults.dataBase>')
            >> 'defaults.dataBase'
        """
        return address.replace('>', '').replace('<', '')

    @staticmethod
    def is_default_value(string_value):
        """Class static method that figures out whether string is custom default variable in config.

        Args:
            string_value (str): Specificly formatted string. Example: '<defaults.dataBase>'

        Returns:
            bool: True if it is default variable, False otherwise
        """
        return type(string_value) is str and '<' in string_value and '>' in string_value

    @staticmethod
    def get_value_by_property_address(property_address, dictionary):
        """Class static method that returns value from the dict based on the address string.

        Args:
            property_address (str): Address of the property in the config. Example: 'dataBase.connection'
            dictionary (dict): Configuration

        Returns:
            Could be bool, dict, srt, number, list etc.
        """
        list = property_address.split('.')
        value = dictionary
        for address in list:
            if type(value) is not dict:
                return value
            value = value[address]
        return value
