import requests
Post_url = "http://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        self.url = Post_url
        self.data = []
        self.get_posts()

    def get_posts(self):
        response = requests.get(url=self.url)
        self.data = response.json()
