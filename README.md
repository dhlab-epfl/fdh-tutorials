# FDH Computer Vision and Deep Learning Tutorial
Computer Vision and Deep Learning tutorials for the course Foundation of Digital Humanities (Fall 2018)

## Clone or download the repository 
* Clone : `git clone https://github.com/dhlab-epfl/FDH_Tutorials_CV_DL.git`
* or download the zip directly

## Install the environment
* Install Anaconda with Python 3.* : https://www.anaconda.com/download/

### With the command line

* Install from yml file : `conda env create -f environment.yml`
* Activate the environment : `source activate FDH_tutorial_CV_DL`
* Start a Jupyter Notebook Server : `jupyter notebook`
* Once you're done with the exercice : `source deactivate`

### With the graphical interface

* Open `Anaconda Navigator`
* In `Environments`, use `Import` and select the file `environment.yml` from this repository.
* After the creation and installation of the packages (might take a bit of time), use the arrow next to the name of the newly create environment and click `Open with Jupyter Notebook`.

## Run the notebooks
Through Jupyter, open the notebook files (`.ipynb`) in the different directories of this very repository.

1. Image processing basics : get familiar with the principal concepts in image processing and computer vision (image handling, filters, denoising)
2. Deep learning : Tensorflow basics with MNIST example (single layer network and multilayer network)
3. Computer Vision Application : Face detection and features descriptors using Convolutional Neural Networks (CNN)

If you're already familiar with some concepts, feel free to go to the next notebook.


