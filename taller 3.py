x = [True, True, True, True, False, False, False, False]
y = [True, True, False, False, True, True, False, False]
z = [True, False, True, False, True, False, True, False]


print("Ley asociativa\nx\t y\t z\t( x or y) or z\t( x and y) and z ")

for i in range(len(x)):
    x_and_y = (x[i] or y[i]) or z[i]
    x_or_y = x[i] and (y[i] and z[i]) 
    print(f"{x[i]}\t {y[i]}\t {z[i]}\t {x_and_y}\t\t {x_or_y}")

print("Ley conmutativa\nx\t y\tx or y\t x and y")
for i in range(4):
    x_and_y = (x[i] or y[i]) 
    x_or_y = x[i] and y[i]  
    print(f"{x[i]}\t {y[i]}\t {x_and_y}\t\t {x_or_y}")

print("Ley distributiva\nx\t y\t z\tx and(y or z)\t x or(y and z)")
for i in range(len(x)):
    x_and_y = (x[i] and (y[i] or z[i]))
    x_or_y = x[i] or (y[i]  and z[i])
    print(f"{x[i]}\t {y[i]}\t{z[i]}\t {x_and_y}\t\t {x_or_y}")

print("Ley identidad\nx\t x or False\t x and True")
for i in range(4):
    x_and_y = z[i] or False
    x_or_y = z[i] and True
    print(f"{z[i]}\t {x_and_y}\t\t {x_or_y}")
    
print("Ley Complementos\nx\t x or not x\t x and not x")
for i in range(4):
    x_and_y = z[i] or (not z[i])
    x_or_y = z[i] and (not z[i])
    print(f"{z[i]}\t {x_and_y}\t\t {x_or_y}")