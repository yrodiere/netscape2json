from JSONBookmark import JSONBookmark, JSONBookmarksFolder

_PLACES_ROOT = 'placesRoot'
_PLACES_TITLE = ''
_BOOKMARKS_MENU_FOLDER_ROOT = 'bookmarksMenuFolder'
_BOOKMARKS_MENU_FOLDER_TITLE = 'Menu des marque-pages'
_TAGS_FOLDER_ROOT = 'tagsFolder'
_TAGS_FOLDER_TITLE = 'Étiquettes'

_TAGS_SEPARATOR = ','

class JSONMozBookmarksBuilder :
	def build (self, bookmarksList, startId, timestamp) :
		# Bookmarks root
		root = JSONBookmarksFolder(startId, _PLACES_TITLE, timestamp)
		root.setRoot(_PLACES_ROOT)
		startId += 1

		# Bookmarks menu folder
		bookmarksFolder = JSONBookmarksFolder(startId, _BOOKMARKS_MENU_FOLDER_TITLE, timestamp)
		bookmarksFolder.setRoot(_BOOKMARKS_MENU_FOLDER_ROOT)
		startId += 1
		
		# Bookmarks tags folder
		tagsFolder = JSONBookmarksFolder(startId, _TAGS_FOLDER_TITLE, timestamp)
		tagsFolder.setRoot(_TAGS_FOLDER_ROOT)
		startId += 1
		
		# Create base structure
		root.addChild(bookmarksFolder)
		root.addChild(tagsFolder)
		bookmarksFolder.setChilds(bookmarksList)
		
		# Parse tags
		for bookmark in bookmarksList :
			for tag in bookmark.tags.split(_TAGS_SEPARATOR) :
				startId = self._cloneBookmarkInSubfolder(tagsFolder, tag, bookmark, startId) 

		return root

	def _cloneBookmarkInSubfolder(self, folder, subfolderName, bookmarkModel, startId) :
		subfolder = folder.getChild(subfolderName)

		# Subfolder may not exist, create it if necessary
		if subfolder == None :
			subfolder = JSONBookmarksFolder(startId, subfolderName, startId)
			startId += 1
			folder.addChild(subfolder)

		# We found the subfolder, clone the bookmark
		subfolder.addChild(bookmarkModel.clone(startId))
		startId += 1
		return startId

