"""
Google trend hot video item crawler

Eason Cao (eason@lenlabs.com)
"""
import urllib, urllib2, json

class GoogleTrend:

    def __init__(self, hvd = '', geo = 'US'):

        url = 'https://trends.google.com.tw/trends/hotvideos/hotItems'

        param = { 'hvd' : hvd, 'geo' : geo, 'mob' :0, 'hvsm' :1 }

        self.req = urllib2.Request(url, urllib.urlencode(param))
        self.req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        self.req.add_header('origin', 'https://trends.google.com.tw')
        self.req.add_header('referer', 'https://trends.google.com.tw/trends/hotvideos')

    def get(self):
        video_list = []
        data = urllib2.urlopen(self.req)
        raw_json = json.loads(data.read())

        if 'videoList' in raw_json:

            for video in raw_json['videoList']:
                # print "%s : " % video['title']
                video_list.append(video['title'])

        return video_list
