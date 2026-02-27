from django.db import models
from django.utils.timezone import now


class HardwareManual(models.Model):
    """
    The permanent storage for validated hardware specifications.
    Enforces uniqueness and provides persistence via Postgres/Supabase.
    """

    # Identification
    brand = models.CharField(max_length=255, db_index=True)
    model_name = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255, blank=True, null=True)

    # Categorization
    category = models.CharField(max_length=50, db_index=True)

    # Technical Specs (Stored as JSON in Postgres for flexibility)
    specs = models.JSONField(
        help_text="Flexible dictionary of technical specifications."
    )

    # Intelligence & Metadata
    raw_summary = models.TextField(blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)
    source_url = models.URLField(max_length=500)

    # The Idempotency Key
    content_hash = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="SHA-256 hash to prevent duplicate entries.",
    )

    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hardware Manual"
        verbose_name_plural = "Hardware Manuals"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.model_number})"
