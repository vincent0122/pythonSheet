from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    limit = 50 * 1024 * 1024

    if filesize > limit:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value
