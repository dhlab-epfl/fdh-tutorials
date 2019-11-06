# FDH Computer Vision, Deep Learning and CRF Tutorial
Computer Vision, Deep Learning and CRF tutorials for the course Foundation of Digital Humanities (Fall 2019)

To access previous years tutorials you can switch to branch ``v.2018``

## Clone or download the repository 
* Clone : `git clone https://github.com/dhlab-epfl/fdh-tutorials.git`
* or download the zip directly

## Install the environment
* Install Anaconda with Python 3.* : https://www.anaconda.com/download/

### With the command line

* Install from yml file: `conda env create -f environment.yml`
* Activate the environment: `source activate fdh_tutorial_cv_dl`
* Download spacy italian model (other models can be found on [this page](https://spacy.io/usage)) `python -m spacy download it_core_news_sm`
* Start a Jupyter Notebook Server: `jupyter notebook`
* Once you're done with the exercice: `source deactivate`

## Run the notebooks
Through Jupyter, open the notebook files (`.ipynb`) in the different directories of this very repository.

Inside the `computer-vision-deep-learning` folder you will find:
1. Image processing basics: get familiar with the principal concepts in image processing and computer vision (image handling, filters, denoising)
2. Deep learning: Tensorflow basics with MNIST example (single layer network and multilayer network)
3. Applications: 
    * CV: Face detection using Convolutional Neural Networks (CNN)
    * DL: Historical document processing - page and textline detection
    
Inside the `crf`folder you will find a CRF tutorial notebook treating how to use a CRF from annotating to predicting new text.

If you're already familiar with some concepts, feel free to go to the next notebook.


