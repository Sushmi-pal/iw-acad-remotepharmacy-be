**Remote Pharmacy**

Remote pharmacy is an online medicine ordering portal for a pharmacy where customers can order common medicines such as cold, cough, fever, pressure etc medicines and other utilites such as sanitary pads, handiplasts, powders, wipes etc for more convinience.

**Team Members:**
1. Sushmita Palikhe[sushmipalikhe97@gmail.com]

2. Salina Karki[salinakarki00@gmail.com]

3. Shrijan Bajracharya[shrijan.buzz.5@gmail.com]

4. Samip Shrestha [samip0884@gmail.com]

**Setup Steps**
1. Should have python installed on the device.Download python from [https://www.python.org/]

2. Install virtual environment using

   python -m venv venv
  
3. Install django on that venv using

   pip install django
   
4. Start a new project using

   django-admin startproject projectname
   
5. Create a new app using 

   python manage.py startapp newapp
   
6. For the mediaa files in settings.py

   MEDIA_ROOT=os.path.join(BASE_DIR,'media')
   MEDIA_URL='/media/'
   
   in urls.py
   if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
