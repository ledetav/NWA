from django.db import models

class Moderators(models.Model):
    moderator_position = models.CharField(max_length=100)
    moderator_shedule = models.CharField(max_length=100)

class NorthernWarmers(models.Model):
    nw_name = models.CharField(max_length=30)
    nw_join_date = models.DateField()

class Blogs(models.Model):
    moderator_id = models.ForeignKey(Moderators, on_delete=models.CASCADE)
    celebrant_name = models.CharField(max_length=30)
    birthday_date = models.DateField()

class NWAArchiveArts(models.Model):
    nw_ID = models.ForeignKey(NorthernWarmers, on_delete=models.CASCADE)
    work_art = models.CharField(max_length=100)
    work_publication_date = models.DateField()
    work_type = models.IntegerField()
    blog_part = models.IntegerField()
    blog_id = models.ForeignKey(Blogs, on_delete=models.CASCADE)

class NWAArchiveTexts(models.Model):
    nw_ID = models.ForeignKey(NorthernWarmers, on_delete=models.CASCADE)
    work_text = models.TextField()
    work_publication_date = models.DateField()
    work_type = models.IntegerField()
    blog_part = models.IntegerField()
    blog_id = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    moderator_id = models.ForeignKey(Moderators, on_delete=models.CASCADE)

class NWAArchiveCongratulations(models.Model):
    nw_ID = models.ForeignKey(NorthernWarmers, on_delete=models.CASCADE)
    congratulation_text = models.CharField(max_length=100)
    sender_name = models.CharField(max_length=30)
    work_publication_date = models.DateField()
    blog_id = models.ForeignKey(Blogs, on_delete=models.CASCADE)

class NWAArchiveCodes(models.Model):
    nw_ID = models.ForeignKey(NorthernWarmers, on_delete=models.CASCADE)
    work_code = models.CharField(max_length=100)
    work_publication_date = models.DateField()
    blog_id = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    moderator_id = models.ForeignKey(Moderators, on_delete=models.CASCADE)