
print("London Elections\n")
users = {}
count = 0
answer = int(input("How many users to vote ?"))
for i in range(answer):
    name = input("enter name:")
    id = input("enter id:")
    city = input("enter city:")
    year = int(input("enter year:"))
    print("-" * 50)

    age = 2023 - year
    allow = 0

    info = {"name": name, "id": id, "city": city, "year": year, "allow": allow}
    users[i] = info

    if age < 18:
        info["allow"] = 0
    else:
        city = info.get("city")
        if city == "london" or city == "westminster":
            info["allow"] = 1
            count += 1
        else:
            info["allow"] = 2

print(users)

print("Number of voters :" + str(count) + "\n")


def vote():

    candidate = ["Obama", "Trump", "Biden"]
    print(candidate)

    num_vote = int(input("How many votes do you register?"))
    number = 0
    vote = dict()
    registration =[]
    while number != num_vote:
        candidates = input("enter the candidates:")
        number += 1
        registration.append(candidates)

    for i in registration:
       if i in vote:
           vote[i] += 1
       else:
           vote[i] = 1

    for i in sorted(vote):
        print(i, vote[i])

vote()