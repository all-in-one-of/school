import numpy as np

from skimage import data
from skimage import draw
from skimage.transform import probabilistic_hough_line

from skimage.viewer import ImageViewer
from skimage.viewer.widgets import Slider
from skimage.viewer.plugins.overlayplugin import OverlayPlugin
from skimage.viewer.plugins.canny import CannyPlugin


def line_image(shape, lines):
    image = np.zeros(shape, dtype=bool)
    for end_points in lines:
        end_points = np.asarray(end_points)[:, ::-1]
        image[draw.line(*np.ravel(end_points))] = 1
    return image


def hough_lines(image, *args, **kwargs):
    lines = probabilistic_hough_line(image, threshold=0.5, *args, **kwargs)
    image = line_image(image.shape, lines)
    return image


image = data.camera()
canny_viewer = ImageViewer(image)
canny_plugin = CannyPlugin()
canny_viewer += canny_plugin

hough_plugin = OverlayPlugin(image_filter=hough_lines)
hough_plugin += Slider('line length', 0, 100, value=100, update_on='move')
hough_plugin += Slider('line gap', 0, 20, value=0, update_on='move')

hough_viewer = ImageViewer(canny_plugin)
hough_viewer += hough_plugin

canny_viewer.show()
