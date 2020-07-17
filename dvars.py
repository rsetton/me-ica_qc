import nibabel as nib
import numpy as np
from sys import argv, exit



def _interpolate(a, b, fraction):
    """Returns the point at the given fraction between a and b, where
    'fraction' must be between 0 and 1.
    """
    return a + (b - a)*fraction;

def scoreatpercentile(a, per, limit=(), interpolation_method='fraction'):
    """
    This function is grabbed from scipy

    """
    values = np.sort(a, axis=0)
    if limit:
        values = values[(limit[0] <= values) & (values <= limit[1])]

    idx = per /100. * (values.shape[0] - 1)
    if (idx % 1 == 0):
        score = values[int(idx)]
    else:
        if interpolation_method == 'fraction':
            score = _interpolate(values[int(idx)], values[int(idx) + 1],
                                 idx % 1)
        elif interpolation_method == 'lower':
            score = values[np.floor(idx)]
        elif interpolation_method == 'higher':
            score = values[np.ceil(idx)]
        else:
            raise ValueError("interpolation_method can only be 'fraction', " \
                             "'lower' or 'higher'")

    return score

##DVARS based on percent signal change
#Load data
dfn = argv[1]
dv = nib.load(dfn)
if len(argv)==3: muv = nib.load(argv[2])
else: muv = None
nx,ny,nz,nt = dv.get_data().shape
d = dv.get_data().reshape([nx*ny*nz,nt]).T

#Compute mean and mask
if muv!=None:
	mud = muv.get_data()
	if len(mud.shape) == 4:
		mud = mud.reshape([nx*ny*nz,nt]).T
		d_mu = mud.mean(0).reshape([nx*ny*nz])
	elif len(mud.shape) ==3 :  d_mu = mud.reshape([nx*ny*nz])
	else: print "Can't figure out mean dataset dimensions. Goodbye."
	d_beta = d
else:
	d_mu = d.mean(0)
	d_beta = d-d_mu

d_mask = d_mu!=0
d_mask = (d_mu > scoreatpercentile(d_mu[d_mask],3)) & (d_mu < scoreatpercentile(d_mu[d_mask],98) )
dp =   (d_beta[:,d_mask]/d_mu[d_mask])*100
dpdt = np.abs(dp[1:]-dp[0:-1])+0.0000001

#Condition distribution of dp/dt's
dpdt_thr = np.log10(dpdt).mean(0)
dpdt_max = pow(10,scoreatpercentile(dpdt_thr,98))
dpdt_mask = dpdt.mean(0) < dpdt_max

#Threshold differentials with extreme values, compute DVARS
dvars = np.sqrt(np.mean(dpdt[:,dpdt_mask]**2,1))
np.savetxt('%s_dvars.1D' % dfn.split('.nii.gz')[0],dvars)
