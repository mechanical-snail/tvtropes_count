#!/usr/bin/env python3
# This script is released under the GNU General Public License version 2 or later.

'''Calculates the number of trope entries of a work according to its page on TV Tropes (http://tvtropes.org/).

Notes:
* TV Tropes does not standardize their article format or use machine-readable semantic markup, so it is impossible to do this accurately. We assume that there is a single <ul> of tropes following an <h2>, and that top-level bullet points in that list = tropes.
* Works by parsing the rendered HTML, rather than the source. This is because TV Tropes's source functionality is currently broken.
'''
import sys
from lxml import etree

def count_tropes(article_name):
	slug = ''.join(c for c in article_name if c.isalnum() or c == '/')
	url = 'http://tvtropes.org/pmwiki/pmwiki.php/' + slug
	doc = etree.parse(url, etree.HTMLParser())
	[articlebody] = doc.xpath('''//*[@id='wikitext']''')
	
	# The usual format is this order: <h2>, empty <p>, the <ul> of tropes, empty <p>, <hr>.
	[h2] = articlebody.xpath('h2')
	assert h2.getnext().tag == 'p'
	tropelist = h2.getnext().getnext()
	assert tropelist.tag == 'ul'
	assert tropelist.getnext().tag == 'p'
	assert tropelist.getnext().getnext().tag == 'hr'
	assert all(elem.tag == 'li' for elem in tropelist.getchildren())
	return len(tropelist.getchildren())

if __name__ == '__main__':
	print('{0} tropes'.format(count_tropes(sys.argv[1])))