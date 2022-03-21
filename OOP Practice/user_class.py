from post_class import Post


class User:
    def __init__(self, email, name, password, job_title):
        self.email = email
        self.name = name
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"Username is {self.name} and the password will be {self.password}."
              f" Currently working as {self.job_title} and you can contact him at {self.email}")

    def post(self):
        Post(self.name, "This is a message").get_post()
