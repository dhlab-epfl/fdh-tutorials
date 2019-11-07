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
* Activate the environment: `conda activate fdh_tutorial`
* Download spacy italian model (other models can be found on [this page](https://spacy.io/usage)) `python -m spacy download it_core_news_sm`
* (Optional) if you want to run the 3-application/cv-faces notebook, install dlib: ``pip install dlib``
* Start a Jupyter Notebook Server: `jupyter notebook`
* Once you're done with the exercice: `source deactivate`

__Known issues__

* On MacOS the ``sklearn-crfsuite`` might not get correctly installed with conda. 
If you're having an error try installing it (in the ``fdh_tutorial`` environment) with: 
```
    conda install -c conda-forge python-crfsuite
    conda env update -f environment.yml 
```

## Run the notebooks
Through Jupyter, open the notebook files (`.ipynb`) in the different directories of this very repository.

Inside the `computer-vision-deep-learning` folder you will find:
1. Image processing basics: get familiar with the principal concepts in image processing and computer vision (image handling, filters, denoising)
2. Deep learning: Tensorflow basics with MNIST example (single layer network and multilayer network)
3. Applications: 
    * CV: Face detection using Convolutional Neural Networks (CNN)
    * DL: Historical document processing - page and textline detection
    * DL: Historical document classification
    
Inside the `crf`folder you will find a CRF tutorial notebook treating how to use a CRF from annotating to predicting new text.

If you're already familiar with some concepts, feel free to go to the next notebook.


