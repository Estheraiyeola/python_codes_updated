# input_ = []
# for i in range(3):
#     user_input = input("")
# input_[i] = int(input_[0])
# int(input_[2])
# print(input_)


entry = []
for x in range(3):
    entry[x] = int(input(""))
    if x == 1:
        entry[x] = input("")
print(entry)