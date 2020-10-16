import pandas as pd
dataset = pd.read_csv("/users/mustafaaliaykon/Downloads/USvideos.csv")

# print(dataset.head(5)) #> first 5 data
dataset = dataset.drop(columns = ["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis = 1)

# print(dataset[dataset["views"].max() == dataset["views"]]["title"].iloc[0]) => most viewed video's title
# print(dataset[dataset["views"].min() == dataset["views"]]["title"].iloc[0]) => min viewed video's title.

# print(dataset.groupby("category_id")["comment_count"].mean()) => groupby category id and mean of the comment count.

# print(dataset["category_id"].value_counts())  => number of videos for each category

# -------------------------------------------------------------------------------

# def baslikuzunlugu(title):
#     return len(title)
    
# dataset["title_length"] = dataset["title"].apply(baslikuzunlugu)       => length of title for every videos
# print(dataset)

#------------------------------------------------------------------

# def ayir(tags):
#     taglist = tags.split("|")
#     return len(taglist)
# dataset["Column 2"] = dataset["tags"].apply(ayir)        => seperating all tags with '|' and showing number of '|' usage.
# print(dataset)
#--------------------------------------------------------------------
# newyoutube = dataset.head()
# def likesAnddislikes(likes,dislikes):
#     likesList = list()
#     dislikesList = list()
#     for key,value in likes.iteritems():
#         likesList.append(value)
#     for key,value in dislikes.iteritems():
#         dislikesList.append(value)
    
#     likeanddislikeratio = list()
#     for like,dislike in zip(likesList,dislikesList): 
#         if like + dislike == 0:                                     => We have ranked videos from highest to lowest like
#             likeanddislikeratio.append(0)
#         else:
#             likeanddislikeratio.append(like/(like + dislike))
#     return likeanddislikeratio
        
# dataset["likes_dislikes"] = likesAnddislikes(dataset["likes"],dataset["dislikes"])
# dataset.sort_values(by = "likes_dislikes",ascending = False,inplace=True)
# print(dataset)
