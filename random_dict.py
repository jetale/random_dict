import random
from collections import MutableMapping





class RandomDict(MutableMapping):


    def __init__(self):

        self.main_dict = {}
        self.len_counter = 0
        self.key_list = []
        self.key_dict = {}



    def __setitem__(self, key, value):


        if key not in self.main_dict:
            self.len_counter += 1
            self.key_list.append(key)
            self.key_dict[key] = len(self.key_list) - 1

        self.main_dict[key] = value



    def __delitem__(self, key):

        if key in self.main_dict:

            key_index = self.key_dict[key]
            last_key = self.key_list[-1]

            self.key_list[-1], self.key_list[key_index] = self.key_list[key_index], self.key_list[-1]

            self.key_list.pop()

            self.key_dict[last_key] = key_index

            del self.main_dict[key]

            self.len_counter -= 1

        else:
            raise ValueError


    def __getitem__(self, key):

        if key in self.main_dict:
            return self.main_dict[key]
        else:
            raise KeyError


    def __iter__(self):
        return iter(self.main_dict)


    def __len__(self):

        return self.len_counter



    def get_random_key(self):

        random_index = random.randint(0, len(self.key_list)-1)

        return self.key_list[random_index]


    def view(self):
        print(self.main_dict)



test_dict = RandomDict()

test_dict.__setitem__(2, "Hello")
test_dict.view()
test_dict.__setitem__(5, "World")
test_dict.view()
test_dict.__setitem__(9, "dhungan")
test_dict.view()
test_dict.__setitem__(10, "pad")
test_dict.view()
test_dict.__setitem__(15, "hag")
test_dict.view()
test_dict.__setitem__(19, "nunni")
test_dict.view()
test_dict.__delitem__(9)

test_dict[129] = "bhampak"

for i in range(20):
    print(test_dict.get_random_key())

print(test_dict.key_list)
test_dict.view()