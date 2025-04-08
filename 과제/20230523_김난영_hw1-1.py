import numpy as np
a = np.zeros(3, dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S10')])
a[0] = (0.5, 2, b'a')
a[1] = (1.0, 4, b'aa')
a[2] = (1.5, 6, b'aaa')
for i in range(3, 13):
    new = np.array([(a[i-1][0]+0.5, a[i-1][1]+2, a[i-1][2]+b'a')], dtype=a.dtype)
    a = np.concatenate((a, new))
print(a)

