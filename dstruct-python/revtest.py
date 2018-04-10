class Reverse:
    def rever_string(self, string):
        reversed_string = string[::-1]
        return reversed_string

R1 = Reverse()
my_string = "Akshatha"
rev_str = R1.rever_string(my_string)
print(rev_str)

