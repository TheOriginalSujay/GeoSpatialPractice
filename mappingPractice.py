# credits to http://blog.thehumangeo.com/2014/05/12/drawing-boundaries-in-python/ for the original code
# this is just for familiarizing myself with some geographical border mapping logic

from shapely.ops import cascaded_union, polygonize
from scipy.spatial import Delaunay
import numpy as np
import math

