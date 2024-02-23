# Anki Bot
<hr>

## Overview
Anki Bot is an algorithm utilizing GPT 3.5 Turbo to convert notes into a text file that could be read and imported by a renowned space repition service Anki
Anki is used primarily by medical students, but is also used by other high end degrees such as Law and Bio Sciences. 

Spaced repetition has been proven to be an extremely effective way of memorizing, dating back to 1885 by a German psychologist named Herman Ebbinghaus.

## Directions

#### Open AI Setup
<ol>
  <li>
    You will need to have an access key and funds to use the bot. Don't worry, with the model we're using it will only cost a fraction of a cent with each request
  </li>
  <li>
    Navigate to the <a href="https://platform.openai.com/account/billing/overview" target="_blank">Billing Page</a> at OpenAI <br>
    Add some money to your account, $5 is more than enough for the year (until expiry)
  </li>
  <li>
    Obtain your <a href="https://platform.openai.com/api-keys" target="_blank">API key</a> and store it in a safe place, we will need this to allow you to convert your notes!
  </li>
</ol>

#### Set up your API Key
<ol>
  <li>
    Clone the repository and save the folder somewhere
  </li>
  <li>
    Create a new file within the folder called <strong>.env</strong> and write the following <br>
    <code>export OPENAI_API_KEY = [paste your api key here]</code><br>
    Save the file
  </li>
</ol>

#### Installations
<ol>
  <li>
    You will need python to run on your computer. If you do not have python installed, install it.
  </li>
  <li>
    Open up the command line / terminal in your operating system, navigate to the folder and type the following things in
    <code>python install openai</code><br>
    <code>python install dotenv</code><br>
    You should be all set!
  </li>
</ol>

#### You're ready, run the file!
<ol>
  <li>
    In the terminal, write <code>python main.py</code>
  </li>
  <li>
    It will ask you to name your deck. For instance, if you were making a deck to memorize fruits in spanish, type "spanish-fruits" and it will make a file called <strong>spanish-fruits-anki-bot-deck.text</strong>
  </li>
  <li>
    Follow the directions and continue to paste your notes. When finished, hit enter. If the loop continues, type <code>exit</code> (no caps) to stop the program
  </li>
  <li>
    Navigate to the newly create file which would be in your anki bot folder
  </li>
</ol>

#### Importing to Anki
<ol>
  <li>
    Open up Anki and click <strong>import file</strong> > Navigate to your [filename]-anki-bot.txt file. 
  </li>
  <li>
    It should already have the delimeter as pipe, but if not select pipe
  </li>
  <li>
    Scroll down to the bottom to the <strong>Field Mapping</strong> section <br>
    Make sure to: <br>
    <ul>
      <li>Select the front of card as the first column</li>
      <li>Select the back of card as the second column</li>
      <li>Select the category as the third column</li>
    </ul>
      <li>Click import at the top and you should be ready to go!</li>
  </li>
</ol>
<hr>

## Example
<ul>
  <li>Notes that I pasted in:<br>
  <code>
    What is docker
	• Docker is a way to package software so it can be run on any hardware
	• 3 main components
		○ Dockerfile - blueprint for building docker images
		○ Image - template for running docker containers
		○ Container - running process
Docker in use
	• You can share data across containers using volume
	• To upload your docker file, you use docker.build -t username/appname
	• To run a file, go onto the docker desktop and find the image name. From there you can run using
		○ Docker run imgtag
			§ If you want to run it on a local port, you can use docker run -p localport:dockerport imagetag
  </code>
  </li>
  <li>
    Here was the output: in a <em>docker-training-anki-bot-deck.txt</em> file: <br>
    <code>  
      What is Docker? | Docker is a way to package software so it can be run on any hardware | Docker Basics  
      What are the 3 main components of Docker? | Dockerfile - blueprint for building docker images, Image - template for running docker containers, Container - running process | Docker Basics  
      How can you share data across containers in Docker? | You can share data across containers using volume | Docker Usage  
      How do you upload your Docker file? | To upload your docker file, you use docker build -t username/appname | Docker Usage  
      How do you run a file in Docker? | To run a file, go onto the docker desktop and find the image name. From there you can run using Docker run imgtag | Docker Usage  
      How can you run a Docker container on a local port? | If you want to run it on a local port, you can use docker run -p localport:dockerport imagetag | Docker Usage
    </code>
  </li>
</ul>
