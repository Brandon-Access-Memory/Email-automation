# Email/Cold mail Automation tool- AtMailWin

<p align="center">
  <img src="logos/atmailwin-logo.svg" alt="CupidCues icon" width="200px" height="200px"/>
</p>

A free and open-source email automation tool. Schedule, personalize and send!
<br/>
<br/>
Have you ever meticulously crafted a personalized email to a potential employer or business and waited eagerly for a response that never arrived? It's a common scenario, and the disappointment is palpable. Creating highly personalized emails is time-consuming and often doesn't yield the desired results. AtMailWin offers a workaround - the ability to create semi-personalized emails, schedule them send them in bulk to multiple recipients.

You can use the site at [https://atmailwin.com](https://atmailwin.com) 


## Features

* Create dynamic email templates.
* Use variables, if statements in your email template.
* Schedule email.
* Schedule Follow-ups (follow-ups increases the chance of receiving response from recipient).
* Specify follow up rule. 
* Use existing [templates](https://atmailwin.com/email/templates/?public=True).

>**Note**: Don't use this service to send marketing emails or spams. It can result in your email's being sent to spam or locked.

Read this [article](https://atmailwin.com/blog/9/making-the-most-of-atmailwin-for-effective-cold-mailing/) 
to make most out of this tool

> This tool makes use if Jinja2 to render the emails, so any valid jinja syntax is acceptable


## How it works?

 1. Configure a email id by clicking on email configuration link.
 2. Create a email template. Use Variables within enclosed brackets `{{}}` to personalize the email.
 3. Schedule the email, create followups.


## Self hosting
If you want to self host it.

clone the repo
```
git clone https://github.com/PaulleDemon/Email-automation
```
Install python 3.8 or above

Install dependencies
```
pip install -r requirements.txt
```

add a .env file inside the email_automation folder with the following 
```
DEBUG=1
DOMAIN=""
SECRET_KEY=""
PORD_SECRET_KEY=""
REDIS_PROD_HOST=""

FIELD_ENCRYPTION_KEY=""
PROD_FIELD_ENCRYPTION_KEY=""

EMAIL_HOST=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""

POSTGRES_DATABASE=""
POSTGRES_USER=""
PROD_DB_PASSWORD=""
POSTGRES_PASSWORD=""
POSTGRES_HOST=""

POSTGRES_URL=""

FIREBASE_CRED_PATH=""
```
> You must fill up the values required

> You can create encryption key using the following `python manage.py generate_encryption_key`

> To generate secret key use `from django.core.management.utils import get_random_secret_key` then `get_random_secret_key()` in your python shell

Run database creation queries using
```
python manage.py migrate
```

now run the website using 
```
python manage.py runserver
```

The project uses tailwind so, when running locally use
```
python manage.py tailwind start
```

Run celery worker:
```
celery -A email_automation worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler 
```

Once you are satisfied you can build the tailwind using
```
python manage.py tailwind build
```

> Note: This tool makes use of Jinja templatig engine in the backend and nunjucks in the frontend for error checks. 

> You can use any valid Jinja syntax in the email template you are creating.

### Deployment:

If you are deploying on Render, Railway, Digital Ocean, You will be required to fire up different services. One for web other for celery.

You can make use of Railway to deploy your own instance.

<a href="https://railway.app?referralCode=BfMDHP">
  <img src="logos/railway.png" alt="railway icon" height="50px"/>
</a>


### **Support Opensource**

Developing and maintaining open-source and free projects requires a significant commitment of time and effort. My goal is to transition to working on open-source projects on a full-time basis. If you'd like to support me and the open-source community consider making a small donation. You can have your logo/name on this [page](https://atmailwin.com/support/) .


[<img src="https://github.com/PaulleDemon/PaulleDemon/blob/main/images/buy-me-coffee.png?raw=true" height="100px" width="350px">](https://www.buymeacoffee.com/ArtPaul)

**Other ways to support open-source**

* To dedicate more time to open-source I am also giving a non-GPL/commercial code license that can be used in a closed source project. Send a mail to paul@adostrings.com

* I also have production scale private projects (dating app, Social media, food delivery and more.), If you are interested in purchase, send a mail to paul@adostrings.com. 