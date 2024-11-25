from TikTokApi import TikTokApi
import json

def get_trending_hashtags():
    api = TikTokApi()
    hashtags_list = []

    for video in api.trending.videos(get_all=True):
        video_data = video.as_dict()
        hashtags = video_data.get('hashtags', [])
        for tag in hashtags:
            hashtags_list.append(tag['name'])

    return json.dumps(hashtags_list)
