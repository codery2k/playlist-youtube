# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery
import googleapiclient.errors
import csv

api_service_name = "youtube"
api_version = "v3"
developerKey=os.getenv("YOUTUBE_DATA_API_KEY")
yt_video_base_url="https://www.youtube.com/watch?v="
max_results=3
filename="track.csv"
music_directory="/home/coder/Music/Assorted"

class Yt_info:
    def __init__(self, title, uploader, link):
        self.title=title
        self.uploader=uploader
        self.link=link

def load_track_file():
    if(not(os.path.isfile(filename))):
        files=os.listdir(music_directory)
        with open(filename, 'w') as track_file:
            # writer = csv.writer(file)
            for file in files:
                track_file.write(file+",0"+"\n")

def print_yt_infos(query):
    yt_infos=get_yt_info(query)
    for yt_info in yt_infos:
        print_yt_info(yt_info)

def print_yt_info(yt_info):
    print(yt_info.link)
    print(yt_info.uploader)
    print(yt_info.title)
    print()

def get_yt_info(query):
    yt_response=hit_yt(query)
    yt_infos=[]
    for item in yt_response.get('items',[]):
        item_title=item.get('snippet').get('title')
        item_uploader=item.get('snippet').get('channelTitle')
        item_link=create_yt_video_link(item.get('id').get('videoId'))
        yt_info=Yt_info(item_title, item_uploader, item_link)
        yt_infos.append(yt_info)
    return yt_infos

def create_yt_video_link(video_id):
    return yt_video_base_url+video_id

def hit_yt(query):
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developerKey)
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=query,
        type="video"
    )
    response = request.execute()
    return response    

def get_top_filename():
    top_filename=None
    with open(filename) as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if row[1]=="0":
                top_filename=row[0].rstrip(".mp3")
                break
    return top_filename

def update_track_file():
    pass
    # open track_file for reading and temp_file for writing     
    # load all lines from track_file
    # loop through lines to find first occurence where line[1]==0
    # update it so line[1]==1
    # write to temp_file
    # remove track_file
    # rename temp_file to track_file


def main():
    load_track_file()
    
    query=get_top_filename()

    while not(query is None):
        print_yt_infos(query)
        proceed=input("Proceed? [y/n]:")
        if(proceed=="y"):
            update_track_file()
            query=get_top_filename()
        else:
            break
    
    if(query is None):
        print("Phew! It's all done ✌")




if __name__ == "__main__":
    main()