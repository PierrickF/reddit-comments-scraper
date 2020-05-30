import praw     # To use the reddit API.
import time     # To use sleep().

# This is a read-only Reddit instance.
reddit = praw.Reddit(client_id="ml9nlUyBYrhExw",                            # Do not share this information.
                     client_secret="_wV2Qfvoip4AxMEiNi9GB3rG5Bc",           # Do not share this information.
                     user_agent="python:msc_dissertation_scrapper:v1.0")    # Do not share this information.

# Information regarding network requests limits, in a dictionary.
# The keys are: number of requests remaining, time when the counter will reset, and number of requests made.
# The limit is 60 requests per minute.
net_requests = reddit.auth.limits

# Set the number of requests remaining to an integer value so the while loop below can initialize.
net_requests["remaining"] = 60

# Structure for the data gathered: a list of lists.
# Each comment is a list containing its information: ID, author, time, comment, etc.
reddit_data = []

# Obtain a subreddit.
subreddit = reddit.subreddit("wow")

# Scrapping loop.
for submission in subreddit.hot(limit=None):    # Iterate through the hottest submissions in r/wow.
    while net_requests["remaining"] <= 1:       # Check there are more than 1 network request allowed left.
        print("Maximum network requests reached. Sleeping for 61 seconds.")
        time.sleep(61)                          # Wait for more network requests to be allowed.
    else:
        submission.comments.replace_more(limit=None)    # Reveal comments hidden behind "More comments" links.
        for comment in submission.comments.list():      # Iterate through the comments of each submission.
            comment_data = [comment.link_id,    # Create a list for each comment and add the submission ID.
                            comment.parent_id,  # Add the ID of the parent comment, or the submission ID if top comment.
                            comment.id,         # Add the ID of the comment.
                            comment.created_utc,        # Add the time the comment was created in Unix Time.
                            comment.author,             # Add the username of the comment's author.
                            comment.body]               # Add the comment itself.
            reddit_data.append(comment_data)            # Add all of the above in a meta list.

# Save the data in a text file.
with open("reddit_data.txt", "a") as f:     # Parameter "a" means "append", to run the script multiple times.
    for item in reddit_data:
        f.write("%s\n" % item)              # Jump to next line before writing the next item.

# Printing the number of comments gathered.
print("Scrapped {0} comments.".format(len(reddit_data)))
