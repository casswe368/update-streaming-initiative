Update Streaming Code
======

This project is written to identify flash-based streaming players imbedded in AO3 works. It is build off of a forked version of alexwlchan's unofficial AO3 api.
You can find `the original package by alexwlchan here <https://github.com/alexwlchan/ao3/>`_ and `the version used for this project here <https://github.com/casswe368/ao3>`_.



Motivation
**********

With the flash plug-in being decomissioned, it is no longer supported by many browsers and soon will not be supported by AO3 on any browser. There was no alternative to the flash player for audio files on AO3 until `November 2019 <https://archiveofourown.org/admin_posts/14125>`_ when the html5 audio tag was added.

This means that for many podficcers, the in-page streaming for their podfics will soon stop working if it has not already. This is not a devastating change as one can still click through to the original file link to access the podfic, but it is inconvenient.

I wrote this code to find all my podfics that need to be updated, and then to pull out the url from the old code and reformat it using the html5 audio tag. I then expanded it so that you can pull from any user that you enter so that the "update report" can be generated for other podficcers as well.

Installation
************

There is no package for this code or for my version of the unofficial AO3 api, so you will need to have all the files downloaded to use it. You will also need the packages in requirements.txt installed. To run the script, you have to be using a Python IDE such as Spyder or IDLE.

To view restricted works, you have to be logged in to AO3. To access the log-in details from the Python script, you have to have a file called "cred.py". Edit the file "sample-cred.py" and change the username and password to your AO3 username and password. Then rename the file from "sample-cred.py" to "cred.py"


Usage
*****

The file that you actually need to run is "UpdateStreaming.py". This then calls on the other files.

It will prompt you to enter the user/tag you want to search through. You only need to include part of the url as everything else is already included in the script. You will be prompted:

"Please specify the url in the format of users/gunpowderandlove or tags/Leverage: "

Type in the user whose works you want to search through and press enter. Ex. for https://archiveofourown.org/users/gunpowderandlove/works, you would type in users/gunpowderandlove (you do not need any quotation marks). If you wanted to look only through a specific pseud, just include that as part of the url. Ex. for https://archiveofourown.org/users/gunpowderandlove/pseuds/wingedwords/works, you would type in users/gunpowderandlove/pseuds/wingedwords.

You can also enter a tag that you wish to search through, but just because you can does not mean you should.

It will then create a report with the updated code. For each podfic, it will give the title of the podfic, the link to the work, and the broken and reformatted code that needs to be changed. If there are multiple embedded streaming players in one podfic, it will list the broken and reformatted code for each of them.

Warning: This process will be slow. That is by design. Since you have to open each one of your fics to check for the out-dated code, you are connecting with the server very often. I have therefore added wait times in. It will wait approximately 3 seconds after each page is accessed before accessing the next page. Sometimes if you have accessed the server to often, it will say "Retry later". If it sees that error it will wait 20 seconds and then try again. If it sees that error a second time, the script will end with an error. Wait a while and then try again. If it happens repeatedly, I recommend increasing the wait times. Be cautious with multiple "Retry later" messages. I have not yet had a problem but it is theoretically possible that AO3 might block you/your IP address in self-defense.


How it works
*****

First the script runs through each page of the specified url, and captures the work id for each work on each page. You then have a list of all your works by id. The script then takes that list and loops through it, looking up each work by its id, and capturing the information in a class instance.

One piece of information it captures is the actual text in the body of the work. The script then looks through that text for each work and finds if there is any code starting with "<embed".

If there is, it attempts to identify the mp3 link used in the code, pull it out, and reformat it with the html5 audio tag. If it cannot find the link, it will not generate the new code but it will still include it in the report so that you can update it manually.

It is looking for the following kinds of code:

`The archiveofourown player <https://archiveofourown.org/admin_posts/250>`_

.. code-block:: pycon
	
	<embed type="application/x-shockwave-flash" flashvars="mp3=MP3_FILE_URL" src="https://archiveofourown.org/system/dewplayer/dewplayer.swf" width="200" height="27" allowscriptaccess="never" allownetworking="internal"></embed>
	
	<embed type="application/x-shockwave-flash" flashvars="mp3=MP3_FILE_URL" src="https://archiveofourown.org/system/dewplayer/dewplayer-vol.swf" width="250" height="27" allowscriptaccess="never" allownetworking="internal"></embed>
	
	<embed type="application/x-shockwave-flash" flashvars="mp3=MP3_FILE_URL" src="https://archiveofourown.org/system/dewplayer/dewplayer-bubble.swf" width="250" height="65" allowscriptaccess="never" allownetworking="internal"></embed>
	
	<embed type="application/x-shockwave-flash" flashvars="mp3=MP3_FILE_URL" src="https://archiveofourown.org/system/dewplayer/dewplayer-bubble-vol.swf" width="250" height="65" allowscriptaccess="never" allownetworking="internal"></embed>
	
Or `the podfic.com player <http://podfic.com/>`_

.. code-block:: pycon

	<embed type="application/x-shockwave-flash" flashvars="audioUrl=LINKTOMP3HERE" src="http://podfic.com/player/audio-player.swf" width="400" height="27" allowscriptaccess="never" allownetworking="internal"></embed>


And will generate code using the html5 audio tag to replace it in the following format:

.. code-block:: pycon

	<audio src="MP3_FILE_URL" controls="controls" crossorigin="anonymous" preload="metadata">Your browser does not support streaming with the HTML5 audio tag, but you can still <a href="MP3_FILE_URL">play this podfic</a> in another tab.</audio>
   
Note: This code is not guaranteed to work depending on your hosting. There are some shenanigans to watch out for with http vs https, and your hosting site has to have CORS enabled. Check that this code is compatible with your hosting before you go and do all this work of replacing your code. Also watch for urls that just say http instead of https because those will not work either, but you can just find and replace to add the s.

License
*******

The project is licensed under the MIT license.
