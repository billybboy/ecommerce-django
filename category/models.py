from django.db import models
from app import models as app


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    DRAFT = 'draft'
    WATING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'draft'),
        (WATING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'active'),
        (DELETED, 'deleted')
    )


    user = models.ForeignKey(app.User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price

    class Meta:
        ordering = ['-created_at']