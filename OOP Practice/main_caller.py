import user_class


user_app_1 = user_class.User("jj@jj", "Jack", "123123", "Fullstack Developer")
user_app_1.get_user_info()
user_app_1.change_job_title("Mobile App Developer")
user_app_1.get_user_info()
user_app_1.post()
