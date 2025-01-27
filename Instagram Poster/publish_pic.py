# Imports
from instagrapi import Client

# Logs in to Instagram and posts specified pic with specified caption
def post_to_instagram(username, password, image_path, ig_caption):

    try:
        cl = Client()
        cl.login(username, password)  # Log in
        cl.photo_upload(image_path, ig_caption)  # Upload photo and caption
        print("\nPost successful!")

    # Error handling
    except Exception as e:
        print(f"\nAn error occurred: {e}")
