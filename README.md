This Python script scraps reddit comments from a specific subreddit.

It uses PRAW: Python Reddit API Wrapper.

https://praw.readthedocs.io

Authenticating is required, the three "TOP_SECRET" placeholders need to be replaced.

https://praw.readthedocs.io/en/latest/getting_started/authentication.html

The script gathers the following data:
- Submission ID
- ID of the parent comment
- ID of the comment
- Time at which the comment was posted
- Username of the comment's author
- Comment itself

The data is gathered in the form of a list of lists.
It is then stored in a text file.

See also reddit's API:

https://github.com/reddit-archive/reddit/wiki/API
