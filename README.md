# Polls app

Poll app project which provides polling functionality for Questions.
-   [https://docs.djangoproject.com/en/3.0/intro/tutorial01/](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

### Setup Instructions
```
git clone [https://github.com/raajsuthar/polls-app](https://github.com/raajsuthar/polls-app)
virtualenv env_polls
source env_polls/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Create some Questions and Choices
- Create a super user
- Visit http://127.0.0.1:8000/
 