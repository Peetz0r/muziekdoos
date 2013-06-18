from apiclient.discovery import build
from optparse import OptionParser
import config
import subprocess


# depends:
# http://code.google.com/p/google-api-python-client/downloads/list
# youtube-dl

def search(query):
	youtube = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION, developerKey=config.YOUTUBE_API_KEY)

	videos = youtube.search().list(q=query, part="id,snippet", maxResults=10, type="video", videoDefinition="high").execute()

	for video in videos["items"]:
		if video["snippet"]["channelTitle"].endswith("VEVO") or video["snippet"]["channelTitle"] == ("SpinninRec"):
			print video["snippet"]["channelTitle"], " === ", video["snippet"]["title"]
			return subprocess.check_output(["youtube-dl", "-g", video["id"]["videoId"]])
			
	return False
