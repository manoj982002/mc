import numpy as np

c1 = np.array([1, 1, 1, 1])
c2 = np.array([1, -1, 1, -1])
c3 = np.array([1, 1, -1, -1])
c4 = np.array([1, -1, -1, 1])

# Example data bits (replace these with your actual values)
d1 = 1
d2 = -1
d3 = 1
d4 = -1

r1 = np.multiply(c1, d1)
r2 = np.multiply(c2, d2)
r3 = np.multiply(c3, d3)
r4 = np.multiply(c4, d4)

resultant_channel = r1 + r2 + r3 + r4
print("Resultant Channel:", resultant_channel)

# Example channel selection (1-4)
channel = 2  # Change this to select different channel

if channel == 1:
    rc = c1
elif channel == 2:
    rc = c2
elif channel == 3:
    rc = c3
elif channel == 4:
    rc = c4
else:
    print("Invalid Channel")
    exit()

inner_product = np.multiply(resultant_channel, rc)
print("Inner Product:", inner_product)

res1 = sum(inner_product)
data = res1 / len(inner_product)

print("Data bit that was sent:", data)