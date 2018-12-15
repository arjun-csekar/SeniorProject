# SeniorProject
Arjun Chandrasekaran


Handwriting recognition project using machine learning techniques.

Current version has executable located in Recognition\build\UIMain.exe
Executable might not run currently due to problems with using tensorflow in Python 3.7 version

To run, install Anaconda python. Spyder is the IDE we will use to run and it comes with Anaconda.

Once installed open Anaconda Navigator click on Environments tab and under search packages install the following

numpy
matplotlib
pillow
tensorflow
opencv

After installing packages open Spyder and open UIMain.py and run


Features:
  1. Click upload to upload image. Sample Images available.
  2. All images shown on UI are clickable to open in default Image Viewer
  3. Click Process to start the pre process. This can take a while, so do not be alarmed if it is unresponsive. As this takes
     time, upload small sample handwritten images.
  4. Once done click advance to view the pre processing steps and adjust to optimize.
  5. Click convert to start recignition process. Text should be displayed on Main window. Current version does not include save.
  
This should be run on Python 3.7. If there is any module error. Install the recommended package.
