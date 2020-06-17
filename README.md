# Project 2

Web Programming with Python and JavaScript
---
Flack Slack Clone
---
## Features
---
Display Name: When a user visits Flack for the first time, they are prompted to type in a display name using bootsrap modal that will eventually be associated with every message the user sends. If a user closes the page and returns to the app later, the display name is still be remembered as it is stored in localStorage in Browser.
---
Channel Creation: Every User create a new channel, so long as its name doesn’t conflict with the name of an existing channel. By default after login user is redirected to lobby channel which is a genral channel.
---
Channel List: All th users are able to view the channels in the app and can switch channels. When a new channel is created it is added to channel list every user is able to see new channel without reloading the page.
---
Messages View: After Entering display name user is redirected lobby where he can view existing messages or go to another channels and view Existing Messages. Maximum 100 Messages are stored in server side memory.
---
Sending Messages: User can send messages without reloading the page unlimited is displayed the can scroll through chat-box users can view their sent or others recieved messages even after closing window but is limitted to only 100 recent earlier messages rest are deleted from the server side memory.
---
Remembering the Channel: If a user is on a channel page, closes the web browser window, and goes back to site, the site takes them back to on what channel they were previously on.
---
Logout:The Site has a Logout feature when a  user clicks on logout his name is deleted from the browsers local storage and he is redirected to lobby where he is prompted to enter a display name he can enter same display name or a different one.
---
## Pages
---
application.py:Main Python File to run flask
---
template/index.html: Conatins HTML and Design of Page
---
static/myscript.js: Contains Javacript Code
---
