# load pytraj
import pytraj as pt
import numpy as np

# load mdtraj
import mdtraj as md
from mdtraj.testing import get_fn
# load h5 file 
#filename, topology_name = get_fn('tfit_10.xtc'), get_fn('prot0.pdb')
m_traj = md.load('tfit_10.xtc', top='prot0.pdb')
m_traj
traj = pt.Trajectory(xyz=m_traj.xyz.astype('f8'), top='prot0.pdb')
traj

# creat N-H vector pairs

# select H (backbone) indices with given residue number (from previous step)
#H_mask = ':' + ','.join(str(i) for i in resnums) + '@H'
#print('H_mask: ', H_mask)
h_indices = pt.select_atoms(traj.top, '@H')

# select N (backbone) indices
n_indices = h_indices - 1

# create pairs
nh_pairs = list(zip(n_indices, h_indices))
nh_pairs[:3]

# do calculation
s2 = pt.nh_order_parameters(traj, nh_pairs, tcorr=52801.0, tstep=1.0)
st20 = pt.nh_order_parameters(traj, nh_pairs, tcorr=20000.0, tstep=1.0)
st10 = pt.nh_order_parameters(traj, nh_pairs, tcorr=10000.0, tstep=1.0)
st5 = pt.nh_order_parameters(traj, nh_pairs, tcorr=5000.0, tstep=1.0)

# plot
#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'  # high resolution
import matplotlib
#matplotlib.rcParams['savefig.dpi'] = 1.5 * matplotlib.rcParams['savefig.dpi'] # larger image
from matplotlib import pyplot as plt

plt.plot(s2, 'red', label='T3P-Full')
plt.plot(st20, 'blue', label='T3P-20ns')
plt.plot(st10, 'green', label='T3P-10ns')
plt.plot(st5, 'magenta', label='T3P-5ns')

plt.ylim([0., 1.])
plt.ylabel('S2')
plt.xlabel('Residue')
plt.legend(loc=4)
plt.xticks(np.arange(1, 331, 20.0))
plt.grid(True)
plt.savefig("orderparameter.eps", dpi=600)
