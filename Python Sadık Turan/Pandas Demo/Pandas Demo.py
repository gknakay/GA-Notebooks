# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:43:09 2021

@author: Gökhan Akay
"""

import pandas as pd

df = pd.read_csv("GBvideos.csv")
df.head()

drop_cols = ['thumbnail_link','comments_disabled','ratings_disabled',
             'video_error_or_removed','description','trending_date']

df.drop(drop_cols, axis = 1, inplace = True)

df[df.views == df.views.max()][['title','views']]

df.sort_values(by='views', ascending = False).head(10)[['title','views']]

df['title_len'] = df['title'].apply(len)

df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))


df['like_dislike_ratio'] = df['likes']/df['dislikes']
df.sort_values(by='like_dislike_ratio', ascending = False).head(5)['title']
