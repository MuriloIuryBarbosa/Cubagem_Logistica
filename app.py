import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rectpack import newPacker
import numpy as np

rectangles = [(1.20, 2.28), (0.50, 0.50)]
bins = [(2.72, 14), (2.72, 14)]

packer = newPacker(rotation = True)

# Add the rectangles to packing queue
for r in rectangles:
	packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in bins:
	packer.add_bin(*b)

# Start packing
packer.pack()

for index, abin in enumerate(packer):
  bw, bh  = abin.width, abin.height
  print('bin', bw, bh, "nr of rectangles in bin", len(abin))
  fig1 = plt.figure()
  ax = fig1.add_subplot(111, aspect='equal')
  for rect in abin:
    x, y, w, h = rect.x, rect.y, rect.width, rect.height
    plt.axis([0,bw,0,bh])
    print('rectangle', w,h)
    ax.add_patch(
        patches.Rectangle(
            (x, y),  # (x,y)
            w,          # width
            h,          # height
            facecolor="#964B00",
            edgecolor="black",
            linewidth=1.5
        )
    )


    #renderização 3D
    #fig = plt.figure(figsize=(8, 3))
    #ax1 = fig.add_subplot(121, projection='3d')

    #_x = np.arange(14)
    #_y = np.arange(2.72)
    #_xx, _yy = np.meshgrid(_x, _y)
    #x, y = _xx.ravel(), _yy.ravel()

    #top = x + y
    #bottom = np.zeros_like(top)
    #width = depth = 1

    #ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
    #ax1.set_title('Shaded')


  #fig.savefig("rect_%(index)s.png" % locals(), dpi=144, bbox_inches='tight')
  plt.show()