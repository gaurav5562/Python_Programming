from pytube import YouTube
url="https://youtu.be/ydQtI30SbBg"
obj=YouTube(url)
resolutions=[]
# size=[]
# title_video=obj.title
# thumbnail_video=obj.thumbnail_url
# stm_all=obj.streams

res=obj.streams.filter(progressive = True)

for i in res:
	resolutions.append(i)
print(resolutions)	

# for i in stm_all:
# 	resolutions.append(i.resolution)
# 	size.append(round(int(i.filesize)/(1024*1024),2))
# print(resolutions)	
# resolutions=list(dict.fromkeys(resolutions))
# size=list(dict.fromkeys(size))		
# embd_link=url.replace("watch?v=","embed/")
# my_dict={'reso':resolutions,'embd':embd_link,'title_video':title_video,'thumbnail_video':thumbnail_video}

# print(thumbnail_video)
# print(title_video)
# print(size)
# print(resolutions)
print()
print()