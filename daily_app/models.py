from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=150, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=150, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_category_name

    
class DayWiseData(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=600, blank=True, null=True)
    input = models.CharField(max_length=600, blank=True, null=True)
    time_0800 = models.CharField(max_length=100, blank=True, null=True)
    time_0900 = models.CharField(max_length=100, blank=True, null=True)
    time_1000 = models.CharField(max_length=100, blank=True, null=True)
    time_1100 = models.CharField(max_length=100, blank=True, null=True)
    time_1200 = models.CharField(max_length=100, blank=True, null=True)
    time_1300 = models.CharField(max_length=100, blank=True, null=True)
    time_1400 = models.CharField(max_length=100, blank=True, null=True)
    time_1500 = models.CharField(max_length=100, blank=True, null=True)
    time_1600 = models.CharField(max_length=100, blank=True, null=True)
    time_1700 = models.CharField(max_length=100, blank=True, null=True)
    time_1800 = models.CharField(max_length=100, blank=True, null=True)
    time_1900 = models.CharField(max_length=100, blank=True, null=True)
    time_2000 = models.CharField(max_length=100, blank=True, null=True)
    time_2100 = models.CharField(max_length=100, blank=True, null=True)
    time_2200 = models.CharField(max_length=100, blank=True, null=True)
    time_2300 = models.CharField(max_length=100, blank=True, null=True)
    time_0000 = models.CharField(max_length=100, blank=True, null=True)
    time_0100 = models.CharField(max_length=100, blank=True, null=True)
    time_0200 = models.CharField(max_length=100, blank=True, null=True)
    time_0300 = models.CharField(max_length=100, blank=True, null=True)
    time_0400 = models.CharField(max_length=100, blank=True, null=True)
    time_0500 = models.CharField(max_length=100, blank=True, null=True)
    time_0600 = models.CharField(max_length=100, blank=True, null=True)
    time_0700 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return (self.sub_category.sub_category_name + ' ' + str(self.date))
 