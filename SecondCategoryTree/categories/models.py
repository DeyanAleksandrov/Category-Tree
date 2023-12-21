from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            on_delete=models.CASCADE,
                            related_name='sub_categories'
                            )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
