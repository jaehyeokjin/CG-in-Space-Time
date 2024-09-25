import matplotlib.pyplot as plt

plt.style.use('classic')

# load image
img = plt.imread('simulation_image.png')

# plot image
fig, ax = plt.subplots()
ax.imshow(img)
# Add (a) in corner
ax.text(0.03, 0.90, '(a)', transform=ax.transAxes, fontsize=30)
# Remove axis
ax.axis('off')

plt.savefig('simulation_image_modified.png', dpi=300, bbox_inches='tight')
plt.show()