class Demo:
    def __init__(self):
        self.name = "Public"
        self._role = "Protected"
        self.__salary = 50000

d = Demo()

print(d.name)        # ✅ Public
print(d._role)       # ✅ Protected (use with caution)
# print(d.__salary)  # ❌ Private - will raise error
print(d._Demo__salary)  # ✅ Name mangling to access private
