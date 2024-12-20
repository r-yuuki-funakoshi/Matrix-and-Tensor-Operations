import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

'''Definition

Let V be a function such that

V : α -> W | "function" V takes input from vector α(x, y) and any output must belong in the new vector space W
V is predetermined and it must satisfy the following:

    :V(α + β) = V(α) + V(β)
    :V(cα) = c*V(α)
    :cV(α + β) = cV(α) + cV(β)

And any vector from V must be generatable from basis vector of V, and any vector that is produced onto W must be generatable from basis vector of W.
'''

""" STEP 1 : create V(x, y) grid """
# Definition of colorizer
def colorizer(x, y):
    r = min(1, 1 - y / 4)
    g = min(1, 1 + y / 4)
    b = 1 / 4 + x / 16
    return (r, g, b)

# Create grid
xvals = np.linspace(-4, 4, 9)
yvals = np.linspace(-4, 4, 9)
xygrid = np.array([[x, y] for x in xvals for y in yvals]).T  # Transposed for proper plotting

'''This will create a matrix (or vector space of x, y)

[x,   [-4, -3, -2, -1, 0, 1, 2, 3, 4
 y] =  -4, -3, -2, -1, 0, 1, 2, 3, 4]'''

# Map grid coordinates to colors
colors = [colorizer(x, y) for x, y in zip(xygrid[0], xygrid[1])]

# Plot grid
plt.figure(figsize=(4, 4), facecolor="w")
plt.scatter(xygrid[0], xygrid[1], s=36, c=colors, edgecolors="none")
plt.grid(True)
plt.axis("equal")
plt.title("Original grid in X(x, y) space")
plt.show()


""" STEP 2 : operate linear transformation and plot W(u, v) """
# Linear transformation matrix
a = np.array([[1, 0],
              [0, -1]])
print("Function V: ")
print(a)

''' examples
theta = np.pi/3 # 60 degree clockwise rotation
a = np.column_stack([[np.cos(theta), np.sin(theta)],
                     [-np.sin(theta), np.cos(theta)]])
print(a) '''

# Transform grid
uvgrid = np.dot(a, xygrid)

# Plot transformed grid
plt.figure(figsize=(4, 4), facecolor="w")
plt.scatter(uvgrid[0], uvgrid[1], s=36, c=colors, edgecolors="none")
plt.grid(True)
plt.axis("equal")
plt.title("Transformed grid in W(u, v) space")
plt.show()

""" STEP 3 : stepwise transformation for animation """

# Stepwise transformation
def stepwise_transform(a, points, nsteps=30):
    transgrid = np.zeros((nsteps + 1,) + points.shape)
    for j in range(nsteps + 1):
        intermediate = np.eye(2) + j / nsteps * (a - np.eye(2))
        transgrid[j] = np.dot(intermediate, points)
    return transgrid

steps = 30
transform = stepwise_transform(a, xygrid, nsteps=steps)

# Animation frames
def make_plots(transarray, colors, outdir="tmp", figuresize=(4, 4), figuredpi=150):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    maxval = np.abs(transarray).max()
    frames = []
    
    for j in range(transarray.shape[0]):
        plt.figure(figsize=figuresize, facecolor="w")
        plt.scatter(transarray[j, 0], transarray[j, 1], s=36, c=colors, edgecolors="none")
        plt.xlim(1.1 * np.array([-maxval, maxval]))
        plt.ylim(1.1 * np.array([-maxval, maxval]))
        plt.grid(True)
        plt.title(f"Step {j + 1}/{transarray.shape[0]}")
        
        frame_path = os.path.join(outdir, f"frame-{j + 1:03d}.png")
        plt.savefig(frame_path, dpi=figuredpi)
        frames.append(frame_path)
        plt.close()
    
    return frames

""" STEP 4 : generate frames for animation and gif """

# Generate frames for animation
frames = make_plots(transform, colors)

# Convert frames to GIF
gif_path = os.path.abspath("animation.gif")  # Use absolute path for clarity
with Image.open(frames[0]) as img:
    img.save(
        gif_path, save_all=True, append_images=[Image.open(f) for f in frames[1:]], duration=100, loop=0
    )

# Check if GIF is created successfully
if os.path.exists(gif_path):
    print(f"GIF saved at: {gif_path}")
else:
    raise FileNotFoundError("GIF file was not created!")

# Display the GIF
try:
    from IPython.display import Image as IPImage, display
    display(IPImage(gif_path))
except Exception as e:
    print(f"Could not display GIF: {e}")
    print(f"Please open the GIF manually at: {gif_path}")


