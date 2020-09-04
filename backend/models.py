from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cumstomer(models.Model):
    '''

    '''
    ID = models.UUIDField(primary_key=True, null=False)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    LAST_MIDDLE_NAME = models.CharField(max_length=200, null=False)
    FIRST_NAME = models.CharField(max_length=200, null=False)
    EMAIL = models.CharField(max_length=200, null=False)
    COMPANY_FIELDS = models.CharField(max_length=200, null=False)
    JOB_POSITION = models.CharField(max_length=200, null=False)
    CREATE_DATE = models.DateTimeField(auto_now_add=True)
    UPDATE_DATE = models.DateTimeField(auto_now=True)
    VERSION = models.IntegerField(default=0)
    ACTIVE = models.BooleanField()

    def __str__(self):
        return self.ID

class Campaign(models.Model):
    '''

    '''
    ID = models.UUIDField(primary_key=True, null=False)
    CUMSTOMER_ID = models.ForeignKey(Cumstomer, on_delete=models.CASCADE)
    NAME = models.CharField(max_length=200, null=False)
    CREATE_DATE = models.DateTimeField(auto_now_add=True)
    UPDATE_DATE = models.DateTimeField(auto_now=True)
    VERSION = models.IntegerField(default=0)
    ACTIVE = models.BooleanField()

    def __str__(self):
        return self.ID

class UnitAnalysis(models.Model):
    '''

    '''
    ID = models.UUIDField(primary_key=True, null=False)
    CAMPAIGN_ID = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    NAME = models.CharField(max_length=200, null=False)
    TYPE = models.IntegerField(default=0)
    KEY_MAIN = models.CharField(max_length=200, null=True)
    KEY_EXTRA = models.CharField(max_length=200, null=True)
    KEY_EXCLUDE = models.CharField(max_length=200, null=True)
    KEY_PLACE = models.CharField(max_length=200, null=True)
    CREATE_DATE = models.DateTimeField(auto_now_add=True)
    UPDATE_DATE = models.DateTimeField(auto_now=True)
    VERSION = models.IntegerField(default=0)
    ACTIVE = models.BooleanField()

    def __str__(self):
        return self.ID

class AnalysisResults(models.Model):
    '''

    '''
    ID = models.UUIDField(primary_key=True, null=False)
    UNIT_ANALYSIS_ID = models.ForeignKey(UnitAnalysis, on_delete=models.CASCADE)
    PERIOD = models.CharField(max_length=200, null=False)
    POSITIVE_INDICATOR = models.IntegerField(default=0)
    NEGATIVE_INDICATOR = models.IntegerField(default=0)
    NEUTRAL_INDICATOR = models.IntegerField(default=0)
    TOTAL_MENTION = models.IntegerField(default=0)
    TOTAL_INTERACTIVE = models.IntegerField(default=0)
    CREATE_DATE = models.DateTimeField(auto_now_add=True)
    UPDATE_DATE = models.DateTimeField(auto_now=True)
    VERSION = models.IntegerField(default=0)
    ACTIVE = models.BooleanField()

    def __str__(self):
        return self.ID

class Notification(models.Model):
    '''

    '''
    ID = models.UUIDField(primary_key=True, null=False)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE = models.CharField(max_length=200, null=False)
    DOMAIN = models.CharField(max_length=200, null=False)
    TITLE = models.CharField(max_length=200, null=False)
    CONTENT = models.CharField(max_length=200, null=False)
    IMAGE = models.ImageField(upload_to = None)
    ICON = models.CharField(max_length=200, null=False)
    LINK = models.CharField(max_length=200, null=False)
    SUB_CONTENT = models.CharField(max_length=200, null=False)
    MARKER = models.BooleanField()
    STATUS = models.BooleanField()
    CREATE_DATE = models.DateTimeField(auto_now_add=True)
    UPDATE_DATE = models.DateTimeField(auto_now=True)
    VERSION = models.IntegerField(default=0)
    ACTIVE = models.BooleanField()

    def __str__(self):
        return self.ID