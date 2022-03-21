class Post:
    def __init__(self, author, message):
        self.author = author
        self.message = message

    def get_post(self):
        print(f"Post : {self.message} is written by {self.author}")
