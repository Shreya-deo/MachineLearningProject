# MachineLearningProject
This is first machine learning project.

### SOFTWare and account requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads) 

Creating conda environment
'''
conda create -p venv python==3.7 -y
'''
'''
conda activate venv/
'''
'''
conda activate venv
'''
'''
pip install -r requirements.txt
'''
To add files to git
'''
git add .
'''
OR
'''
git add <filename>
'''

Note : to ignore file or folder from git we can write name of file /folder in .gitignore file.

to check the git status
'''
git status
'''

to check all version maintained by git
'''
git log
'''

to create version/create all changes by git
'''
git commit -m "message"
'''

to send version/changes to github
'''
git push origin main
'''

to check remote url
'''
git remote -v
'''

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = shreyaofficial8999@gmail.com
2. HEROKU_API_KEY = 295b777e-e7db-48db-9055-a4c221ac74d1
3. HEROKU_APP_NAME = first-ml-application

BUILD docker image
'''
docker build -t <image_name>:<tagname> location of dockerfile
'''

>Note: Image name for docker must be lowercase
tagname can be anytagname, mostly it's, latest

To list docker images
'''
docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 <imageID>
'''

To check running container
'''
docker ps
'''

To stop docker containers
'''
docker stop <containerID>
'''
