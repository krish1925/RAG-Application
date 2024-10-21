from django.db import models

# Create your models here for RAG application.

# Description of Models being used in the project 
# 1. User
# 2. Profile
# 3. Symptom list 
# 4. Symptom
# 5. Chat list


# User model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Profile model
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medical_history = models.TextField()
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):

        return self.user.name
    
# Symptom list model
class SymptomList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# Symptom model
class Symptom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptom_list = models.ForeignKey(SymptomList, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.user.name
    
# Chat list model
class ChatList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.user.name
    
# Chat model
class Chat(models.Model):
    chat_list = models.ForeignKey(ChatList, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.chat_list.user.name



