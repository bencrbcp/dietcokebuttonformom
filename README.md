## Diet Coke button for mom

A webapp with a Diet Coke button. When pressed, you get notified through email and/or SMS the user of the button wants a diet Coke. 

Made a long time ago at the request of a friend, so I'm not actively working on this at the moment.

![Demo gif](https://i.imgur.com/X7nVU3s.gif)

## Setup

For the time being, the setup for this involves forking the project, adding your desired forms of contact info for notifications, and hosting it on your desired webapp platform.

Recommended steps:
<ol>
  <li> Fork the project through GitHub and make it private </li>
  <li> Add the desired email address and/or phone number to be notified, as well as the name of the person who you want to build this for </li>
  <li> Crate a new project on a cloud platform such as Heroku (https://www.heroku.com), and choose the option to build from GitHub. Then paste the link to the fork of this project you just made, and publish the heroku app </li>
  <li> You should now be able to go on the link for the webapp and receive notifications when your desired person presses the button </li>
</ol>
  
Note: You may notice that in the app.py, the template for the SMS notifications is an email.Read more [here](https://www.dialmycalls.com/blog/send-text-messages-email-address)
  
