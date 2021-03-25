# myproject

**Instructions:**

You need to send me your public key in order to connect to the virtual machine (via Gal/linkedin)

**Running the app:**
<br>**Connecting to the machine** open your shell and run `ssh 35.184.29.91`
<br>**Running the app** `bash ~/run-app.sh`

**You will need to connect to the machine from other shell in order to run commands** `ssh 35.184.29.91`

**Example for running api calls** `python3 ~/myproject/myproject/example/api_calls_example.py`

**Token** 7250270b0d6d401c05d1375c43845729f17af91f

**Access to DB** 
<br>**From browser** Go to admin page http://35.184.29.91/admin with user 'noa' password '1234'
<br>**From the machine** run the commands: `sudo su - postgres`, `psql` and `\c myproject2` (to log out- run `\q` and `exit`).

**Error logs** `nano ~/myproject/myproject/err_logs.txt`

**Running the tests** `python3 ~/myproject/myproject/api/tests.py`



