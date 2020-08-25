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
   
6. For the media files in settings.py

   MEDIA_ROOT=os.path.join(BASE_DIR,'media')
   MEDIA_URL='/media/'
   
   in urls.py
   if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

7. For the custom user model, create a new app named users where the User model will be inherited from AbstractUser. In order to log in from 
    the phone number, the username field is changed to phone i.e. USERNAME_FIELD = 'phone'.
    
8. In order to communicate with frontend, Django Rest Framework is used. Install Postman for the simplicity.

9. Use serializers.py to allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON and also for validation.

10. For viewing the data in API format in Postman or in Browsable API, use concept of generics_views or simply views.

11. Role of users is classified into customers and admin. By default, all the users are customers. The user is assigned as an admin under some conditions.

12. In order to display messages after logged in, logged out, changes in products and categories view, Response should be imported.
    
    from rest_framework.response import Response
    
13. For deleting the images from media folder when the admin updates or deletes the products,
    
    import os
    os.remove(product.image.path), where product is the object of Product to which the admin wants either to delete or update.   



    