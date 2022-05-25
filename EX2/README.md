## Shell Script and Docker Automation Task

### 1) Setup

For this task, you will need a gmail account. Create one in case you don't have.
After your gmail account is created, you will need to generate an App Password to enable the provided script to send an e-mail. Remember, this key should only be used for tests, and should not be commited to your repository! Although the generated password is encrypted, you should not make this key public. Use this only for testing. 
[Link to guide](https://support.google.com/accounts/answer/185833?visit_id=637885811456670765-2473021700&p=InvalidSecondFactor&rd=1) to generate your App Password.

### 2) The Script

Create a shell script that will download the image ```lucasgaspar95/python-email-sender:latest``` available in docker hub, run a container, run a few commands inside this container, save comands output to a text file and run a existing python script inside the contianer.
Inside this container you should run the bellow commands saving it's output to RELATORY.txt
   
 * RAM Memory information in GigaBytes
 * Working user information
 * Working directory name
 * Working directory space
 * Disk Space information
 * Sorted list of all environment variables
 * Recusive list all files and permissions from root direcoty
 * A list of the last 9 commands used

The provided script expects specific environment variables, they should be set in the command to run the container. The need environment variables are:
 * EMAIL_SENDER
 * EMAIL_RECIEVER
 * SENDER_KEY    **(This is the key generated in the setup step)**
 * RELATORY_PATH  **(This is the file were the commands output should be stored)**

To run the provided script, just run:

``` python email-sender.py ```

### 3) Summary

You should create a shell script, that automates the commands inside a container, this script should download an image, run a container, execute some commands in the container, save the commands output into a file, and run the provided script. As a result, you should get an e-mail with the content inside the text file were the commands outputs are saved. 

### Deliverables
  * A shell script that download the image,performs all commands listed inside a container.
  * The txt generated with command outputs.
