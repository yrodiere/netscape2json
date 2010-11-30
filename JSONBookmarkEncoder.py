import json
from JSONBookmark import JSONBookmarkElement

class JSONBookmarkEncoder (json.JSONEncoder) :
	def default(self,obj) :
		if isinstance(obj, JSONBookmarkElement) :
			return obj.data
		else :
			return json.JSONEncoder.default(self,obj)

