from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

def validate_title(value):
    if len(value.strip()) > 2:
        raise ValidationError('Title must be less than 2 characters. The original title is %s' % value)

def validate_content(value):
    if len(value.strip()) > 10:
        raise ValidationError('Content must be less than 10 characters. The original Content is %s' % value)

class Post(models.Model):
    title = models.CharField(
        max_length=10,
        error_messages={
            'blank' : 'Title is required',
        },
        validators=[validate_title]
    )

    # for custom max_length error message
    title.validators[-1].message = 'Your title must be less than 10 characters.'

    content = models.TextField(
        error_messages={
            'blank' : 'Content is required'
        },
        validators=[validate_content, validators.MaxLengthValidator(50)]
    )

    # for custom max_length error message
    content.validators[-1].message = 'Your title must be less than 50 characters.'