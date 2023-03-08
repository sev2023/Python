print("Start!!!")
from importlib import reload

with open("London.txt") as f:
    ff = f.read()
       
c = ff.split("=")[1]
cc = eval(c)
for i in cc.items():print(i)
print("Enter device name:", end="")
try:
    inp = input()
    print(f"location: { cc[inp]['location'] }, "
            f" vendor: { cc[inp]['vendor'] },"
            f" model: { cc[inp]['model'] },"
            f" ios: { cc[inp]['ios'] },"
            f" ip: { cc[inp]['ip'] },")
except:
    print("WRONG INPUT")


