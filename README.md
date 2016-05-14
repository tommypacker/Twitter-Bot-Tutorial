# Twitter Bot Tutorial
Made for CS Sail 2016 at UIUC

##Step 1: Install Git

Got to the following link where it will walk you through installing git based on your operating system.
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git. You can also click "download zip" if you don't want to install git.


##Step 2: Install Pip on your computer

Go to the following link: https://bootstrap.pypa.io/get-pip.py.
From your browser, click "save page as", and save it to your desktop.
Open up a terminal window and run ```python get-pip.py```. This will install pip to your computer.


##Step 3: Install Tweepy 

From your terminal, run ```pip install tweepy```. This will install the Twitter library to your computer.


##Step 4: Create a Twitter Application

Create a Twitter application from the Twitter [dev site] (https://apps.twitter.com/).
You will see a screen like this when you create your application:

![alt tag](http://imgur.com/Jet2dbE.png)

Fill it out with whatever you like. Next you need to go to the Keys and Access Tokens tab. 

![alt tag](http://imgur.com/VjLJgLB.png)

When you get there, scroll down and generate your access tokens. 
Keep this page open, because we will need it for a later step.


##Step 5: Download our Boilerplate Code

In your terminal, navigate to where you would like your project to be stored.
When there, run the following command to download the project:
```
git clone https://github.com/tommypacker/Twitter-Bot-Tutorial
```

This will download your initial setup.


##Step 6: Insert your credentials into tokens.py

Open up tokens.py with a text editor, and copy and paste all the info over from the Twitter application page.
Save tokens.py after you have inserted all your info over.


##Step 7: Writing the Actual Bot:

We will be going over this in class. If you want to look at something for future reference, check out twitterBot.py in the directory you downloaded.


##Step 8: Running the bot

In your terminal, run
```
python twitterBotBoiler.py
```


