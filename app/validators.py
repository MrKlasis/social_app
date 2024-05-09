from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


def validate_password(value):
    if len(value) < 8 or not any(char.isdigit() for char in value):
        raise ValidationError('Password must be at least 8 characters long and contain at least one digit.')


def validate_email_domain(value):
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError('Only mail.ru and yandex.ru domains are allowed.')


def validate_author_age(date_of_birth):
    if date_of_birth > (timezone.now() - timedelta(days=365*18)).year:
        raise ValidationError('Author must be at least 18 years old to create a post.')


def validate_title(value):
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError('Title cannot contain forbidden words: ерунда, глупость, чепуха.')
