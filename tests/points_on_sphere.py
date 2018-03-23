import numpy as np

# https://stackoverflow.com/questions/33976911/generate-a-random-sample-of-points-distributed-on-the-surface-of-a-unit-sphere

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

n = 5000
xi, yi, zi = sample_spherical(n)*10
array_s = np.transpose([xi, yi, zi])
array_r = np.random.rand(n,3)*0.1
array = array_s + array_r
# array = np.random.permutation(array)

np.savetxt("{}x3s.dat".format(n), array)
    
