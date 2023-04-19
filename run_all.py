import os

os.system('./django-schedule/env/Scripts/Activate.ps1 & python django-schedule/schedule_proj/manage.py runserver')
os.system('cd vue-schedule & npm run dev')