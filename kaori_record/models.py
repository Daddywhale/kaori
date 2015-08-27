# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AllBestRecord(models.Model):
    primary_key = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', blank=True, null=True)
    event = models.ForeignKey('Event', blank=True, null=True)
    record = models.ForeignKey('Record', blank=True, null=True)
    best_record = models.CharField(db_column='best_record', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_best_record'

class Competition(models.Model):
    competition_id = models.AutoField(primary_key=True)
    competition_name = models.CharField(max_length=200, blank=True, null=True)
    competition_year = models.IntegerField(blank=True, null=True)
    competition_formality = models.IntegerField(blank=True, null=True)
    kirokhoe = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competition'

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_distance = models.IntegerField(blank=True, null=True)
    event_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=45, blank=True, null=True)
    member_year = models.IntegerField(blank=True, null=True)
    member_gender = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Record(models.Model):
    record_id = models.IntegerField(primary_key=True)
    member = models.ForeignKey(Member, blank=True, null=True)
    competition = models.ForeignKey(Competition, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    record = models.CharField(max_length=45, blank=True, null=True)
    rank = models.CharField(max_length=45, blank=True, null=True)
    medal = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'

class FormalBestRecord(models.Model):
    primary_key = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', blank=True, null=True)
    event = models.ForeignKey('Event', blank=True, null=True)
    record = models.ForeignKey('Record', blank=True, null=True)
    best_record = models.CharField(db_column='best_record', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formal_best_record'

class EventForRank(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=45, blank=True, null=True)
    event_distance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_for_rank'