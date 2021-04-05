# autoVaxAppointment

## First and Foremost
I did not write geckodriver.exe! I don't think anyone would have truly believed it, but nethertheless. All the credit belongs to: https://github.com/mozilla/geckodriver/releases.
Also, if you are a developer, I apologize for this sometimes very verbouse READ.md, it is intended for people with a more rudimentary knowledge in Coding.

## Purpose
This little script is an inspiration to automate the laborious appointment-making-process for vaccinations against COVID19 in Germany. It should work fine for the Bundesland "Niedersachsen". For other region outside Niedersachsen you will need a different code since every Bundesland seems to have its own website.

## Prerequisits
First, you need to install python on your machine. Here is a reference on how to do that on a Windows machine: https://www.liquidweb.com/kb/how-to-install-python-on-windows/ here is one for mac https://www.dummies.com/programming/python/how-to-install-python-on-a-mac/. If you use Linux, I don't think you'll need an explaination on how to install python. If you have virtually no programming experience, I highly recommend to install PyCharm -- it comes as a community version which is free to use and open-source (https://pycharm-community-edition.en.softonic.com/download). As a last prerequisit you need to install selenium. This should fairly easy once you installed python. The site describes how to do it: https://www.makeuseof.com/how-to-install-selenium-webdriver-on-any-computer-with-python/

## How to
First, clone the repo. You can just click on the little button somewhere right-cornerish with the label "code". Click on it and download it as a zip file and extract it. You can open the file 'automateVaxAppointment.py' with your new IDE called PyCharm. 
Then go to line 33 and put in your date of birth in the same format as it is written there. Go to line 46, enter your post-code. Now we get to the mail ping. Set up a new Google-Account, I would highly recommend to only use this account for this sole purpose. Then enter this mail address in line 61 instead of the one which is written there. Do the same thing for the receiver mail address one line below. In line 63 you find the password section. Note, normally, you should never write a clear password into any electronic device connected to the internet. Thats why we were setting up the dummy mail address. Delete line 63 and enter instead: ´password = "yourpassword´ with yourpassword being the password for the dummy mail address. You can also specify the message in line 64 if you want to. Finally, scroll down to the end of the file. In PyCharm you'll see a small green triangle on the left of your code, click on it and choose ´run´. If it is not there, right click on the line 76 you should see an option to run this file. Thats it. One final note: the program tries again to make an appointment every 30 seconds. If you want it to be a different amount of time, you can choose a different amount of seconds in line 53, just rreplace the 30 with your number. Keep in mind, though, that your browser might be slow so maybe don't overdo it.

Should you encounter problems, just create a github account and write me a message. We will figure it out.
