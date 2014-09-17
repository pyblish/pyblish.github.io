"""Full hello world example

1. Select data from memory
2. Validate data
3. Extract data to other part of memory
4. Conform data into plain-text

"""

import pyblish.backend.plugin


data = {'message': 'Helo World'}


class SelectData(pyblish.backend.plugin.Selector):
    hosts = ['python']

    def process_context(self, context):
        pass


class ValidateData(pyblish.backend.plugin.Validator):
    hosts = ['python']
    families = ['*']

    def process_instance(self, instance):
        pass


class ExtractData(pyblish.backend.plugin.Extractor):
    hosts = ['python']
    families = ['*']

    def process_instance(self, instance):
        pass


class ConformData(pyblish.backend.plugin.Conformer):
    hosts = ['python']
    families = ['*']

    def process_instance(self, instance):
        pass


if __name__ == '__main__':
    context = pyblish.backend.plugin.Context()

    for plugin in (SelectData, ValidateData, ExtractData, ConformData):
        for instance, error in plugin().process(context):
            if error is not None:
                print error, instance
                return
