import logging

import click
import pandas as pd
import snscrape.modules.telegram as sntelegram

from telegram_posts_parser.telegram_channels import telegram_channels_to_parse

logging.basicConfig(level=logging.INFO)


OUTPUT_FILE = "../data/posts.csv"


TOTAL_POSTS_TO_FETCH = 150


def parse_channel(channel_name: str, number_of_posts: int) -> list:
    """
    Parses posts from a specified Telegram channel.

    Args:
        channel_name (str): The name of the Telegram channel to parse posts from.
        number_of_posts (int): The maximum number of posts to parse from the channel.

    Returns:
        list: A list containing the parsed posts from the specified channel.

    This function parses posts from the given Telegram channel using the snscrape library.
    It iterates over the posts using the TelegramChannelScraper and stops when the specified
    number of posts has been reached. The parsed posts are stored in a list and returned.
    """
    channel_posts = []

    for i, mydata in enumerate(
        sntelegram.TelegramChannelScraper(channel_name).get_items()
    ):
        if i > number_of_posts:
            break
        channel_posts.append(mydata)

    return channel_posts


def fetch_posts(channel: str) -> list:
    """
    Fetches vacancies from the specified Telegram channel.

    Args:
        channel (str): The name of the Telegram channel to fetch vacancies from.

    Returns:
        list: A list containing the fetched vacancies from the specified channel.

    This function retrieves vacancies from the given Telegram channel by utilizing
    the parse_channel() function. It logs information about the fetching process
    including the channel name and the number of vacancies fetched.
    """
    logging.info(f"Fetching posts from channel: {channel}")
    channel_data = parse_channel(
        channel_name=channel, number_of_posts=TOTAL_POSTS_TO_FETCH
    )
    logging.info(f"Fetched {len(channel_data)} posts from channel: {channel}")
    return channel_data


@click.command()
@click.argument("output_folder_path")
def parse_posts(output_folder_path: str):
    full_list_of_posts = []

    for channel in telegram_channels_to_parse:
        full_list_of_posts.extend(fetch_posts(channel=channel))

    posts_df = pd.DataFrame(full_list_of_posts)
    posts_df.to_csv(output_folder_path)
    logging.info(f"Posts data saved to: {output_folder_path}")


if __name__ == "__main__":
    parse_posts()
