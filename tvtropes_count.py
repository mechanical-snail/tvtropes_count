#!/usr/bin/env python3

'''Calculates the number of trope entries of a work according to its page on TV Tropes (http://tvtropes.org/).

Notes:
* TV Tropes does not use machine-readable semantic markup, so it is impossible to do this accurately. We assume that the last block is the list of tropes, and that top-level bullet points = tropes.
* Works by parsing the rendered HTML, rather than the source. This is because TV Tropes's source functionality is currently broken.
'''