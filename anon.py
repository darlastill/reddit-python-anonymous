import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

c=pd.read_csv("SUBREDDITPOSTCOMMENTFILE.csv")
a=pd.read_csv("SUBREDDITPOSTAUTHORFILE.csv")
aut=pd.read_csv("ALLOFREDDITAUTHORFILE.csv")
aut=aut[aut.author != '[deleted]']
aut.drop( aut[ aut['subreddit'] == "SUBREDDITOFSTUDY" ].index , inplace=True)

commenters=[]
commenters=list(c['author'])
posters=list(a['author'])
allOPs=list(aut['author'])
x=np.array(aut['author'])
y=np.array(aut['subreddit'])
xy=np.column_stack((x,y))
a["commenter"] = np.where(a["author"].isin(commenters), "Comments", "Only Posts")
a["commenter_b"] = np.where(a["author"].isin(commenters), "1", "0")
c["onlycomments"] = np.where(c["author"].isin(posters), "Post_Comments", "Only Comments")
c["onlycomm_b"] = np.where(c["author"].isin(posters), "0", "1")

c['comments'] = c['author'].groupby(c['ID']).transform('sum')
a['trueanon'] = np.where(a["author"].isin(allOPs),"Not Anon", "Anonymous")
a['trueanon_b']= np.where(a["author"].isin(allOPs),"0", "1")

a.to_csv('NEWSUBREDDITPOSTFILE.csv', encoding='utf-8')
c.to_csv('NEWSUBREDDITPOSTCOMMENTFILE.csv', encoding='utf-8')