from django.core.exceptions import ValidationError


class MaxFileSizeInMbValidator:
    b_to_mb = 1024 * 1024

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * self.b_to_mb:
            raise ValidationError(f"File must be less than {self.max_size}MB")