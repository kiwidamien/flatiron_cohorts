import re

prefix_normalizer = {
    'new york': ['new york', 'nyc', 'brookly', 'bronx', 'ny, ny', 'queens', 'manhattan', 'long island'],
    'london': ['london'],
    'seattle': ['seattle', 'everett, wa', 'tacoma'],
    'san francisco': ['san francisco', 'sf', 'bay area', 'richmond, ca', 'oakland', 'berkeley'],
    'chicago': ['chicago'],
    'los angeles': ['los angeles', 'long beach', 'irvine'],
    'boston': ['boston', 'cambridge'],
    'austin': ['austin'],
    'houston': ['houston'],
    'denver': ['denver'],
    'philadelphia': ['philadelphia'],
    'nashville': ['nashville'],
    'pittsburgh': ['pittsburgh'],
    'atlanta': ['atl'],
    'dehli': ['dehli'],
    'miami': ['miami'],
}

dc_re = re.compile(r'washington\s*[,]?\s*d\.?c\.?')
seattle_re = re.compile(r'seattle')
boston_re = re.compile(r'boston')

def normalize_location(loc_string):
    if loc_string is None:
        return None
    loc_string = loc_string.lower()

    for std_form in prefix_normalizer:
        for prefix in prefix_normalizer[std_form]:
            if loc_string.startswith(prefix):
                return std_form
    if dc_re.search(loc_string):
        return 'dc'
    if seattle_re.search(loc_string):
        return 'seattle'
    if boston_re.search(loc_string):
        return 'boston'
    return loc_string
