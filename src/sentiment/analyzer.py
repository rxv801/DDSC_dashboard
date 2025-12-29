from transformers import pipeline
from typing import Any


def analyze_sentiment(text: str) -> dict[str, Any]:
    sentiment: Any = pipeline(  # type: ignore
        "sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )
    result = sentiment(text)
    return result[0]


while True:
    text = input("enter text: \n")
    results = analyze_sentiment(text)
    print(results)
    print("\n")
