from collections import OrderedDict


class DictFlattener:
    """ A 'disposable' class that uses output attribute to hold data
    during recursion.
    """

    def __init__(self, ordered=False):
        self._output = OrderedDict() if ordered else {}

    def flatten(self, data, json_path='$'):
        """ Flatten the JSON input by adding recursively into the output dictionary.
        """
        if type(data) in [str, int, float, bool] or data is None:
            self._output[json_path] = data

        elif isinstance(data, dict):
            if not data:  # Empty dictionary
                self._output[json_path] = {}
            else:
                for key in data:
                    self.flatten(data[key], '%s.%s' % (json_path, str(key)))

        elif type(data) == list:
            if not data:  # Empty list
                self._output[json_path] = []
            else:
                for index in range(len(data)):
                    self.flatten(data[index], '%s[%d]' % (json_path, index))

    def return_output(self):
        """ Clean the output attribute and return result.
        """
        temp = self._output
        self._output = {}
        return temp
