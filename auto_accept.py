import pyautogui
import time
import smtplib
from datetime import datetime

# I use this to auto accept Dota2 games, but it could be used for anything.

while True:
    # Locate trigger on screen
    accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
    if accept:
        pyautogui.moveTo(accept)
        # click multiple times just to make sure accept button gets clicked
        pyautogui.click(accept)
        pyautogui.click(accept)
        pyautogui.click(accept)
        pyautogui.click()

        print(f'Game Accepted. {datetime.now()}')

        # get connected to mail server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.connect('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Next, log in to your server
        server.login('youremail@gmail.com', 'YourPassword')

        # Send the mail
        msg = f'Dota2 Ready! {datetime.now()}'

        # I use verizon, so I use vtext.com, yours will depend on your cell provider.
        server.sendmail('youremail@gmail.com', 'phonenumber@vtext.com', msg)
        server.quit()

        time.sleep(5)
    else:
        pass
        time.sleep(3)
        print(datetime.now())


