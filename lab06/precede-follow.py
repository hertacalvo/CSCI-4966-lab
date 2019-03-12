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
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i + 1:]
            j = lookup[c]  # lowercase.index(c)
            for cc in lowercase[j + 1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
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
    G = words_graph(4)

    word_list = ['slid','dote','herd','omen','nine','sell','stat','what']

    for word in word_list:
        if word in G:
            print("Neighbors to {} are:".format(word))
            try:
                neighbors = nx.neighbors(G, word)
                for n in neighbors:
                    print(n)
            except nx.NetworkXNoPath:
                print("None")
        else:
            print("Word: '{}' not in graph".format(word))
