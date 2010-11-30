# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import json
from JSONBookmark import JSONBookmarkElement

class JSONBookmarkEncoder (json.JSONEncoder) :
	def default(self,obj) :
		if isinstance(obj, JSONBookmarkElement) :
			return obj.data
		else :
			return json.JSONEncoder.default(self,obj)

