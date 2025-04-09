# BasicPyrogramBot
Basic Template for Bot with Pyrogram and Python. This Template is For Beginners like me ;) 

**This Bot Can Be Deployed on `VPS`, to Heorku and Railway easily. **

## Deployment
Plz give it a star

## The Easy Way ⚡️
### Deploy on `VPS`
- Fork and star the repo
- Go to main then edit ```config.py``` as below
- Put respective values in `""` and save.

```
API_ID = ""
API_HASH = ""
BOT_TOKEN = ""
```

- Now run following commands one by one...

```
sudo apt update
sudo apt install git python3-pip
git clone your_repo_link
cd you_repo_name
pip3 install -r requirements.txt
python3 -m PyroBot
```

- if you want bot to be running in background then enter `screen -S PyroBot` before `python3 -m PyroBot` 
- after `python3 -m PyroBot`, click `ctrl+A`, `ctrl+D`
- if you want to stop bot, then enter `screen -r PyroBot` and to kill screen enter `screen -S PyroBot -X quit`.


## Deploy your bot on `heroku`

» Method - 1:
- Star the repo, and fork it in desktop mode
- Click on  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- Fill your values and done ✅
 
» Method - 2:
- Star the repo, rate and fork it in desktop mode
- create app in heroku
- go to settings of ```app›› reveal config vars››``` add all variables as shown above by typing their correct name and value.
- add buildpacks i.e. `python` and `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
- connect to github and deploy
- turn on dynos
- Note: you must add buildpack in heroku to get the original video thumbnail and to remove already set thumbnail otherwise you will get black video
<b> How to add? </b>
- Go to heroku settings
- scroll down and click add buildpack
- now paste following link i.e `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git` in input bar and click add buildpack
- Now go back and redeploy


## Deploy on Render
- Fork and star the repo
- edit `config.py` same as guided for VPS deployment (you can edit on render also by filling enviroment variables)
- Go to render.com and singup/signin
- create new web service and select free plan
- connect github and your repository
- Click Deploy
- Done ✅
- See tutorial


## Koyeb Deployment

- Fork and star the repo
- edit `config.py` same as guided for VPS deployment (you can edit on koyeb also by filling enviroment variables)
- Go to koyeb.com and singup/signin
- create new web service make sure you must choose build type `Dokerfile` because in Koyeb as a default it is checked to `buildpacks` so you have to change that.
- connect github and your repository
- Click Deploy
- Done ✅
