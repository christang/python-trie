import bisect
import collections
__all__ = ['DictTrie', 'ListTrie']

class DictTrie:

    def __init__(self):
        self._dct = {}

    def incr(self, keys):
        DictTrie.incr_dict(self._dct, keys)
        return self._dct

    @staticmethod
    def incr_dict(dct, keys):
        for key in keys[:-1]:
            if not key in dct:
                dct[key] = {}
            dct = dct[key]

        last = keys[-1]
        if last in dct:
            if isinstance(dct[last], int):
                dct[last] += 1
            else:
                dct[last][''] = dct[last].get('', 0) + 1
        else:
            dct[last] = 1


class ListTrie:

    def __init__(self):
        self._lst = []

    def incr(self, keys):
        ListTrie.incr_trie(self._lst, keys)
        return self._lst

    @staticmethod
    def incr_trie(lst, keys):

        def search(lst, key, on_found, on_not_found):
            i = bisect.bisect_left([t[0] for t in lst], key)
            if i != len(lst) and lst[i][0] == key: 
                return on_found(lst, i, key)
            else:
                return on_not_found(lst, i, key)

        key_value = lambda lst, i, key: lst[i]

        def new_key_list(lst, i, key):
            kv = (key, [])
            lst.insert(i, kv)
            return kv

        def new_key_value(lst, i, key):
            kv = (key, 1)
            lst.insert(i, kv)
            return kv

        def incr_key_value(lst, i, key):
            lst[i] = (lst[i][0], lst[i][1] + 1)

        def check_key_value(lst, i, key):
            if isinstance(lst[i][1], int):
                incr_key_value(lst, i, key)
            else:
                search(lst[i][1], '', incr_key_value, new_key_value)
                
        for key in keys[:-1]:
            kv = search(lst, key, key_value, new_key_list)
            lst = kv[1]

        last = keys[-1]
        search(lst, last, check_key_value, new_key_value)
