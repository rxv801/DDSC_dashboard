import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
from tqdm import tqdm
from src.sentiment.analyzer import analyze_sentiment

# Get project root and build path
project_root = Path(__file__).parent.parent
csv_path = project_root / "data" / "discord_messages.csv"

# Load CSV
df = pd.read_csv(csv_path)

# Add progress bar
tqdm.pandas(desc="Analyzing sentiment")

# Add sentiment column with progress bar
df["sentiment"] = df["message"].progress_apply(
    lambda x: analyze_sentiment(str(x))["label"]
    if pd.notna(x) and str(x).strip()
    else "neutral"
)

print(df[["message", "sentiment"]].head())
