from django.db import models


class Note(models.Model):
    """
    A simple note model storing a title and content along with created/updated timestamps.
    """
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.title}"
