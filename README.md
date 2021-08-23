# Summer project software archive

First, please unzip all the data repositories, and put all of them in the main repository. out.csv and out_3bldngs.csv are the most important files, as they are necessary to run any of the learning algorithm. The other are used to visualize the results. 

Every file in this repo is my original work, excluding vtktools.py that comes from a libraryattached to the software Fluidity.

Now, let's enumerate quickly each of the Python scripts and notebooks to sum up their content :

• LSTM1.ipynb: it contains the first deep neural network architecture that has been implemented for this project.  It is a One-to-Many purely data driven  architecture. Nevertheless, some preliminary functions for the physics informed architecture had already been added to this file (customloss,runstepsimufrom,andrunsimulation).

• LSTM2.ipynb: this file contains the conversion of the architecture from LSTM1.ipynb to a physics informed neural network.

• LSTMmtm.ipynb:  it was born from the idea that a Many-to-Many architecture could perform better than the previous one. This file implements the data driven version of the architecture.  It was mainly used to compare the performances of the One-to-Many to the Many-to-Many architecture.

• LSTMmtmflu.ipynb:  it contains the conversion of the Many-to-Many algorithm to a physics informed neural network.

• test.ipynb:  this is basically an unstructured file containing a trace of the tests that have been made to get a better understanding of the structure of the different datasets (effect of normalisation, presence of outliers, PCA details...).

• simdata4sc.py:  this  module  contains  all  the build functions  related  to the one building geometry :  one for the One-to-Many architecture,  one for the Many-to-Many architecture and one that can be used for the Many-to-One architecture.  Each of those allows to split the dataset, perform a PCA, display some  details  about  the  PCA,  and  shuffle  in  unison  the  Xs  and  Ys.   There  is a  function  that  also  allows  to  store  the  data  simulated  from  Fluidity  into  a Pandas dataframe without splitting or shuffling anything.

• build3bldngs.py: this file contains basically the same features as simdata4sc.py, except that they apply to the three buildings geometry.

• processxml.py:  this file contains getters and setters for XML-like files. It is  used  essentially  to  change  the .vtu reference  in  a .flml file,  and  to  getinformation about the simulation from the .flml file.

• testdata.py: this file was used to debug and test the first LSTM architecture when the simulation data was not yet available. It splits and preprocesses data from a EEG database from the State University of New York Health Center.

• visu.py:  this file allows to generate the first type of performance visualisation.  It uses functions from the matplotlib and mpltoolkits libraries.

• visupara.py:  this  file  allows  to  put  some  simulation  data  contained  in a Numpy array into a group of .vtu files.  Once the main method has run, the user only has to open the vtu group on Paraview to get a visualisation of the simulated/predicted data.

• vtuclass.py:  this module allows to perform simple modifications on .vtu files and to get useful information from these files.

Further information about the learning architectures and their performances can be found in the final report.
