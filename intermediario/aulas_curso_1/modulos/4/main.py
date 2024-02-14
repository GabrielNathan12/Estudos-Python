import importlib
import main_m
print(main_m.var)


for i in range(10):
    importlib.reload(main_m)
    print(i)