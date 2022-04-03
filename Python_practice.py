

# score = int(input("Enter the Temperature : "))

# if score >= 90:
#     print ("A")
# elif score >=80:
#     print ("B")
# elif  score >= 70:
#     print ("C")
# else :    
#     print ("D")



# counties =["Arapahoe","Denver","Jefferson"]
# print(counties)

# Alternative :

# for i in range(len(counties)) :
#     print(counties[i])


# Finding item using in or not in :
# if "Denver" in counties :
#     print("yes")
# else :
#     print("no")


# While loop :
# x = 4   
# while x<=5:
#     print(x)
#     x=x+1

# count = 5
# while count <6:
#     print("Yes")

# numbers = [ 1,2,3,4]
# for num in range(5):
#     print(num)


#  Get the  keys of  a dictionary :

# counties_dict = {"Arapahoe" : 1000, "Denver" : 2000, "Jefferson" : 3000 }
# for county in counties_dict:
#     print(county)

### Alternative
# counties_dict = {"Arapahoe" : 1000, "Denver" : 2000, "Jefferson" : 3000 }
# for county in counties_dict.keys():
#     print(county)

# Get the  value of dictionary :

# counties_dict = {"Arapahoe" : 1000, "Denver" : 2000, "Jefferson" : 3000 }
# for county in counties_dict :
#     # [ Alternative :
#     # for county in counties_dict:
#     # print(counties_dict.get(county)) ]
    
#     print(counties_dict[county])


# # Get the Key-Value Pairs of a Dictionary :
# counties_dict = {"Arapahoe" : 1000, "Denver" : 2000, "Jefferson" : 3000 }

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} register voters.")


# Get Each Dictionary in a List of Dictionaries :
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
    
# # Get the Values from a list of dictionary using range:
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for i in range(len(voting_data)):
#        print(voting_data[i]["county"])


# # # Get the Values after keys from a List of Dictionaries:
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     for value in county_dict.values():
#        print(value)


# Get the values from a list dictionary :
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#        print(county_dict ["registered_voters"])

# Get the 1st values from each dictionay of a list dictionary :
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict["county"])    


# ***Print formatting:**  
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():

#     print(f" {county} county has  {voters:,} registered voters")


# # Print different list from the list of dictionary
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# b=voting_data[0]['county']
# c=voting_data[1]['county']
# d=voting_data[2]['county']
# new_list1=[b,c,d]
# e=voting_data[0]['registered_voters']
# f=voting_data[1]['registered_voters']
# g=voting_data[2]['registered_voters']
# new_list2=[e,f,g]
# print(new_list1, new_list2)
# # Result : ['Arapahoe', 'Denver', 'Jefferson'] [422829, 463353, 432438]


# # Print each county and registered voter from the dictionary
# # Unsonlved : Print each county and registered voter from the dictionary (unsolved)
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# count_dict = voting_data[0:2]["county"]
# voters = voting_data[0:2]["registered_voters"]
# print(county_dict)
# for county_dict, voters in voting_data.items():
#     print(county_dict['county'],voters['registered_voters'])