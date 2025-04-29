# Coding Challenge App



## Install:
- Install VSCode
- Download the code as zip file from https://github.com/mathurasridhar/divvy_dose.git
Navigation: After opening the link above, press the green button '<> Code' and select the option 'Download as zip' from the drop down list.
- Extract the zip folder and open the unzipped folder in VSCode

## pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running the code
- cd "to the unzipped folder path" in VSCode "Terminal" tab
- in "Terminal" tab of VSCode, execute the following:
python3 run.py
- Go to the browser and ping the health check URL:
http://127.0.0.1:5000/ = The expected output will be "Flask Rest API"

http://127.0.0.1:5000/api/git=mailchimp to get the gitstats output of the repository mailchimp

http://127.0.0.1:5000/api/bb=mailchimp to get the bitbucket stats output of the repository mail chimp

http://127.0.0.1:5000/api/git=mailchimp&bb=mailchimp => to get the consolidated stats for both git and bitbucket

http://127.0.0.1:5000/api/git=mailchi, http://127.0.0.1:5000/api/bb=mailchi, http://127.0.0.1:5000/api/git=mailchi&bb=mailchimp to see the failure messages

## Run pytest
- cd /divvy_dose
- type the command => pytest
- The above command should collect 7 items; there should be 5 passed 2 fails
### Making Requests

```
curl -i "http://127.0.0.1:5000/health-check"
```

