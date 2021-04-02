# dota
automate some stuff so I can be more noob

 This is a simple project, but one that I've wanted forever! I use pyautogui, time, smtplib and datetime to achieve my goal. Sometimes dota2 game queues can last 10 minutes or more, this script allows me to start searching for a game and walk away.
 
![accept](https://github.com/kickinslowly/dota/blob/master/accept.png)
 
 I define the image I want to look for, which in this case is the accept button for the game Dota2. Then I have pyautgui search for this image on screen every 3 seconds. If it finds the image then it moves the mouse to the image and clicks it. Print to console current date and time, just for my OCD. Then it's time to fire off a text so I can wrap up whatever I'm doing in the other room and return to my pc. I use smtplib to connect and login to email server, this will depend on your email server, I use gmail. Then define the msg, which for me is 'Dota2 Ready {datetime.now()}' and fire it off by sending email to phonenumber@vtext.com. VTEXT.COM is used because my provider is Verizon, yours may be different and a quick google search can help you figure that out. BOOOM done, rinse and repeat.
