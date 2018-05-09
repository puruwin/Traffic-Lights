# Copied from CodeWars solution ;)

def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

x=update_light("red")
print(x)