import urllib, urllib2, json

class Salary:

    def __init__(self, username):

        url = 'https://socialblade.com/js/class/youtube-money-calculator'

        param = { 'query' : username }

        self.req = urllib2.Request(url, urllib.urlencode(param))
        self.req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        self.req.add_header('origin', 'https://socialblade.com/js/class/youtube-money-calculator')
        self.req.add_header('referer', 'https://socialblade.com/js/class/youtube-money-calculator')

    def get(self):
        data = urllib2.urlopen(self.req)

        return data.read()
