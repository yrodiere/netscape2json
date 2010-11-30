#!/usr/bin/env python3.1
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import sys
from JSONBookmarksHTMLExtractor import JSONBookmarksHTMLExtractor
from JSONMozBookmarksBuilder import JSONMozBookmarksBuilder
from JSONBookmarkEncoder import JSONBookmarkEncoder

_MSG_ARGUMENT_NEEDED = 'Usage: netscape2json sourceFile'

def __main__ () :
	if len(sys.argv) <= 1 :
		print(_MSG_ARGUMENT_NEEDED)
		return 1
	else :
		pair = JSONBookmarksHTMLExtractor().extractFromFile(open(sys.argv[1]))
		encoder = JSONBookmarkEncoder()
		result = JSONMozBookmarksBuilder().build(pair[0],pair[1],0)
		print(encoder.encode(result))
		return 0

__main__()
