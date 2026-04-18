#Student ID: 2540830

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

#Part 0 - Student ID Personalization Rules
student_id = 2540830

d1= 3
d2= 0
k = (d1+d2) % 4 + 2 
shift = d1 - d2 
n_points = 20 + d1 
frame_step= d2 + 1 

print("Student ID:", student_id)
print("d1 =", d1)
print("d2 =", d2)
print("k =", k)
print("shift =", shift)
print("n_points =", n_points)
print("frame_step =", frame_step)


# Component A
# Task A1 - 2D Line Plot
x = list(range(1, n_points + 1))
y = [val ** 2 for val in x]

if len(x) == 0 or len(x) != len(y):
    print("Error: Invalid data for Task A1")
else:
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title("Task A1: x vs x²")
    plt.xlabel("x")
    plt.ylabel("y = x²")
    plt.grid(True)
    plt.show()

    input("Press ENTER to continue...")

# Task A2 - Distribution Plot
data_values = list(np.random.normal(loc=50, scale=5, size=40))

print("\nFirst 10 data values:")
print(data_values[:10])

"""
Histogram helps us understand distribution of repeated measurements by 
showing how frequently values occur within ranges
"""

plt.figure(figsize=(8, 5))
plt.hist(data_values, bins=10)
plt.title("Task A2: Distribution of Repeated Measurements")
plt.xlabel("Measured Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

input("Press ENTER to continue...")
# Component B
# Task B1 - Personalized 2D Plot
y2 = [k * val + shift for val in x]

print("First 5 (x, y2) pairs:")
for i in range(5):
    print(f"({x[i]}, {y2[i]})")

plt.figure(figsize=(8, 5))
plt.plot(x, y2, marker='o', linestyle='--')
plt.title(f"Task B1: Student {student_id} | k={k}, shift={shift}")
plt.xlabel("x")
plt.ylabel("y = kx + shift")
plt.grid(True)
plt.show()

input("Press ENTER to continue...")

print("Starting Task B2")
# Task B2 - Personalized 3D Scatter Plot
y_3d = [value + shift for value in x]
z_3d = [k * value for value in x]

print("First 5 (x, y, z) points: ")
for i in range(5):
    print(f"({x[i]}, {y_3d[i]}, {z_3d[i]})")

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y_3d, z_3d)

ax.set_title("Task B2: Personalized 3D Scatter Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()

input("Press ENTER to continue...")
# Task B3 - Personalized Animation
x_anim = list(range(n_points))
y_anim = [k * value + shift for value in x_anim]

fig, ax = plt.subplots()
ax.set_xlim(0, n_points)
ax.set_ylim(min(y_anim) - 2, max(y_anim) + 2)
ax.set_title("Task B3: Line Animation")
ax.set_xlabel("x")
ax.set_ylabel("y")

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    print(f"Animating frame: {frame}")
    x_data = x_anim[:frame:frame_step]
    y_data = y_anim[:frame:frame_step]
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=len(x_anim),
    init_func=init,
    interval=200,
    blit=True
)

plt.show()
