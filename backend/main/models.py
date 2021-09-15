from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.contrib.gis.db.models import PointField, PolygonField


class Channel(models.Model):
    channel_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # coordinates = PointField(null=True, blank=True)
    # area = PolygonField(null=False)
    uid = models.UUIDField(null=True, blank=True)
    extra_data = JSONField(null=True, blank=True)

    class Meta:
        db_table = 'channels'
        verbose_name_plural = 'channels'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)


class Video(models.Model):
    video_id = models.CharField(max_length=11, unique=True)
    channel = models.ForeignKey(to='Channel', related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    published_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'videos'
        verbose_name_plural = 'videos'

    def __unicode__(self):
        return '%s - %s' % (self.id, self.video_id)
