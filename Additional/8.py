
# The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics.
# But today, Spain won 2 more gold medals.
# Update golds to reflect this information. Do not hard code this.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

# your code here to make changes to the golds dictionary.
if "Spain" in golds:
    golds["Spain"] = golds["Spain"] + 2
else:
    golds["Spain"] = 2

print golds