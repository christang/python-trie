import locale
import random
import string
import time
from guppy import hpy
from trie import DictTrie, ListTrie

hp = hpy()
magnitudes = [2**i for i in range(1, 20)]
locale.setlocale(locale.LC_ALL, 'en_US')

def random_string(choices, length):
    return ''.join(random.choice(string.ascii_lowercase[:choices]) for _ in range(length))

def print_stats(i, t0, hp, heap=False):
    td = time.clock() - t0
    size = locale.format('%d', hp.heap().size, grouping=True) if heap else 'skipped'
    print "{0:>7}   {1:2.4f} {2:>12}".format(i, td, size)

def load_trie(n, width, length, verbose=False):
    print "\nn=%d w=%d, l=%d" % (n, width, length)
    dct = {}
    data = list((_, random_string(width, length)) for _ in range(n))

    print "DictTrie(n, t_cpu, mem)"
    hp.setrelheap()
    t0 = time.clock()
    for i, s in data:
        DictTrie.incr_dict(dct, s)
        if i in magnitudes:
            print_stats(i, t0, hp, verbose)
    print_stats(i, t0, hp, True)
    dct = None

    lst = []
    print "ListTrie(n, t_cpu, mem)"
    hp.setrelheap()
    t0 = time.clock()
    for i, s in data:
        ListTrie.incr_trie(lst, s)
        if i in magnitudes:
            print_stats(i, t0, hp)
    print_stats(i, t0, hp, True)
    lst = None

load_trie(10000, 25, 20)
load_trie(10000,  2, 20)
load_trie(10000,  5, 100)
