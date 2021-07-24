# Optical_Character_Recognition
This project contains mainly three python files:

**WebcamVideoStream.py:**
It includes methods that involves in capturing video camera stream and read it frame by frame.

 **FPS.py:**
It includes methods involved in calculating time interval of video camera stream,
number of frames and calculating frames per second(fps).

**main.py**
It imports WebcamVideoStream.py and FPS.py. The methods detects text in frames and 
converts it into data form to formate the captured text. This process is done with the 
help of **OpenCV** and **pytesseract**.
