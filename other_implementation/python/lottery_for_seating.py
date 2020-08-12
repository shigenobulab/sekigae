import sys
import random
import re
from time import sleep
#import pdb; pdb.set_trace()

seats = ("A", "A", "A", "A", "B", "B", "B", "B")
#print(seats)

## Load member list from file
args = sys.argv
member_list_file = args[1]
#print(member_list_file)

members = []
f = open(member_list_file, "r", encoding='utf-8')
for line in f:
# next if -- LATER
    if re.search(r'^#', line):
        continue

    ary = line.rstrip().split("\t")
    name = ary[1]
    members.append(name)

print("# members are being loaded ...")
print(f"# {len(members)} members found")

## Prepare seats and randomize them
seats_shuffled = random.sample(seats, len(seats))
print(seats_shuffled)

if len(members) != len(seats):
    raise ValueError("number of members is different from number of seats")

sleep(2)
print(f"# We have {len(seats)} seats with {len(set(seats))} categories")
print("# Seats are randomized...")
sleep(2)
print("# done")
print("# Let's see your new seats ...")
sleep(2)

## Pairing members and seats
pair = {}
for i, m in enumerate(members):
    pair[m] = seats_shuffled[i]
    print(f"{m} => {pair[m]}")
    sleep(2)

## Display summary
print("")
print("# Summary")
seats_to_members = {}
for mem in pair:
    seat = pair[mem]
    if seat in seats_to_members:
        pass
    else:
        seats_to_members[seat] = []
    
    seats_to_members[seat].append(mem)

for seat in seats_to_members:
    print(f"Category {seat}: ", end='')
    print(", ".join(seats_to_members[seat]))