from xml.dom import minidom
from JSONBookmark import JSONBookmark

_INPUT_BOOKMARK = 'A'
_INPUT_LINK = 'HREF'
_INPUT_ADD_DATE = 'ADD_DATE'
_INPUT_TAGS = 'TAGS'

class JSONBookmarksHTMLExtractor :
	def extractFromFile (self, file, idStart = 0) :
		dom = minidom.parse(file)
		idCounter = idStart
		bookmarks = []
		for node in dom.getElementsByTagName(_INPUT_BOOKMARK):
			idCounter += 1
			bookmark = JSONBookmark(
					idCounter,
					node.firstChild.nodeValue,
					node.getAttribute(_INPUT_ADD_DATE),
					node.getAttribute(_INPUT_LINK),
					node.getAttribute(_INPUT_TAGS)
					)
			bookmarks.append(bookmark)
		return (bookmarks, idCounter+1)

