#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
from ytmusicapi import YTMusic

yt_video_base_url="https://music.youtube.com/watch?v="
filename=os.getenv("HOME")+"/Downloads/track"
music_directory="/home/coder/Music/Assorted"

class Yt_info:
    def __init__(self, title, uploader, link):
        self.title=title
        self.uploader=uploader
        self.link=link

def load_track_file():
    if(not(os.path.isfile(filename+".csv"))):
        files=os.listdir(music_directory)
        with open(filename+".csv", 'w') as track_file:
            # writer = csv.writer(file)
            for file in files:
                track_file.write(file+",0"+"\n")

def print_yt_infos(query):
    print()
    print()
    print(query)
    print()
    yt_infos=get_yt_info(query)
    for yt_info in yt_infos:
        print_yt_info(yt_info)

def print_yt_info(yt_info):
    print(yt_info.link,"\t", yt_info.uploader,"\t", yt_info.title,end=' ')
    print()

def get_yt_info(query):
    yt_response=hit_yt(query)
    yt_infos=[]
    # extract results from response
    # for item in yt_response.get('items',[]):
    #     item_title=item.get('snippet').get('title')
    #     item_uploader=item.get('snippet').get('channelTitle')
    #     item_link=create_yt_video_link(item.get('id').get('videoId'))
    #     yt_info=Yt_info(item_title, item_uploader, item_link)
    #     yt_infos.append(yt_info)
    return yt_infos

def create_yt_video_link(video_id):
    return yt_video_base_url+video_id

def hit_yt(query):
    # call ytmusicapi with query, 'songs' and ?max_results
    # return response    
    pass

def get_top_filename():
    top_filename=None
    with open(filename+".csv") as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if row[1]=="0":
                top_filename=row[0].rstrip(".mp3")
                break
    return top_filename

def update_track_file(query):
    with open(filename+".csv", 'r') as file:
        lines=file.readlines()
        updated_lines=[]
        for line in lines:
            if(line[:-7]==query):
                line=line[:-2]+"1\n"    
            updated_lines.append(line)

        with open(filename+"_temp"+".csv", "w") as track_file:
            track_file.writelines(updated_lines)

    os.remove(filename+".csv")
    os.rename(filename+"_temp"+".csv", filename+".csv")


def main():
    load_track_file()
    
    query=get_top_filename()

    while not(query is None):
        print_yt_infos(query)
        proceed=input("Proceed? [y/n]: ")
        if(proceed=="y"):
            update_track_file(query)
            query=get_top_filename()
        else:
            break
    
    if(query is None):
        print("Phew! It's all done ✌")




if __name__ == "__main__":
    main()