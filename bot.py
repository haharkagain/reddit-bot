import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1')
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as g:
        comments_replied_to = g.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=2):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("hey boss")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
subreddit_comments = subreddit.stream.comments(skip_existing = True)
for comment in subreddit_comments:
    if comment.id not in comments_replied_to:
        if re.search("hey boss", comment.body, re.IGNORECASE):
            comment.reply("can i habe pizza plz")
            print("Bot replying to: ", comment.body)
            comments_replied_to.append(comment.id)
            break
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
with open("comments_replied_to.txt", "w") as g:
    for comment_id in comments_replied_to:
        g.write(comment_id + "\n")