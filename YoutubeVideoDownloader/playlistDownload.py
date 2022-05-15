import os
from pytube import Playlist
count=0
def file_path(heading):
    home = os.getcwd()
    path_current = os.path.join(home, heading)
    return path_current
def convert_str(titls):
	st=""
	for i in titls:
		if i=='|' or i=='!' or i=='/' :
			pass
		else:
			st=st+i
	return st
if __name__ == '__main__':
	try:
		url_playlist=input("Enter the url of Playlist   :-    ")
		print('Please wait while we prepareing download')
		yt=Playlist(url_playlist)
		titls=list(yt.title)
		playlist_length=len(yt.video_urls)
		heading=str(convert_str(titls))
		print(f'Number of video in playlist is {playlist_length}')
		for x in yt.videos:
			count=count+1
			print(f'Title of video {count} is :--{x.title}')
			x.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(file_path(heading))
			print(f'video {count} out of {playlist_length} downloaded successfully ')
		if count==len(yt.video_urls):
			print("Playlist downloaded successfully")	
	except Exception as e:
		print('Some error occured')
		# get_by_itag(134)
		# return FileResponse(open(YouTube(url).streams.first().download(skip_existing=True),'rb'))

