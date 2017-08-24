# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from django.db import models
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z0-9_ ]*$')
PASSWORD_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}$')

class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}            

        print "name: {}".format(post_data['name'])
        print "alias: {}".format(post_data['name'])
        print "email: {}".format(post_data['email'])
        print "birthday: {}".format(post_data['birthday'])
        print "password: {}".format(post_data['password'])


        if len(post_data['name']) < 2 or not re.match(NAME_REGEX, post_data['name']):
            errors['name'] = "The first name field must only consists of letters and must be at least 2 letters long."
            
        if len(post_data['alias']) < 2:
            errors['alias'] = "The alias must must be at least 2 letters long."
        
        if len(post_data['birthday']) < 2:
            errors['birthday'] = "Must enter a valid birthday."
            
        # validate email
        email_input = post_data['email']
        if not re.match(EMAIL_REGEX, email_input):
            errors['email'] = "Invalid email entered"
          
        # if email is valid check db for existing email
        else:
            if len(self.filter(email=email_input)) > 0:
                errors['email'] = "Email already in use"

        # validate password and confirm password field matches confirm password
        if len(post_data['password']) < 8 or not re.match(PASSWORD_REGEX, post_data['password']):
            errors['password'] = "Password must be longer than eight characters, and can contain characters and numbers."
           
        # validate password field matches confirm password field
        elif post_data['password'] != post_data['confirm_pw']:
            errors['password'] = "Password and confirm password do not match"

        print errors
        
        if len(errors) == 0:
            birthday_str = post_data['birthday'].replace('-', ' ')
            birthday_input = datetime.strptime(birthday_str, '%Y %m %d')
            print "birthday: {}".format(birthday_input)
            
            name_input = post_data['name']
            alias_input = post_data['alias']
            email_input = post_data['email']
            password_input = post_data['password']
            hash1 = bcrypt.hashpw(password_input.encode('utf8'), bcrypt.gensalt())
            
            user = self.create(name=name_input, alias=alias_input, email=email_input, birthday=birthday_input, password=hash1, total_pokes=0)
            
            print "return user"
            return user
        
        print "return error"
        return errors
    
    def checkPassword(self, post_data):
        errors = {}
    
        email_input = post_data['email']
        password_input = post_data['password']
        
        users = self.filter(email=email_input)
        
        if len(users) > 0:
            user = users[0]
            password_stored = user.password
            
            print user.email
        
            if not bcrypt.checkpw(password_input.encode('utf8'), password_stored.encode('utf8')):
                errors['password'] = "email or password is not correct"

        else:
             errors['password'] = "No user found"
             
        if len(errors) == 0:
            print "password matches"
            return user
        
        return errors

    def get_user(self, user_id):
        user = User.objects.filter(id = user_id)[0]
        return user
    
    def get_users_exclude(self, user_id):
        users = User.objects.exclude(id = user_id)
        return users
    
    def poke_user(self, user_id, poke_id):
        user = User.objects.filter(id=user_id)[0]       
        poked = User.objects.filter(id=poke_id)[0]
        
        print "user_id: {}".format(user_id)
        print "user_alias: {}".format(user.alias)
        print "poke_id: {}".format(poke_id)
        print "total_pokes: {}".format(poked.total_pokes)
        pokes_total = poked.total_pokes 
        poked.total_pokes = poked.total_pokes + 1
        print "poked_alias: {}".format(poked.alias)
        
        poked.save()
        print "total_pokes: {}".format(poked.total_pokes)
        
        pokers = Poker.objects.filter(poker_id=user_id)
        poker = ""
        if (len(pokers)) < 1:        
            poker = Poker.objects.create(poker_id=user_id, poker_alias=user.alias, total_pokes=1)
            poked.poker.add(poker)
        else:
            poker = pokers[0]
            poker.total_pokes = poker.total_pokes + 1
            poked.poker.add(poker)
            print "poker.alias: {}".format(poker.poker_alias)
            
        poked.save()
        poker.save()

        return user
         
    def poked_by(self, user_id):
        user = User.objects.filter(id=user_id)[0]
        
        pokers = user.poker.order_by("-total_pokes")
        return pokers
        
        
#     def set_user_like_hero(self, user_id, hero_id):
#         user = User.objects.filter(id=user_id)[0]        
#         hero = User.objects.filter(id=hero_id)[0]
#         
#         user.heroes.add(hero)
#         return user

class PokerManager(models.Manager):
    def get_user(self, user_id):
        user = User.objects.filter(id = user_id)[0]
        return user
    
#     def get_users_exclude(self, user_id):
#         users = User.objects.exclude(id = user_id)
#         return users
#     
#     def poke_user(self, user_id, poke_id):
#         user = User.objects.filter(id=user_id)[0]        
#         poked = User.objects.filter(id=poke_id)[0]
#         
#         print "poke_id: {}".format(poke_id)
#         print "total_pokes: {}".format(user.total_pokes)
#         poked.total_pokes = poked.total_pokes + 1
#         print "total_pokes: {}".format(user.total_pokes)
#         poked.save()
#         
#         return user


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    birthday = models.DateTimeField()
    password = models.CharField(max_length=255)
    total_pokes = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    objects = UserManager()
    
    def __str__(self):
        return "<User object - name: {}; alias: {}; password: {}; email: {};".format(self.name, self.alias, self.password, self.email)
    
    def __repr__(self):
        return "<User object - name: {}; alias: {}; password: {}; email: {};".format(self.name, self.alias, self.password, self.email)
    
class Poker(models.Model):
    poker_id = models.IntegerField()
    poker_alias = models.CharField(max_length=255)
    total_pokes = models.IntegerField()
    poking = models.ManyToManyField(User, related_name='poker')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    objects = PokerManager()
    
    def __str__(self):
        return "<User object - poker_id: {}; total_pokes: {}".format(self.poker_id, self.total_pokes)
    
    def __repr__(self):
        return "<User object - poker_id: {}; total_pokes: {}".format(self.poker_id, self.total_pokes)
