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
# Transformation to rotated space
def rotation_operation(x, y):
    theta = np.pi / 2
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)

    return np.array([x_rot, y_rot])

# Transform xygrid to polar coordinates
polar_grid = np.array([rotation_operation(x, y) for x, y in zip(xygrid[0], xygrid[1])]).T

# Plot transformed grid (polar coordinates)
plt.figure(figsize=(4, 4), facecolor="w")
plt.scatter(polar_grid[0], polar_grid[1], s=36, c=colors, edgecolors="none")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Transformed grid (rotated) (x, y)")
plt.show()

""" STEP 3 : stepwise transformation for animation """

# Stepwise transformation from Cartesian to Polar
def stepwise_rotation_operation(points, nsteps=30):
    transgrid = np.zeros((nsteps + 1, 2, points.shape[1]))
    for j in range(nsteps + 1):
        alpha = j / nsteps
        theta = alpha * np.pi / 2 # Interpolate between 0 and desired degrees (0 <= theta <= 360)
        for i, (x, y) in enumerate(zip(points[0], points[1])):
            x_rot = x * np.cos(theta) - y * np.sin(theta)
            y_rot = x * np.sin(theta) + y * np.cos(theta)
            transgrid[j, :, i] = [x_rot, y_rot]
    return transgrid

steps = 30
transform = stepwise_rotation_operation(xygrid, nsteps=steps)

# Animation frames
def make_rotation(transarray, colors, outdir="tmp", figuresize=(4, 4), figuredpi=150):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    maxval = transarray[:, 0, :].max()  # Correct usage of max()
    frames = []

    for j in range(transarray.shape[0]):
        plt.figure(figsize=figuresize, facecolor="w")
        plt.scatter(transarray[j, 0], transarray[j, 1], s=36, c=colors, edgecolors="none")
        plt.xlim([-1.1 * maxval, 1.1 * maxval])  # Update limits for symmetry
        plt.ylim([-1.1 * maxval, 1.1 * maxval])
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Step {j + 1}/{transarray.shape[0]}")

        frame_path = os.path.join(outdir, f"frame-{j + 1:03d}.png")
        plt.savefig(frame_path, dpi=figuredpi)
        frames.append(frame_path)
        plt.close()

    return frames


""" STEP 4 : generate frames for animation and gif """

# Generate frames for animation
frames = make_rotation(transform, colors)

# Convert frames to GIF
gif_path = os.path.abspath("rotation_animation.gif")
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
