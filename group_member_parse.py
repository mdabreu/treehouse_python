## code to parse group names from bands

musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]


# Your code here

g = 0


# code to parse musical groups
for member in musical_groups:
    parse_group = ", ".join(musical_groups[g])
    print(parse_group)
    g = g +1
                     
        
        
# code to parse groups with more than three members
for member in musical_groups:
    if len(musical_groups[g]) == 3:
        parse_group = ", ".join(musical_groups[g])
        print(parse_group)
    g = g +1
    
