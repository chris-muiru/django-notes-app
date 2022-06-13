# django-notes-app
A Django application that enables users to create,delete and update notes based on a particular subject.Users can also view notes created by others.
## Installation
To install the project follow the following instructions:

```bash
> git clone https://github.com/kris-slinger/django-notes-app
> cd django-notes-app
> python manage.py runserver
```
in a new tab,create a superuser and migrate
```bash
> python manage.py createsuperuser
> python manage.py makemigrations
> python manage.py migrate
```
on your browser,enter http://localhost:8000/sign-in. 

Log in with the created cridentials(i.e superuser).

You can create new users in http://localhost:8000/admin/. Check out django documentation for more information

## Technologies Used
- [django](https://docs.djangoproject.com/en/4.0/)
- [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)

- [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)


## Contributing
Pull requests are allowed.For major tweak,please open a pull request to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


