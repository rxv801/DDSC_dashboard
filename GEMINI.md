# DDSC-Dashboard Project Context

## Project Overview
This project is a data dashboard for managing the "DDSC" club. It integrates membership data, financial tracking, and community sentiment analysis into a centralized interface. The application serves as a demonstration of skills in data analysis, web development (Streamlit), and machine learning.

## Architecture & Tech Stack

*   **Framework:** Streamlit (Python)
*   **Database:** PostgreSQL (primary storage for Members), CSV (storage for Discord message logs).
*   **Machine Learning:** Scikit-learn (Linear Regression for membership forecasting).
*   **NLP:** Hugging Face Transformers (`cardiffnlp/twitter-roberta-base-sentiment-latest`) for sentiment analysis.
*   **Visualization:** Plotly Express.
*   **External Integration:** Discord Bot (`discord.py`) for data collection.

## Directory Structure

*   `app.py`: The main entry point for the Streamlit application.
*   `pages/`: Contains the individual dashboard pages (Streamlit multipage app structure).
    *   `members.py`: Displays membership data, trends, and future predictions.
    *   `finances.py`: (Assumed) Financial tracking.
    *   `sentiment.py`: Currently a script for running sentiment analysis on CSV data (work in progress).
*   `src/`: Core application logic.
    *   `discord_bot/bot.py`: A bot that logs Discord messages to `data/discord_messages.csv`.
    *   `model/training.py`: Logic for training the membership prediction model using Linear Regression.
    *   `sentiment/analyzer.py`: Wrapper around the Hugging Face sentiment analysis pipeline.
    *   `utils/`: Utility functions (e.g., database connection).
*   `data/`: Stores local data files like `discord_messages.csv`.

## Setup & Development

### Prerequisites
*   Python 3.x
*   PostgreSQL database (for membership data).
*   Discord Bot Token (for message logging).

### Installation
1.  **Environment Variables:** Create a `.env` file with:
    ```
    DB_URL="postgresql://user:password@host:port/database"
    DISCORD_TOKEN="your-discord-bot-token"
    ```
2.  **Dependencies:**
    ```bash
    pip install -r requirements.txt
    # Note: 'transformers' and 'torch' might be missing from requirements.txt but are needed for sentiment analysis.
    pip install transformers torch
    ```

### Running the Application

1.  **Start the Dashboard:**
    ```bash
    streamlit run app.py
    ```
    Access at `http://localhost:8501`.

2.  **Run the Discord Bot (Data Collection):**
    ```bash
    python src/discord_bot/bot.py
    ```
    This logs messages to `data/discord_messages.csv`.

## Key Logic Details

*   **Membership Prediction:** `src/model/training.py` fetches data from the `MEMBERS` table, aggregates it by month, and trains a Linear Regression model to predict the next month's member count.
*   **Sentiment Analysis:** `src/sentiment/analyzer.py` uses a pre-trained RoBERTa model. `pages/sentiment.py` currently reads the CSV and prints sentiment to the console; it does not yet render visualizations in Streamlit.
*   **Database Connection:** Handled via `src/utils/utils.py` using `sqlalchemy`.

## Conventions
*   **Path Handling:** Uses `pathlib` for robust path management across operating systems.
*   **Code Style:** Follows standard Python structure. Imports are organized (standard lib, 3rd party, local).
*   **Type Hinting:** Some usage of type hints (e.g., `dict[str, Any]`).
