# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors


def main():

    api_service_name = "youtube"
    api_version = "v3"
    developerKey=os.getenv("YOUTUBE_DATA_API_KEY")

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developerKey)

    request = youtube.search().list(
        part="snippet",
        maxResults=3,
        q="Paani Yuvraj Hans-Topic",
        type="video"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()