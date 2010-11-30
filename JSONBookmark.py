import copy

_JSON_TITLE = 'title'
_JSON_ID = 'id'
_JSON_PARENT = 'parent'
_JSON_ADD_DATE = 'dateAdded'
_JSON_TYPE = 'type'
_JSON_TYPE_BOOKMARK = 'text/x-moz-place'
_JSON_TYPE_FOLDER = 'text/x-moz-place-container'
_JSON_LINK = 'uri'
_JSON_CHARSET = 'charset'
_JSON_CHARSET_DEFAULT = 'UTF-8'
_JSON_CHILDREN = 'children'
_JSON_ROOT = 'root'

class ExistingChildsError (Exception) :
	def __init__ (self, id) :
		self.id = id
	def __str__(self) :
		return repr('Bookmark folder of id ' + id + ' already has child(s)')

class JSONBookmarkElement :
	def __init__ (self, bookmarkId, title, dateAdded,
			charset = _JSON_CHARSET_DEFAULT) :
		self.data = {
			_JSON_TITLE		: title,
			_JSON_ID		: bookmarkId,
			_JSON_ADD_DATE 	: dateAdded,
			_JSON_CHARSET	: charset
			}

	def clone (self, newId) :
		newBookmark = copy.deepcopy(self)
		newBookmark.data[_JSON_ID] = newId
		return newBookmark

class JSONBookmarksFolder(JSONBookmarkElement) :
	def __init__ (self, bookmarkId, title, dateAdded,
			charset = _JSON_CHARSET_DEFAULT) :
		JSONBookmarkElement.__init__(self, bookmarkId, title,
				dateAdded, charset)
		self.data[_JSON_TYPE] = _JSON_TYPE_FOLDER

	def setRoot (self, root) :
		self.data[_JSON_ROOT] = root

	def addChild(self, jsonBookmark) :
		jsonBookmark.data[_JSON_PARENT] = self.data[_JSON_ID]
		if _JSON_CHILDREN not in self.data :
			self.data[_JSON_CHILDREN] = [jsonBookmark]
		else :
			self.data[_JSON_CHILDREN].append(jsonBookmark)

	def setChilds(self, jsonBookmarksList) :
		if _JSON_CHILDREN in self.data :
			raise ExistingChildsError(self.data[_JSON_ID])
		else :
			self.data[_JSON_CHILDREN] = jsonBookmarksList
			for child in jsonBookmarksList :
				child.data[_JSON_PARENT] = self.data[_JSON_ID]

	def getChild(self, childTitle) :
		if _JSON_CHILDREN in self.data :
			for child in self.data[_JSON_CHILDREN] :
				if child.data[_JSON_TITLE] == childTitle :
					return child
			return None
		else :
			return None

class JSONBookmark (JSONBookmarkElement) :
	def __init__ (self, bookmarkId, title, dateAdded, link, tags,
			charset = _JSON_CHARSET_DEFAULT) :
		JSONBookmarkElement.__init__(self, bookmarkId, title,
				dateAdded, charset)
		self.data[_JSON_TYPE] = _JSON_TYPE_BOOKMARK
		self.data[_JSON_LINK] = link
		self.tags = tags

