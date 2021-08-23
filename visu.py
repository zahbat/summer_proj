################################################################################################
################################################################################################
#############  This script allows you to plot the evolution of the tracer  #####################
############# through time on the dispersion cube experimentation on each  #####################
#############                     point of the mesh.                       #####################
################################################################################################
################################################################################################



import pandas as pd
import sim_data_4_sc as sd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



def viz(coord):
    
    """
    Creates a 3D visualization for a given output of a RNN. Has to be 2D.
    """
    
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


    #coord = np.array(pd.read_csv("out.csv", header=None))

    #X1, X2, Y1, Y2, sc, acp = sd.build_mtm(split=0, pca=True, pca_details=False, shuffle=False)

    #X2 = sc.inverse_transform(acp.inverse_transform(X2))

    #print(X2[:,0,:].shape)

    #coord = X2[:,0,:]



    X = np.array(range(coord.shape[0]))
    Y = np.array(range(coord.shape[1]))

    X,Y = np.meshgrid(X,Y)

    #print(coord.shape)
    #print(X.shape, Y.shape)


    surf = ax.plot_surface(X.T, Y.T, coord, cmap=cm.coolwarm)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('Timestamps')
    ax.set_ylabel('Mesh points')

    plt.show()
    return


resraw = np.array(pd.read_csv("out.csv", header=None))
#restem = np.loadtxt("restemoin.csv")
resfirsttry = np.loadtxt("resfirsttry.csv")
resphy = np.loadtxt("resfirsttryphy75rate0001.csv")
onebldon3bld = np.loadtxt("1bldon3blddata.csv")
threebldononebld = np.loadtxt("3bldon1blddata.csv")
resdata = np.loadtxt("truedata.csv")

##########
X1, X2, Y1, Y2, sc, acp = sd.build_mtm(split=0, pca=True, pca_details=False, shuffle=False)
X2 = sc.inverse_transform(acp.inverse_transform(X2))
respca = X2[:,0,:]
##########

#out=np.loadtxt("out_3bldngs.csv")
import build_3bldngs as b3
X1, X2, Y1, Y2, sc, acp = b3.build_mtm(split=0,pca=True,shuffle=False)
X2 = sc.inverse_transform(acp.inverse_transform(X2))
pca3bld=X2[:,0,:]


viz(np.divide(respca-resraw[:319],resraw[:319])/200)
