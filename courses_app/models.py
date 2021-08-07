from django.db import models

class Course_manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name_input']) < 6:
            errors['name_input'] = 'Name must be more than 5 characters'
        if len(postData['desc_input']) < 16:
            errors['desc_input'] = 'Description must be more than 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Course_manager()
    

class Desc(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    desc = models.TextField(default='')

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)