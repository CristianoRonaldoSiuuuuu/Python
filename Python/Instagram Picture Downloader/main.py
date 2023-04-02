import instaloader
import os

loader = instaloader.Instaloader()

post_numbers = input("Enter Instagram post numbers (separated by commas): ")

post_numbers_list = post_numbers.split(",")

for number in post_numbers_list:
    url = f"https://www.instagram.com/p/{number}/"

    try:
        post = instaloader.Post.from_shortcode(loader.context, number)

        # Create the target directory if it doesn't exist
        target_dir = "C:\\Users\\Taha\\Desktop\\Python\\Instagram Picture Downloader\\Downloads\\post_" + number
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Save the post to the target directory with the post shortcode as the filename
        loader.download_post(post, target=target_dir)

        print(f"Image for post {number} downloaded successfully!")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Post {number} not found.")

    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"You need to be following the owner of post {number} to download the image.")

    except Exception as e:
        print(f"An error occurred while downloading the image for post {number}: {e}")
