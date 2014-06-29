import unittest
from trie import DictTrie, ListTrie


class DictTrieTest(unittest.TestCase):

    def setUp(self):
        self.dct = {}

    def test_incr_dict(self):
        DictTrie.incr_dict(self.dct, ('a', 'b', 'c'))
        self.assertEqual(self.dct, {'a': {'b': {'c': 1}}})

        # incrementing 'abc' and ('a', 'b', 'c') are equivalent
        DictTrie.incr_dict(self.dct, 'abc')
        self.assertEqual(self.dct, {'a': {'b': {'c': 2}}})

        DictTrie.incr_dict(self.dct, 'abf')
        self.assertEqual(self.dct, {'a': {'b': {'c': 2, 'f': 1}}})

        DictTrie.incr_dict(self.dct, 'arf')
        self.assertEqual(self.dct, {'a': {'r': {'f': 1}, 'b': {'c': 2, 'f': 1}}})

        DictTrie.incr_dict(self.dct, 'az')
        self.assertEqual(self.dct, {'a': {'r': {'f': 1}, 'b': {'c': 2,'f': 1}, 'z': 1}})

        DictTrie.incr_dict(self.dct, 'a')
        self.assertEqual(self.dct, {'a': {'': 1, 'r': {'f': 1}, 'b': {'c': 2,'f': 1}, 'z': 1}})


class ListTrieTest(unittest.TestCase):

    def setUp(self):
        self.lst = []

    def test_incr_trie(self):
        ListTrie.incr_trie(self.lst, ('a', 'b', 'c'))
        self.assertEqual(self.lst, [('a', [('b', [('c', 1)])])])

        # incrementing 'abc' and ('a', 'b', 'c') are equivalent
        ListTrie.incr_trie(self.lst, 'abc')
        self.assertEqual(self.lst, [('a', [('b', [('c', 2)])])])

        ListTrie.incr_trie(self.lst, 'abf')
        self.assertEqual(self.lst, [('a', [('b', [('c', 2), ('f', 1)])])])

        ListTrie.incr_trie(self.lst, 'arf')
        self.assertEqual(self.lst, [('a', [('b', [('c', 2), ('f', 1)]),('r', [('f', 1)])])])

        ListTrie.incr_trie(self.lst, 'az')
        self.assertEqual(self.lst, [('a', [('b', [('c', 2), ('f', 1)]),('r', [('f', 1)]), ('z', 1)])])

        ListTrie.incr_trie(self.lst, 'a')
        self.assertEqual(self.lst, [('a', [('', 1), ('b', [('c', 2), ('f', 1)]),('r', [('f', 1)]), ('z', 1)])])

if __name__ == '__main__':
    unittest.main()
