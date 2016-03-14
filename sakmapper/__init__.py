import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import networkx as nx
from sklearn import manifold, cluster, metrics
from math import sqrt, cos, sin, pi

from .lens import apply_lens
from .network import mapper_graph
