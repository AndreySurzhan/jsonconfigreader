## Description

Utility that allows to read and parse json config files.

Possible to specify links to the default values in the config (See Usage section).

## Installation

1. Install python 3.6+
2. Ensure pip, setuptools, and wheel are installed and up to date
   
`python -m pip install --upgrade pip setuptools wheel`
 
3. Create virtual enviroment (make sure that is not part of the project)

`python -m venv <ENV NAME>`

or 

`python -m venv %path%\to\<ENV NAME>`

4. Active virtual enviroment

`%path%\to\<ENV NAME>\Script\activate`

5. Install all project dependencies if needed

`pip install -r requirements.txt`

6. Install pandoc and pypandoc. [Instruction](https://pypi.python.org/pypi/pypandoc)

`pip install pypandoc`

## Usage

Example of the config file:

```
C:\User\test\qa_hotfix_config.json

{
    "defaults": {
        "dataBaseUrl": "http://db:5000"
    },
    "dataBase1": "<defaults.dataBaseUrl>",
    "dataBase2": "<defaults.dataBaseUrl>"
}
```

1. Specify that lib in your project dependencies
2. Import `from jsonconfigparser.json_config_reader import JsonConfigReader`
3. Create an instance of the class passing config folder path and options

```
config_path = 'C:\User\test\qa_config.json'
json_config_reader = JsonConfigReader(config_path)
config = json_config_reader.get()
file_path = json_config_reader.get_config_file_path()
print(config['dataBase1'])
print(file_path)

>> http://db:5000
>> C:\User\test\qa_config.json
```

## Uploading project to PyPi

1. Change version in `setup.py`
2. Upload changes to PyPi server

`python setup.py sdist upload -r <Repository URL to the PyPi server>`


## Run unit tests (Example for Visual Studio)

1. From Visual Studio
   1. Click `Test` -> `Run` -> `All Test`
   2. View Test run in `Test Explorer`
2. From CLI
   1. Navigate into project directory 
   2. `python -m unittest`

## Generate docs and updating docs

1. Run `easy_install -U sphinx`
2. Navigate to `docs` folder
3. Run `sphinx-quickstart`
4. [Follow instruction](https://daler.github.io/sphinxdoc-test/includeme.html)

