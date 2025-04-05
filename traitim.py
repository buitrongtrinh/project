import matplotlib.pyplot as plt

# Tạo khung vẽ
fig, ax = plt.subplots(figsize=(8, 8))

# Vẽ các đường tròn với đường kính 20, 25, 30 (bán kính = đường kính / 2)
circle1 = plt.Circle((0, 0), 10, edgecolor='red', fill=False, linewidth=2, label='D = 20')
circle2 = plt.Circle((0, 0), 12.5, edgecolor='green', fill=False, linewidth=2, label='D = 25')
circle3 = plt.Circle((0, 0), 15, edgecolor='blue', fill=False, linewidth=2, label='D = 30')

# Vẽ hình vuông cạnh 15 (góc dưới trái tại (-7.5, -7.5) để tâm vuông là (0, 0))
square = plt.Rectangle((-7.5, -7.5), 15, 15, edgecolor='black', fill=False, linewidth=2, label='Square 15')

# Thêm các hình vào khung vẽ
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(square)

# Tùy chỉnh giới hạn trục để bao hết các hình
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Bỏ trục tọa độ
ax.axis('off')

# Thêm chú thích
ax.legend(loc='upper right')

# Hiển thị hình
plt.show()
