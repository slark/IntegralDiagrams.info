import flickrapi
from django.shortcuts import render_to_response

API_KEY = "80819a22922b12c2882bbdf129f951da"
flickr = flickrapi.FlickrAPI(API_KEY, cache = True)
USER_ID = "92888631@N00"
INTEGRAL_DIAGRAMS_SET = "939928"
NAV_BAR = ["subjects", "authors", "sources", "more"]
SET_NAV_BAR = ["thumbnails", "details"]
COLLECTION_SUBJECTS = "245016-72157600929284498"
COLLECTION_AUTHORS  = "245016-72157600929429778"

collection = flickr.collections_getTree(collection_id = COLLECTION_SUBJECTS,
                                        user_id = USER_ID)
setID = []
setTitle = []
subjectList = []
for i in collection[0][0]:
	setID.append(i.get("id"))
	setTitle.append(i.get("title"))
for i in range(len(setID)):
	subjectList.append([])
	subjectList[i].append(setID[i])
	subjectList[i].append(setTitle[i])
subjectDict = dict(subjectList)
	
collection = flickr.collections_getTree(collection_id = COLLECTION_AUTHORS,
                                        user_id = USER_ID)
setID = []
setTitle = []
authorList = []
for i in collection[0][0]:
	setID.append(i.get("id"))
	setTitle.append(i.get("title"))
for i in range(len(setID)):
	authorList.append([])
	authorList[i].append(setID[i])
	authorList[i].append(setTitle[i])
authorDict = dict(authorList)
	
def setThumbnails(setID, allPageNum = "1"):
	details = flickr.photosets_getPhotos(photoset_id = setID, 
	                                     extras = "url_t", 
	                                     page = allPageNum)
	title = []
	photoID = []
	thumbURL = []
	thumbList = []
	for i in range(len(details[0])):
		title.append(details[0][i].get("title"))
		photoID.append(details[0][i].get("id"))
		thumbURL.append(details[0][i].get("url_t"))
		thumbList.append([])
		thumbList[i].append(title[i])
		thumbList[i].append(photoID[i])
		thumbList[i].append(thumbURL[i])
	return thumbList

def home(request):
	return render_to_response("home.html", {"navBar":NAV_BAR,
	                                        "homePage":True})

def subjects(request):
	return render_to_response("layout.html", {"navBar":NAV_BAR,
	                                          "navLink":"subjects",
	                                          "pageTitle":"subjects",
	                                          "setNavLink":"thumbnails",
	                                          "listContent":subjectList})

def authors(request):
	return render_to_response("layout.html", {"navBar":NAV_BAR,
	                                          "navLink":"authors",
	                                          "pageTitle":"authors",
	                                          "setNavLink":"thumbnails",
	                                          "listContent":authorList})

def sources(request):
	return render_to_response("sources.html", {"navBar":NAV_BAR,
	                                           "navLink":"sources",
	                                           "pageTitle":"sources"})

def more(request):
	return render_to_response("more.html", {"navBar":NAV_BAR,
	                                        "navLink":"more",
	                                        "pageTitle":"more"})

def all(request, allPageNum):
	pageTitle = "all&nbsp;diagrams&nbsp;&rarr;&nbsp;page&nbsp;" + allPageNum
	projectInfo = flickr.photosets_getInfo(photoset_id = INTEGRAL_DIAGRAMS_SET)
	numDiagrams = projectInfo[0].get("photos")
	allNumberPages = []
	for i in range((int(numDiagrams) / 500) + 1):
		allNumberPages.append(str(i + 1))
	numSubjects = len(subjectList)
	numAuthors = len(authorList)
	diagramContent = setThumbnails(INTEGRAL_DIAGRAMS_SET, allPageNum)
	return render_to_response("all.html", {"navBar":NAV_BAR,
	                                       "pageTitle":pageTitle,
	                                       "allPageNum":allPageNum,
	                                       "allNumberPages":allNumberPages,
	                                       "numDiagrams":numDiagrams,
	                                       "numSubjects":numSubjects,
	                                       "numAuthors":numAuthors,
	                                       "diagramContent":diagramContent})

def thumbnails(request, navLink, setID):
	setInfo = flickr.photosets_getInfo(photoset_id = setID)
	listContent = []
	if setID in subjectDict:
		navLink = "subjects"
		setTitle = subjectDict.get(setID)
		listContent = subjectList
	elif setID in authorDict:
		navLink = "authors"
		setTitle = authorDict.get(setID)
		listContent = authorList
	pageTitle = navLink + "&nbsp;&rarr;&nbsp;" + setTitle
	diagramContent = setThumbnails(setID)
	return render_to_response("thumbnails.html", {"navBar":NAV_BAR,
	                                              "navLink":navLink,
	                                              "setNavBar":SET_NAV_BAR,
	                                              "setNavLink":"thumbnails",
	                                              "pageTitle":pageTitle,
	                                              "setTitle":setTitle,
	                                              "setID":setID,
	                                              "listContent":listContent,
	                                            "diagramContent":diagramContent})

def details(request, navLink, setID):
	setInfo = flickr.photosets_getInfo(photoset_id = setID)
	listContent = []
	if setID in subjectDict:
		navLink = "subjects"
		setTitle = subjectDict.get(setID)
		listContent = subjectList
	elif setID in authorDict:
		navLink = "authors"
		setTitle = authorDict.get(setID)
		listContent = authorList
	pageTitle = navLink + "&nbsp;&rarr;&nbsp;" + setTitle
	details = flickr.photosets_getPhotos(photoset_id = setID, extras = "url_m")
	title = []
	photoID = []
	mediumURL = []
	description = []
	diagramContent = []
	for i in range(len(details[0])):
		title.append(details[0][i].get("title"))
		photoID.append(details[0][i].get("id"))
		mediumURL.append(details[0][i].get("url_m"))
		diagramInfo = flickr.photos_getInfo(photo_id = details[0][i].get("id"))
		description.append(diagramInfo[0][2].text)
		diagramContent.append([])
		diagramContent[i].append(title[i])
		diagramContent[i].append(photoID[i])
		diagramContent[i].append(mediumURL[i])
		diagramContent[i].append(description[i])
	return render_to_response("details.html", {"navBar":NAV_BAR,
	                                           "navLink":navLink,
	                                           "setNavBar":SET_NAV_BAR,
	                                           "setNavLink":"details",
	                                           "pageTitle":pageTitle,
	                                           "setTitle":setTitle,
	                                           "setID":setID,
	                                           "listContent":listContent,
	                                           "diagramContent":diagramContent})

def diagram(request, photoID):
	subjectID = []
	subjectTitle = []
	diagramSubjectList = []
	authorID = []
	authorTitle = []
	diagramAuthorList = []
	contexts = flickr.photos_getAllContexts(photo_id = photoID)
	for i in range(len(contexts)):
		if contexts[i].get("id") in subjectDict:
			subjectID.append(contexts[i].get("id"))
			subjectTitle.append(contexts[i].get("title"))
		elif contexts[i].get("id") in authorDict:
			authorID.append(contexts[i].get("id"))
			authorTitle.append(contexts[i].get("title"))
	for i in range(len(subjectID)):
		diagramSubjectList.append([])
		diagramSubjectList[i].append(subjectID[i])
		diagramSubjectList[i].append(subjectTitle[i])
	for i in range(len(authorID)):
		diagramAuthorList.append([])
		diagramAuthorList[i].append(authorID[i])
		diagramAuthorList[i].append(authorTitle[i])
	info = flickr.photos_getInfo(photo_id = photoID)
	title = info[0][1].text
	description = info[0][2].text
	sizes = flickr.photos_getSizes(photo_id = photoID)
	if len(sizes[0]) == 6:
		diagramContent = sizes[0][5].get("source") # large size URL
	else:
		diagramContent = sizes[0][4].get("source") # original size URL
	return render_to_response("diagram.html", {"navBar":NAV_BAR,
	                                          "subjectList":diagramSubjectList,
	                                           "authorList":diagramAuthorList,
	                                           "photoID":photoID,
	                                           "pageTitle":title,
	                                           "title":title,
	                                           "description":description,
	                                           "diagramContent":diagramContent})
