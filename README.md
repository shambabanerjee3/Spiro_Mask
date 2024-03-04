Firstly Recorded the Breadthing with microphone and then conveted in mp3 and wav as it would required.
Next in sample_rate.py file use built in python open() function to read the WAV file and 25th byte of the file sample rate information is stored , so went to that position using seek() function and after getting the information simply print the value, and in my case i am getting 164Hz.

