class FuzzyDict(dict):
    def __init__(self, threshold):
        self.threshold = float(threshold)
    def __getitem__(self, key):
        if self.has_key(key):
            ret = [key]
        chars = int(len(key) * self.threshold)
        keys = [x for x in self.keys() if len(x) == len(key) and x != key]
        for k in keys:
            match = 0
            for i in range(0, len(key), 1):
                if key[i] == k[i]:
                    match += 1
            if chars <= match and self.has_key(k):
                ret.append(k)
        return ret

