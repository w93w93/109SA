import rawpy
import imageio

# path = '/Users/pytsai/RD_project/NTUSA/data/black.CR2'
def img_conv(path):
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess()
    imageio.imsave('image_black77.jpg', rgb)