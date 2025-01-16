



from groq import Groq
import os
import praw
import logging
import schedule
import time



GROQ_API_KEY= os.getenv("SECRET_KEY")
USERNAME=os.getenv("USERNAME")
PASSWORD= os.getenv("PASSWORD")
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
reddit=praw.Reddit(client_id = CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    password=PASSWORD,
                    username = USERNAME,user_agent="test_bot")
client = Groq(api_key=GROQ_API_KEY)
   


def generate_content():
    """Generate content using Groq AI."""
    try:

        Topics=["CS","AI","Neural Networks","Data Structures and Algorithms","Leetcode POTD"]
        string1=",".join(Topics)
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"Give a daily post as a Reddit moderator from any of the following topics {string1} ",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
        return chat_completion.choices[0].message.content
    except:
        logging.error(f"Error generating content:")
        return None

def post_to_reddit(subreddit_name, title, content):
    """Post content to a specified subreddit."""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=content)
        logging.info(f"Post successful: {title}")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")

def daily_post():
    """Generate and post content daily."""
    logging.info("Starting daily post routine.")
    content = generate_content()
    if content:
        post_to_reddit(subreddit_name="test", title=content[:200], content=content)

def generate_comment(subreddit_name):
    """Generate and post a comment on a random post in a subreddit."""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=10):
            content = generate_content()
            if content:
                post.reply(content)
                logging.info(f"Commented on post: {post.title}")
                break
    except Exception as e:
        logging.error(f"Error commenting on Reddit: {e}")

# Schedule daily posting
schedule.every(2).minutes.do(daily_post)

# Bonus: Schedule comment generation
schedule.every().day.at("10:00").do(lambda: generate_comment(subreddit_name="test"))

if __name__ == "__main__":
    logging.info("Reddit bot started.")
    while True:
        schedule.run_pending()
        time.sleep(1)
