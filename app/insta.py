import os
from instapy import InstaPy
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('INSTA_USER')
password = os.getenv('INSTA_PASS')

session = InstaPy(username=username, password=password)
session.login()

session.like_by_tags(["لباس", ], amount=5)
session.set_do_follow(True, percentage=50)
