from django.db import models

# Create your models here.
class MODELNAME(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'MODELNAME'
        verbose_name_plural = 'MODELNAMEs'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        pass


class MODE2LNAME(models.Model):
    """Model definition for MODE2LNAME."""

    # TODO: Define fields here
    foreignkey_name = models.ForeignKey(MODELNAME, verbose_name=("name"), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for MODE2LNAME."""

        verbose_name = 'MODE2LNAME'
        verbose_name_plural = 'MODE2LNAMEs'

    def __str__(self):
        """Unicode representation of MODE2LNAME."""
        pass
