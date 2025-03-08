from django.db import models

class moderators(models.Model):
    position = models.CharField(max_length=30)
    shedule = models.CharField(max_length=30)


class northern_warmers(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=30)


class blogs(models.Model):
    boss_id = models.ForeignKey(moderators, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    date = models.DateField()


class arts(models.Model):
    nw_ID = models.ForeignKey(northern_warmers, on_delete = models.CASCADE)
    art = models.CharField(max_length=100)
    date = models.DateField()
    blog_id = models.ForeignKey(blogs, on_delete = models.CASCADE)
    type = models.IntegerField()
    blog_part = models.IntegerField()


class text(models.Model):
    nw_ID = models.ForeignKey(northern_warmers, on_delete = models.CASCADE)
    texts = models.CharField(max_length=100)
    date = models.DateField()
    boss_id = models.ForeignKey(moderators, on_delete = models.CASCADE)
    blog_id = models.ForeignKey(blogs, on_delete = models.CASCADE)
    type = models.IntegerField()
    blog_part = models.IntegerField()


class code(models.Model):
    nw_ID = models.ForeignKey(northern_warmers, on_delete = models.CASCADE)
    codes =models.CharField(max_length=100)
    date = models.DateField()
    boss_id = models.ForeignKey(moderators, on_delete = models.CASCADE)
    blog_id = models.ForeignKey(blogs, on_delete = models.CASCADE)


class congratulations(models.Model):
    nw_ID = models.ForeignKey(northern_warmers, on_delete = models.CASCADE)
    texts = models.CharField(max_length=100)
    sender_ID = models.SET_NULL
    sender_name = models.CharField(max_length=30)
    image_url = models.SET_NULL
    date = models.DateField()
    blog_id = models.ForeignKey(blogs, on_delete = models.CASCADE)