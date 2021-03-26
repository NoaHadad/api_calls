# myproject

**Instructions:**

You need to send me your public key in order to connect to the virtual machine (via Gal/linkedin)

**Running the app:**
<br>**Connecting to the machine** open your shell and run `ssh 35.184.29.91`
<br>**Running the app** `bash ~/run-app.sh`

**You will need to connect to the machine from other shell in order to run other commands** `ssh 35.184.29.91`

**API overview** http://35.184.29.91/api

**Example for getting existing token and running api calls** <br>`python3 ~/myproject/myproject/example/api_calls_example.py`

**Token to use** 474131a59a189e801c7441b9c29f5ff590a3174d

**Access to DB** 
<br>**From the browser** Go to admin page http://35.184.29.91/admin with user 'noa' password '1234'
<br>**From the machine** run the commands: `sudo su - postgres`, `psql` and `\c myproject` (log out- run `\q` and `exit`).

**Error logs** `cat ~/myproject/myproject/err_logs.txt`

**Running the tests** `python3 ~/myproject/myproject/api/tests.py`



