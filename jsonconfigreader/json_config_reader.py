import json
import os
import logging

import logging


class JsonConfigReader(object):

    def __init__(self, config_path, options=None):
        """Class constructor.

        Args:
            config_path (str): configuration folder wihtout trailling '\' or file absolute path with *.json extension.
            options (?dict): Options that contain information about environment and config file patther.
            options['env'] (dict): Environment description. Example: '{'name': 'qa', 'branch': 'hotfix'}' or {'name': stg} etc.
            options['file_pattern'] (str): File pattern option. Should match Environment keys. Example: '{env[name]}_{env[branch]}_config' or '{evn[name]}Config' etc.
        Returns:
            Void

        """
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.config_path = config_path
        self.options = options   
        self.config_file_path = self.get_config_file_path()      
        config = self.read_json_file(self.config_file_path)
        self.config = self._parse_config(config)

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

    def get_value_by_property_address(self, property_address, dictionary):
        """Class method that returns value from the dict based on the address string.

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

    def get_config_file_path(self):
        """Class method that returns full config file path.

        Returns:
            srt: full config file path

        """
        if self.options is None or type(self.options) is not dict:
            return self.config_path
        file_pattern = self.options['file_pattern']
        file_name = file_pattern.format(env=self.options['env'])
        file_name = file_name + '.json'
        return os.path.join(self.config_path, file_name)

    def is_default_value(self, string_value):
        """Class method that figures out whether string is custom default variable in config.

        Args:
            string_value (str): Specificly formatted string. Example: '<defaults.dataBase>'

        Returns:
            bool: True if it is default variable, False otherwise 

        """
        return type(string_value) is str and '<' in string_value and '>' in string_value

    def get(self):
        """Class method that returns parsed config content in dict format.

        Returns:
            dict: Configuration file content

        """
        return self.config

    def _parse_config(self, config, original_config=None):
        """Class method parse config file, replace default variables with appropriate values and return condig.

        Args:
            config (dict): Config file content.
            original_config (dict, optional): Optional parameter that represents original config file content

        Returns:
            dict: Configuration file content

        """
        keys_list = config.keys()
        for key in keys_list:
            value = config[key]
            if self.is_default_value(value):
                original_config = config if None else original_config
                address = self._get_default_address(value)
                config[key] = self.get_value_by_property_address(address, original_config)
                continue
            if type(value) is dict:
                self._parse_config(value, config)
                continue
            if type(value) is list:
                for element in value:
                    self._parse_config(element, config)
        return config

    def _get_default_address(self, address):
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
