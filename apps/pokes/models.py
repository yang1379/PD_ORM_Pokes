# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# 
# from django.db import models
# from datetime import datetime
# from ..login.models import User
# 
# class PokerManager(models.Manager):
#     def get_user(self, user_id):
#         user = User.objects.filter(id = user_id)[0]
#         return user
#     
# #     def get_users_exclude(self, user_id):
# #         users = User.objects.exclude(id = user_id)
# #         return users
# #     
# #     def poke_user(self, user_id, poke_id):
# #         user = User.objects.filter(id=user_id)[0]        
# #         poked = User.objects.filter(id=poke_id)[0]
# #         
# #         print "poke_id: {}".format(poke_id)
# #         print "total_pokes: {}".format(user.total_pokes)
# #         poked.total_pokes = poked.total_pokes + 1
# #         print "total_pokes: {}".format(user.total_pokes)
# #         poked.save()
# #         
# #         return user
# 
# class Poker(models.Model):
#     poker_id = models.IntegerField()
#     total_pokes = models.IntegerField()
#     poking = models.ManyToManyField(User, related_name='poker')
#     created_at = models.DateTimeField(default=datetime.now)
#     updated_at = models.DateTimeField(default=datetime.now)
#     objects = PokerManager()
#     
#     def __str__(self):
#         return "<User object - poker_id: {}; total_pokes: {}".format(self.poker_id, self.total_pokes)
#     
#     def __repr__(self):
#         return "<User object - poker_id: {}; total_pokes: {}".format(self.poker_id, self.total_pokes)
