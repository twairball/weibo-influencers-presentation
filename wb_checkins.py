##
## Pandas script for cleaning weibo social data
## Copyright 2016, Jerry Liu
## MIT LICENSE
##

import pandas as pd
import matplotlib.pyplot as plt

# read data
wb_users = pd.read_csv('weibo_user.csv')

# print stats
followers_counts = wb_users["followers_count"]
print("Followers Count, min = {}, max= {}, mean = {}", followers_counts.min(), followers_counts.max(), followers_counts.mean())


# 547,363 total users // 349,780 females 63.9%
# 308 users with more than 100,000 followers // 120 females 38.9% 
# 587 users with more than 50k followers // 220 females 37.4%
super_influencers = wb_users[followers_counts >= 50000]
print("Influencers wth 50k followers: {}", super_influencers.shape[0])

# 3825 users with more than 10k followers // 1639 females 42.8% 
influencers = wb_users[followers_counts >= 10000]
print("Influencers wth 10k followers: {}", influencers.shape[0])

# 543,538 users with < 10k followers
plebs = wb_users[followers_counts < 10000]
print("plubs with < 10k followers: {}", plebs.shape[0])

# write to csv
super_influencers.to_csv('supers.csv')
influencers.to_csv('influencers.csv')
plebs.to_csv('plebs.csv')


# status counts
# 87 influencers < 500 status_count
# 169 influencers < 1000 status_count
# 55 influencers > 10,000 status_count
# 3 influencers > 30,000 status_count
# median: 2056
# mean: 3856

##
## status checkins
##
# 520,000 checkins
# min created_at: 
# max created_at: 
# 
wb_checkins = pd.read_csv('weibo_status.csv')
wb_checkins["influencer"] = False
wb_checkins["super"] = False
wb_checkins["pleb"] = False

# check if belongs to influencers
isInfluencer = wb_checkins["weibo_user_id"].isin(influencers["weibo_user_id"])
wb_checkins.loc[isInfluencer, "influencer"] = True

isSuper = wb_checkins["weibo_user_id"].isin(super_influencers["weibo_user_id"])
wb_checkins.loc[isSuper, "super"] = True

isPleb = wb_checkins["weibo_user_id"].isin(plebs["weibo_user_id"])
wb_checkins.loc[isPleb, "pleb"] = True

# super influencer (50k followers) checkins
# min created_at: 2012-12-10 10:42:10+08
# max created_at: 2013-01-07 08:37:20+08
# count: 499
# unique locations: 366 ==> 73.3% unique
super_checkins = wb_checkins[wb_checkins["super"] == True]

# influencer (10k followers) checkins
# min created_at: 2012-11-28 16:17:55+08
# max created_at: 2013-01-07 09:05:44+08
# count: 4497
# unique locations: 2509 ==> 55.8% unique
influencer_checkins = wb_checkins[wb_checkins["influencer"] == True]

# plebs (<10k followers) checkins
# min created_at: 2012-11-18 19:24:56+08
# max created_at: 2013-01-07 10:08:04+08
# count: 513,959
# unique locations: 54,290 ==> 10.6% unique
pleb_checkins = wb_checkins[wb_checkins["pleb"] == True]


# write to csv
influencer_checkins.to_csv('influencer_checkins.csv')
super_checkins.to_csv('super_checkins.csv')


##
## locations
##
# total locations: 54,672
# locations with super checkins: 366
# locations with influencer checkins: 2507
# locations with pleb checkins: 54,283
wb_locations = pd.read_csv('weibo_location.csv')
wb_locations["super_checkins"] = 0
wb_locations["influencer_checkins"] = 0
wb_locations["pleb_checkins"] = 0

# total locations: 54,672
super_checkin_location_freq = super_checkins["weibo_location_id"].value_counts()
influencer_checkin_location_freq = influencer_checkins["weibo_location_id"].value_counts()
pleb_checkin_location_freq =pleb_checkins["weibo_location_id"].value_counts()

wb_locations["super_checkins"] = super_checkin_location_freq
wb_locations["influencer_checkins"] = influencer_checkin_location_freq
wb_locations["pleb_checkins"] = pleb_checkin_location_freq

# fill nan
wb_locations["super_checkins"] = wb_locations["super_checkins"].fillna(0)
wb_locations["influencer_checkins"] = wb_locations["influencer_checkins"].fillna(0)
wb_locations["pleb_checkins"] = wb_locations["pleb_checkins"].fillna(0)

# split to 3 user groups
super_locations = wb_locations[wb_locations["super_checkins"] > 0]
influencer_locations = wb_locations[wb_locations["influencer_checkins"] > 0]
pleb_locations = wb_locations[wb_locations["pleb_checkins"] > 0]

# write to csv
super_locations.to_csv('super_locations.csv')
influencer_locations.to_csv('influencer_locations.csv')
pleb_locations.to_csv('pleb_locations.csv')


##
## histogram of locations with multiple influencer checkins
# il = wb_locations[wb_locations["influencer_checkins"] > 1]["influencer_checkins"]
# plt.clf()
# plt.hist(il, bins=20)
# plt.show()


##
##
## add lat/lon/title to checkins

super_checkins["latitude"] = 0
super_checkins["longitude"] = 0
super_checkins["title"] = 0

# map latitude
s_lat = super_checkins.weibo_location_id.map(wb_locations.latitude)
super_checkins.loc[:, "latitude"] = s_lat

# map longitude
s_lon = super_checkins.weibo_location_id.map(wb_locations.longitude)
super_checkins.loc[:, "longitude"] = s_lon

# map location title
s_title = super_checkins.weibo_location_id.map(wb_locations.title)
super_checkins.loc[:, "location_title"] = s_title

# to csv
super_checkins.to_csv('super_checkins.csv')

##
## influencers
##
influencer_checkins["latitude"] = 0
influencer_checkins["longitude"] = 0
influencer_checkins["title"] = 0

# map latitude
s_lat = influencer_checkins.weibo_location_id.map(wb_locations.latitude)
influencer_checkins.loc[:, "latitude"] = s_lat

# map longitude
s_lon = influencer_checkins.weibo_location_id.map(wb_locations.longitude)
influencer_checkins.loc[:, "longitude"] = s_lon

# map location title
s_title = influencer_checkins.weibo_location_id.map(wb_locations.title)
influencer_checkins.loc[:, "location_title"] = s_title

# to csv
influencer_checkins.to_csv('influencer_checkins.csv')



##
## plebs
## 
pleb_checkins["latitude"] = 0
pleb_checkins["longitude"] = 0
pleb_checkins["title"] = 0

# map latitude
s_lat = pleb_checkins.weibo_location_id.map(wb_locations.latitude)
pleb_checkins.loc[:, "latitude"] = s_lat

# map longitude
s_lon = pleb_checkins.weibo_location_id.map(wb_locations.longitude)
pleb_checkins.loc[:, "longitude"] = s_lon

# map location title
s_title = pleb_checkins.weibo_location_id.map(wb_locations.title)
pleb_checkins.loc[:, "location_title"] = s_title

# to csv
pleb_checkins.to_csv('pleb_checkins.csv')





