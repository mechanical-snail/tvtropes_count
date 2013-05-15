Calculates the number of trope entries of a work according to its page on [TV Tropes](http://tvtropes.org/).

# Notes
* TV Tropes does not standardize their article format or use machine-readable semantic markup, so it is impossible to do this accurately. We assume that there is a single `<ul>` of tropes following an `<h2>`, and that top-level bullet points in that list correspond to tropes.
* Works by parsing the rendered HTML, rather than the source. This is because TV Tropes's source functionality is currently broken.

# License
GPLv2+.