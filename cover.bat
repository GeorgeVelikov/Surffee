rmdir /Q /S htmlcov
coverage erase
coverage run ./manage.py test surveys
coverage html
coverage report