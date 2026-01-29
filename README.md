# DDSC-Dashboard

A comprehensive dashboard for managing the "DDSC" club, providing insights into membership, finances, and community sentiment. This project is designed to showcase skills in data analysis, web development, and machine learning, making it an ideal project for an internship application.

## Features

- **Membership Tracking**: View and manage club membership data. Includes a predictive model to forecast next month's membership numbers.
- **Financial Management**: Track club finances with an easy-to-use interface for adding new transactions.
- **Discord Sentiment Analysis**: Analyze the sentiment of messages from your club's Discord server to gauge community morale.
- **Data-driven Insights**: Utilizes various data analysis and visualization techniques to provide actionable insights.
- **Discord Bot**: A dedicated bot to automatically log messages from specified channels for sentiment analysis.

## Tech Stack

- **Backend**: Python, Streamlit, Pandas, SQLAlchemy
- **Database**: PostgreSQL (or any other SQL-based database)
- **Machine Learning**: Scikit-learn, Hugging Face Transformers
- **Data Visualization**: Plotly

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/DDSC-Dashboard.git
   cd DDSC-Dashboard
   ```

2. **Create a virtual environment and install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - Make sure you have a running PostgreSQL instance.
   - Create a `.env` file in the root directory and add your database connection details:
     ```
     DB_URL="postgresql://user:password@host:port/database"
     ```

4. **Set up the Discord bot**:
   - Create a Discord bot and get the token.
   - Add the token to your `.env` file:
     ```
     DISCORD_TOKEN="your-discord-bot-token"
     ```
   - Invite the bot to your Discord server.

## Usage

1. **Run the Discord bot**:
   ```bash
   python src/discord_bot/bot.py
   ```
   This will start the bot and it will begin logging messages from the specified channels.

2. **Run the Streamlit dashboard**:
   ```bash
   streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501` to view the dashboard.

## Project Structure

```
/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (DB_URL, DISCORD_TOKEN)
├── data/
│   └── discord_messages.csv # Logged Discord messages
├── pages/
│   ├── finances.py         # Finances page
│   ├── members.py          # Membership page
│   ├── misc.py             # Miscellaneous tasks page
│   └── sentiment.py        # Sentiment analysis script
└── src/
    ├── discord_bot/
    │   └── bot.py            # Discord bot
    ├── model/
    │   └── training.py       # Membership prediction model
    ├── sentiment/
    │   └── analyzer.py     # Sentiment analysis module
    └── utils/
        └── utils.py          # Utility functions
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
