class FuzzyDict(dict):
    def __init__(self, threshold):
        self.threshold = float(threshold)
    def _get_fuzzy_elements(self, key):
        if self.has_key(key):
            ret_keys = [key]
            ret_values = [self[key]]
        else:
            ret_keys = []
            ret_values = []
        chars = int(len(key) * self.threshold)
        keys = [x for x in self.keys() if len(x) == len(key) and x != key]
        for k in keys:
            match = 0
            for i in range(0, len(key), 1):
                if key[i] == k[i]:
                    match += 1
            if chars <= match and self.has_key(k):
                ret_keys.append(k)
                ret_values.append(self[k])
        return ret_keys, ret_values
    def assign_dict(self, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                self[k] = v
    def fuzzy_keys(self, key):
        return self._get_fuzzy_elements(key)[0]
    def fuzzy_values(self, key):
        return self._get_fuzzy_elements(key)[1]
    def fuzzy_items(self, key):
        return self._get_fuzzy_elements(key)
    def fuzzy_assign(self, k, v):
        keys = self._get_fuzzy_elements(k)[0]
        for key in keys:
            self[key] = v
