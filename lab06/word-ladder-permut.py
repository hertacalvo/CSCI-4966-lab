#!/usr/bin/env python

# Authors: Aric Hagberg (hagberg@lanl.gov),
#          Brendt Wohlberg,
#          hughdbrown@yahoo.com

#    Copyright (C) 2004-2018 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

# Modified by Herta Calvo-Faugier

from string import ascii_lowercase as lowercase
import sys
import networkx as nx
import itertools as it

#-------------------------------------------------------------------
#   The Words/Ladder graph of Section 1.1
#-------------------------------------------------------------------


def generate_graph(words):
    G = nx.Graph(name="words")
    lookup = dict((c, lowercase.index(c)) for c in lowercase)

    def edit_distance_one(word):
        perm = [ "".join(x) for x in it.permutations(word, len(word))]
        for w in perm:
            for i in range(len(w)):
                left, c, right = w[0:i], w[i], w[i + 1:]
                j = lookup[c]  # lowercase.index(c)
                for cc in lowercase[j + 1:]:
                    yield left + cc + right

    candgen = (\
        (word, cand) for word in sorted(words)
        for cand in edit_distance_one(word) if cand in words\
    )

    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G


def words_graph(n):
    """Return the words example graph from the Stanford GraphBase"""
    fh = open('words'+str(n)+'_dat.txt', 'r')
    words = set()
    for line in fh.readlines():
        if line.startswith('*'):
            continue
        w = str(line[0:n])
        words.add(w)
    return generate_graph(words)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: word-ladder-permut.py word-length")
    if sys.argv[1] not in ['4', '5']:
        syste.exit("ERROR: Program supports only 4 or 5 letter words")
    word_len = int(sys.argv[1])
    G = words_graph(word_len)
    print("Loaded words{}_dat.txt containing {} {}-letter English words."\
        .format(word_len, len(G), word_len))
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          % (nx.number_of_nodes(G), nx.number_of_edges(G)))
    print("%d connected components" % nx.number_connected_components(G))

    if word_len == 5:
        pair_list = [('chaos', 'order'),\
                    ('nodes', 'graph'),\
                    ('moron', 'smart'),\
                    ('pound', 'marks')]
    else:
        pair_list = [('cold', 'warm'),\
                    ('love', 'hate')]

    for (source, target) in pair_list:
        print("Shortest path between %s and %s is" % (source, target))
        try:
            sp = nx.shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
