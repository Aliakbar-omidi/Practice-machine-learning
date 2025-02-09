

data = {"Name": "Ali",
        "Age": 24,
        "country": "iran",
        "city": "tehran"
}


# write data
file = open("data.txt", "wt")
file.write(f"{data}")

file.close()


# read data
read_file = open("data.txt", "rt")
read_data = read_file.read()

read_file.close()
print(read_data)
