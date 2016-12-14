##
## Pandas script for cleaning weibo social data
## Copyright 2016, Jerry Liu
## MIT LICENSE
##

import pandas as pd
import matplotlib.pyplot as plt


# read super influencer locations
super_locations = pd.read_csv('super_locations.csv')
super_cats = super_locations["category_en_name"]

# filter out unknowns
super_cats = super_cats.fillna("Unknown Classification")
super_cats = super_cats[super_cats != "Unknown Classification"]

# map Buildings, Other, Residences, Company, Bus Station, Building instituitions, Door, 
# Research instituitions to "Location"
locations = ("Buildings", "Other", "Residences", "Company", "Building institutions", 
  "Door", "General location marker", "Self", "Building door", "Industrial park", 
   "Town Square", "Press", "Research institutions", "Well-known enterprises",
   "Real estate class company",
   "E-commerce company",
   "Toll stations", "Driving",
   "Automobile traffic class company",
   "Government organization",
   "Business sevices companies")
isLocation = super_cats.isin(locations)
super_cats.loc[isLocation] = "Location"

# schools
schools = ("Institutions of higher learning",
  "Training institutions", "Vocational and technical schools",
  "Campus Life", "High school", "Nursery", "Primary school")
isSchool = super_cats.isin(schools)
super_cats.loc[isSchool] = "School"

# facilities
facilities = ("Hospital", "Bank", "Airport", "Church", "Taoist temples", "Islam Temple", 
  "ATM", "Bus Station", "Botanical garden",
  "Subway station", "Railway station", "Ports", "Parking lot", "Library",
  "Park Plaza", "Convention Center")
isFacilities = super_cats.isin(facilities)
super_cats.loc[isFacilities] = "Facility"

# map shops
shops = ("Antiques and paintings shop", "Cold store", "Supermarket", "Furniture, building materials market", 
  "Jewelry Crafts", "Convenience store / convenience store", "Market", "Personal care / cosmetics shop",
  "Shopping services", "Children stores", "Auto Repair", "Adult Education", "Telecom business hall",
  "Household electronics stores", "Clothing and shoes leather shop", "Auto Sales", "Sporting goods stores",
  "Bookstore", "Commercial Street",
  "China Petrochemical", "Funeral", "Tickets outlets",
  "Stores",
  "Optical shop",
  "Pet shop")
isShop = super_cats.isin(shops)
super_cats.loc[isShop] = "Shop"

# entertainment
entertainment = ("KTV", "Billiard hall", "Cinema", "Bath massage places", "Beach", "Concert Hall",
  "Beatuty Salons", "Campus Life", "Bar", "Live Entertainment", "Beauty Salons", "Art gallery",
  "Game room", "Culture Sports Company", 
  "Palace of Culture",
  "National Attractions",
  "Leisure venues", "Gallery", "Museum",
  "Chess Room",
  "Theater",
  "Playground",
  "General Attractions",
  "Memorial", "Photo Gallery")
isEnt = super_cats.isin(entertainment)
super_cats.loc[isEnt] = "Entertainment"

# hotels
hotel = ("Five-star hotel", "Hotel", "Hotels, guest houses", "Economy hotel chain", "Four star hotels",
  "Three star hotels", 
  "Travel accommodation",
  "Yunnan-Guizhou dishes",
  "Vacation retreat with")
isHotel = super_cats.isin(hotel)
super_cats.loc[isHotel] = "Hotel"

# sports and fitness
sports = ("Sports", "Park", "Park outdoors", "Golf-related", "Fitness Center", "Gymnasium", "Natatorium",
  "Tobacco shops")
isSport = super_cats.isin(sports)
super_cats.loc[isSport] = "Sports"

# food 
food = ("Food & Drink", "Wester Restaurant", "Café", "Cantonese cuisine", "Hot Pot", "Dessert", "Shanghai cuisine",
  "Japanese", "Features / local flavor restaurant", "Bakery", "Chinese Restaurant", "Zhejiang cuisine", 
  "Other Asian dishes", "Hunan", "Sichuan dishes", "Korean cuisine", "Western Restaurant",
  "Fast-food restaurant",
  "Barbecue", "Taiwanese dishes", "Halal Restaurant", "Tea House", "Foreign Restaurant",
  "Northwest cuisine", "Thai / Vietnamese restaurant products", 
  "Comprehensive Restaurant", "Italian cuisine restaurant", 
  "Dongbei", "Seafood Restaurant",
  "Casual dining",
  "Chinese vegetarian restaurants",
  "Jiangsu cuisine",
  "Indian flavor",
  "French restaurant dishes")
isFood = super_cats.isin(food)
super_cats.loc[isFood] =  "Food"

print("========== super influencers =========")
print(super_cats.value_counts())
print("")

# #
# Food             82
# Location         79
# Facility         28
# Entertainment    24
# Shop             16
# School           13
# Sports           10
# Hotel             4





# read influencer locations
inf_locations = pd.read_csv('influencer_locations.csv')
inf_cats = inf_locations["category_en_name"]

# filter out unknowns
inf_cats = inf_cats.fillna("Unknown Classification")
inf_cats = inf_cats[inf_cats != "Unknown Classification"]

# bucketing
isLocation = inf_cats.isin(locations)
inf_cats.loc[isLocation] = "Location"

isSchool = inf_cats.isin(schools)
inf_cats.loc[isSchool] = "School"

isFacilities = inf_cats.isin(facilities)
inf_cats.loc[isFacilities] = "Facility"

isShop = inf_cats.isin(shops)
inf_cats.loc[isShop] = "Shop"

isEnt = inf_cats.isin(entertainment)
inf_cats.loc[isEnt] = "Entertainment"

isHotel = inf_cats.isin(hotel)
inf_cats.loc[isHotel] = "Hotel"

isSport = inf_cats.isin(sports)
inf_cats.loc[isSport] = "Sports"

isFood = inf_cats.isin(food)
inf_cats.loc[isFood] =  "Food"

##
## Some buckets that influencers goto that super-influencers don't:
##
## Barbecue, Three-star hotels, Game room, Railway station, Auto Repair

print("========== influencers =========")
print(inf_cats.value_counts())
print("")

# Location         545
# Food             526
# Facility         194
# Entertainment    142
# Shop             118
# School            91
# Hotel             62
# Sports            55




# pleb locations
pleb_locations = pd.read_csv('pleb_locations.csv')
p_cats = pleb_locations["category_en_name"]

# filter out unknowns
p_cats = p_cats.fillna("Unknown Classification")
p_cats = p_cats[p_cats != "Unknown Classification"]

# bucketing
isLocation = p_cats.isin(locations)
p_cats.loc[isLocation] = "Location"

isSchool = p_cats.isin(schools)
p_cats.loc[isSchool] = "School"

isFacilities = p_cats.isin(facilities)
p_cats.loc[isFacilities] = "Facility"

isShop = p_cats.isin(shops)
p_cats.loc[isShop] = "Shop"

isEnt = p_cats.isin(entertainment)
p_cats.loc[isEnt] = "Entertainment"

isHotel = p_cats.isin(hotel)
p_cats.loc[isHotel] = "Hotel"

isSport = p_cats.isin(sports)
p_cats.loc[isSport] = "Sports"

isFood = p_cats.isin(food)
p_cats.loc[isFood] =  "Food"

## some buckets that only plebs goto:
##
## Gymanasium, Indoor Swimming Pool Tobacco shops, Chess Room, Jiangsu cuisine, Pet shop

print("========== plebs =========")
print(p_cats.value_counts())
print("")

# Food                                         12481
# Location                                     12355
# Facility                                      4001
# Entertainment                                 2942
# Shop                                          2698
# School                                        1640
# Hotel                                         1338
# Sports                                        1043
