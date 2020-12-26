class Sample2:
    def __init__(self, value):
        self.value = value

s1 = Sample2('AAA')
s2 = Sample2('BBB')
print(s1.value)  # AAA
print(s2.value)  # BBB
s1.value = 'CCC'
print(s1.value)  # CCC
print(s2.value)  # BBB