## Diet Coke button for mom

A simple webapp with a Diet Coke button. Upon pressing it, you get notified through email and/or SMS the user of the button wants a diet Coke.

Originally made for a friend that who came up with this idea for his mother's birthday, as she really likes Diet Coke.

## Setup

For the time being, the setup for this involves forking the project, adding your desired forms of contact info for notifications, and hosting it on your desired webapp platform.
I wasn't intending on making this public originally, hence the slight awkwardness of the setup process.

Recommended steps:
<ol>
  <li> Fork the project through GitHub </li>
  <li> Add the desired email address and/or phone number to be notified, as well as the name of the person who you want to build this for </li>
  <li> (Optional) If you want this to be a button for something else, feel free to edit the "Diet Coke" text in /templates/index.html </li>
  <li> Crate a new project on a cloud platform such as [Heroku](https://www.heroku.com), and choose the option to build from GitHub. Then paste the link to the fork of this project you just made, and publish the heroku app </li>
  <li> You should now be able to go on the link for the webapp and receive notifications when your desired person presses the button </li>
</ol>
  
Note: You may notice that in the app.py, the template for the SMS notifications is an email. 

This is because most cell providers have thier own specific email domain that converts your email into a text. E.g. If I want to set this webapp up for someone with Veirzon, I would write <phone number>@vtext.com. You can likely find your desired email to text address with a quick google search.

## Planned feautres
  * An internal server where people can set up their own , private instances of the Diet Coke webapp at the click of a button, without having to deal with forking and creating a project on a separate cloud platform.
  * A method of editing the "Diet Coke" text on the page, the color, among other things without having to edit the HTML by hand, and doing so on the weabpp itself instead.
  
  
  
  