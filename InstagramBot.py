from InstagramAPI import InstagramAPI
from random import randint

username = "bot_account_username"
password = "bot_account_password"

# List of random comments
comments = ["Wow!", "Nice post!", "Love this!", "Cool post!", "Follow me!", "Like my last post!", "Love your account!",
"Awsome!", "I like this!"]

# Random hashtag
hashtag = "puppy"

ig = InstagramAPI(username, password)

def likeAllPosts(ig):
    posts = ig.LastJson
    
    for post in range(len(posts) - 1):
        post_id = posts['items'][post]['id']
        ig.like(post_id)
        print("Liked a post")

def commentAllPosts(ig, comments):
    posts = ig.LastJson
   
    for post in range(len(posts) - 1):
        post_id = posts['items'][post]['id']
        random_post = randint(0, len(comments) - 1)
        ig.comment(post_id, comments[random_post])
        # ig.like(post_id) # just to make sure the comment is there
        print("Commented on a post")

# Login
if (ig.login()):
    print("Successfully logged in!")
else:
    print("Login failed!")

# Uncomment what you want to do

# Upload Photo
photo_path = 'photo_path'
caption = "Sample post"
#ig.uploadPhoto(photo_path, caption=caption)

# Like posts on timeline
ig.getTimeline()
#likeAllPosts(ig)      

# Like posts of a specific hashtag
ig.getHashtagFeed(hashtag)
#likeAllPosts(ig)

# Comment on posts of a specific hashtag
ig.getHashtagFeed(hashtag)
 #commentAllPosts(ig, comments)
