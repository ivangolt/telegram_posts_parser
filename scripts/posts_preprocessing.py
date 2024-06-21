import re
from pathlib import Path

import click
import nltk
import pandas as pd
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("russian"))

# Регулярное выражение для удаления смайлов
emoji_pattern = re.compile(
    "["
    "\U0001f600-\U0001f64f"  # emoticons
    "\U0001f300-\U0001f5ff"  # symbols & pictographs
    "\U0001f680-\U0001f6ff"  # transport & map symbols
    "\U0001f1e0-\U0001f1ff"  # flags (iOS)
    "\U00002702-\U000027b0"
    "\U000024c2-\U0001f251"
    "]+",
    flags=re.UNICODE,
)

# Регулярное выражение для удаления ссылок
url_pattern = re.compile(r"https?://\S+")


def text_preprocessing(text: str) -> str:
    """_summary_

    Args:
        text (str): input disription of vacansy

    Returns:
        str: output preprocessed discription of vacancy
    """
    text = emoji_pattern.sub(r"", text)
    text = url_pattern.sub(r"", text)
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    return " ".join(filtered_tokens)


@click.command()
@click.argument("input_path_of_dataframe", type=Path)
@click.argument("output_path_of_dataframe", type=Path)
def posts_preprocessing(input_path_of_dataframe: Path, output_path_of_dataframe: Path):
    posts_df = pd.read_csv(input_path_of_dataframe)
    posts_df["content"] = posts_df["content"].dropna()
    posts_df["content"] = posts_df["content"].astype(str)
    posts_df["content"] = posts_df["content"].apply(text_preprocessing)
    posts_df.to_csv(output_path_of_dataframe)


if __name__ == "__main__":
    posts_preprocessing()
