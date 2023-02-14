friends = {'Alice': '01/01/2000', 'Bob': '02/02/2000', 'Charlie': '03/03/2000'}

print("Friend's Birthdays:")
for friend, dob in sorted(friends.items()):
    print(f"{friend}: {dob}")

name = input("Enter a friend's name to check their birthday: ")
if name in friends:
    print(f"{name}'s birthday is on {friends[name]}")
else:
    dob = input(f"{name} not found. Enter their DOB (DD/MM/YYYY): ")
    friends[name] = dob
    print(f"{name}'s birthday added to the list")


print("Friend's Birthdays:")
for friend, dob in sorted(friends.items()):
    print(f"{friend}: {dob}")
