
import pickle


x = {
    "a": 1,
    "b": 2,
    "c": [1, 2, 3],
    "d": "text"
}


file = open("binary_data.txt", "wb")


# write binary data
pickle.dump(x, file)

file.close()


# read binary data
read_file = open("binary_data.txt", "rb")

data = pickle.load(read_file)
read_file.close()
print(data)
