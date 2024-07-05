import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np


employee_names = ['Harish', 'Bob', 'Charlie', 'Shami', 'Nehal']
work_hours = [45, 60, 55, 70, 50]

def create_gradient_background(width, height):
    image = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(image)

    start_color = (0, 128, 255)  
    end_color = (0, 255, 128)   

    for i in range(height):
        ratio = i / height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    return image

width, height = 800, 600
gradient_image = create_gradient_background(width, height)
gradient_image.save("gradient_background.png")

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(employee_names, work_hours, color='skyblue')

ax.set_xlabel('Employees')
ax.set_ylabel('Work Hours')
ax.set_title('Employee Work Hours')
ax.set_ylim(0, max(work_hours) + 10)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

bg_image = plt.imread("gradient_background.png")
plt.imshow(bg_image, aspect='auto', extent=[-0.5, len(employee_names)-0.5, 0, max(work_hours) + 10], zorder=-1)

ax.grid(False)
ax.set_frame_on(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Show the plot
plt.show()
