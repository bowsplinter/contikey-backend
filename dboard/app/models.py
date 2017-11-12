from django.db import models

class User(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `App` instance, given the validated data.
    #     """
    #     return App.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `App` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

class Article(models.Model):

class Channel(models.Model):

class Comment(models.Model):
