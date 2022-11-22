# Emily Pearson
# CSCI 102 - Section A
# References: n/a
# Time: 10 mins

# ask for input
print("Enter the Tweet or Message abbreviation to decode.")
abbrev = input("TWEET> ")
tweet = "hi"

# expand abbreviation
if abbrev == "BTW":
  tweet = "By the way"
elif abbrev == "DM":
  tweet = "Direct message"
elif abbrev == "AFAIK":
  tweet = "As far as I know"
else:
  tweet = "I don't know"

# print abbreviation
print("The decoded abbreviation is:")
print("OUTPUT",abbrev,"=",tweet)