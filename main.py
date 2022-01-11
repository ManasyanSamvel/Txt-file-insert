def get_user_data():
    l = []
    i= 1
    while i<=4:
        name = input("Insert your name: ")
        surname = input("Insert your surname: ")
        age = input("Insert your age: ")

        while not age.isdigit():
            age = input("insert your age:")

        l.append({
            "id": i,
            "name": name,
            "surname": surname,
            "age": age
        })

        i+=1
    
    return l


def create_data(l):
    f_str = ''

    for d in l:
        f_str += f"{d['id']}. ------------\n"
        f_str += f"Name: {d['name']}\n"
        f_str += f"Surname: {d['surname']}\n"
        f_str += f"Age: {d['age']}\n"

    with open("test.txt", "w", encoding="utf-8") as f:
        f.write(f_str)


create_data(get_user_data())
