import pyximport
pyximport.install()
from distutils.errors import CompileError

try:
    from .gudhi_bottleneck import bottleneck_distance
except:
    from gudhi import bottleneck_distance
    print("Using original gudhi bottleneck_distance.")

try:
    from .hera_wasserstein import wasserstein
except:
    def wasserstein(diagram_1, diagram_2, p = 1, delta = 0.01):
        pass
    print("Function wasserstein_distance not available.")
