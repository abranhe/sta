import sys

class sta(object):
    def __call__(self, str):
        arr = []
        words = str.strip().split(' ')

        for word in words:
            arr.append(word)
        return arr

sys.modules[__name__] = sta()
