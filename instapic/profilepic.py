import instaloader


root = instaloader.Instaloader()
user_name = 'thug_life_sai'
pr=root.download_profile(user_name,profile_pic_only=True)
print(pr)