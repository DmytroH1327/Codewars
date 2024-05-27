# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H

def abbrev_name(name):
    sp_name = []
    name = name.split()
    for word in name:
        sp_name.append(word[0].upper())
    return ".".join(sp_name)


assert abbrev_name("Sam Harris") == "S.H"
assert abbrev_name("patrick feenan") == "P.F"
assert abbrev_name("Evan C") == "E.C"
assert abbrev_name("P Favuzzi") == "P.F"
assert abbrev_name("David Mendieta") == "D.M"
print("OK")