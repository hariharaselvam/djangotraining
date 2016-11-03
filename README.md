# djangotraining
Sample django application



## Steps:
1.  Create Virtual Environment:

      ``` $ virtualenv da```
      
      ``` $ source da/bin/activate```
     
2.  Pip install required libraries:

      ``` $ pip install -r requirements.txt ```
     
3.  Git clone:

      ``` $ git clone https://github.com/hariharaselvam/djangotraining.git ```
      
4.  Migrate database:

      ``` $ python manage.py makemigrations ``` 
      
      ``` $ python manage.py migrate ``` 
      
5.  Run the web application:

      ``` $ python manage.py runserver ``` 
      
      
6. Download and install redis server:

      ``` $ curl -O http://download.redis.io/redis-stable.tar.gz ```
      
      ``` $ tar -xvzf redis-stable.tar.gz ```
      
      ``` $ cd redis-stable ```
      
      ``` $ make ```
      
      ``` $ sudo make install ```
      
      ``` $ redis-server ```

7. Run celery:

      ``` $ celery -A ecommerce worker -l info ```

     

