# Reddit Bot with Groq AI Integration

This project is a Reddit bot that generates and posts daily content to a specified subreddit, as well as generates comments on random posts using Groq AI. It is designed to automate content creation and interaction on Reddit, focusing on topics like Computer Science, Artificial Intelligence, Neural Networks, and more.

---

## Features

1. **Content Generation**: Uses Groq AI to generate topic-specific posts and comments.
2. **Automated Posting**: Posts generated content to a specified subreddit daily.
3. **Automated Commenting**: Comments on random posts in the subreddit.
4. **Scheduling**: Utilizes the `schedule` library to run tasks at defined intervals.

---

## Setup

### Prerequisites

1. **Python**: Ensure Python 3.8 or later is installed.
2. **PIP**: Install required dependencies.
3. **Reddit API Account**: Create a Reddit app and obtain the following credentials:
   - `CLIENT_ID`
   - `CLIENT_SECRET`
   - `USERNAME`
   - `PASSWORD`

4. **Groq API Key**: Obtain an API key from Groq.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a Virtual Environment** (Optional):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and add the following:
   ```env
   CLIENT_ID=<your_reddit_client_id>
   CLIENT_SECRET=<your_reddit_client_secret>
   USERNAME=<your_reddit_username>
   PASSWORD=<your_reddit_password>
   SECRET_KEY=<your_groq_api_key>
   ```

### Required Libraries

Install the necessary Python libraries using pip:
```bash
pip install praw schedule groq-python python-dotenv
```

---

## Usage

1. **Run the Bot**:
   ```bash
   python bot.py
   ```

2. **Scheduled Tasks**:
   - Posts are generated and submitted every 2 minutes (configurable).
   - Comments are generated daily at 10:00 AM (configurable).

3. **Logs**:
   - Check logs for details about successful posts and any errors encountered.

---

## File Structure

```plaintext
.
├── bot.py          # Main bot script
├── requirements.txt # Python dependencies
├── .env             # Environment variables (not included in the repository for security)
├── README.md        # Documentation (this file)
```

---

## Customization

1. **Topics**:
   Modify the `Topics` list in the `generate_content` function to include your preferred topics.

2. **Subreddit**:
   Change `subreddit_name` in the `daily_post` and `generate_comment` functions to target a different subreddit.

3. **Schedule**:
   Adjust the `schedule.every` statements to change posting/commenting frequency.

---

## Error Handling

- **Content Generation Issues**: Logs errors if Groq AI fails to generate content.
- **Reddit API Errors**: Logs errors when posting or commenting fails.
- **General Logs**: Check `logging.info` and `logging.error` outputs for debugging.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Disclaimer

- Ensure compliance with Reddit's API rules and policies.
- Avoid spamming subreddits or violating community guidelines.
