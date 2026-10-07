import youtube_dl, requests, csv
from bs4 import BeautifulSoup as soup

#################################################################################################
#################################################################################################

def youtube_download_init():
	return youtube_dl.YoutubeDL()

def download_liveleak():
	ydl = youtube_download_init()
	ydl.download(["https://www.liveleak.com/view?t=ZdkC_1570677513"])

def write_file(keyword):
	a = open(str(keyword) + ".csv", "a+")
	return csv.writer(a)

def liveleak_keywords():
	# return ["russia dashcam"]
	return ["dashcam", "russia dashcam", "syria", "car accident"]

#################################################################################################
#################################################################################################

def get_results(keyword, page_num):
	a = requests.get("https://www.liveleak.com/browse?q=" + keyword + "&page=" + str(page_num))
	a =  soup(a.content)
	return a.findAll("div",{"class":"featured_items_outer"})

def get_results_item_attributes(results_item):
	a = results_item
	b = a.find("div", {"class": "featured_text_con"})
	return b

def get_vid_href(results_item):
	a = results_item
	b = a.find("a", href=True)["href"]
	c = a.text
	return [b, c]

def get_vid_date(vid_attr):
	return str(vid_attr.text).split("Leaked: ")[1].split(" in:")[0]

def get_vid_user(vid_attr):
	return str(vid_attr.text).split("By: ")[1].split(" (")[0]

def get_vid_comments(vid_attr):
	return str(vid_attr.text).split("Comments: ")[1].split(" |")[0]

def get_vid_views(vid_attr):
	return str(vid_attr.text).split("Views: ")[1].split(" |")[0]

def compile_results_attributes(results_item):
	a = get_results_item_attributes(results_item)
	b = get_vid_href(results_item)
	c = b[1].encode("utf8")
	b = b[0]
	return [b, c, get_vid_date(a), get_vid_user(a), get_vid_comments(a), get_vid_views(a)]

#################################################################################################
#################################################################################################

def get_page_info(url):
	a = requests.get(url)
	a =  soup(a.content)
	return a.findAll("div",{"id":"item_info"})

def get_time_date(page_info):
	return page_info.find("time")["datetime"]

def get_tags(page_info):
	for a in  page_info.findAll("p"):
		if "Tags:" in str(a):
			return str(a).text.replace("Tags:", "").split(", ")

#################################################################################################
#################################################################################################



#################################################################################################
#################################################################################################

def init():
	# url = "https://www.liveleak.com/view?t=spVxe_1570714207"
	for a in liveleak_keywords():
		b = write_file(a)
		c = 0
		z = True
		while c < 5:
			# print(a)
			# print(c)7
			y = get_results(a, c)
			for d in y:
				print(len(d))
				if len(y) > 0:
					try:
						e = compile_results_attributes(d)
						b.writerow(e)
						print(e)
						print("-"*5)
					except:
						pass
				else:
					z = False
					break
			print(len(y))
			if len(y) == 0:
				break
			if z == False:
				break	
			print("-"*50)
			c+=1

init()
	# for a in liveleak_categories():