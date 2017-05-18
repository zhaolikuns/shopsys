from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

#类型
class Category(models.Model):
    name = models.CharField('名称', max_length=50)
    slug = models.SlugField(
        'Slug',
        max_length=50,unique=True,
        help_text='根据name生成的，用于生成界面url，必须唯一'
    )
    description = models.TextField('描述')
    is_active = models.BooleanField("是否激活", default=True)
    meta_keywords = models.CharField('meta 关键字', max_length=255, help_text='关键字输入区域')
    meta_description = models.CharField('meta 关键字', max_length=255, help_text='关键字输入区域')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = "名称"
        verbose_name_plural = verbose_name
        db_table = 'categories'
        ordering = ['-create_time']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_category', args=(self.slug, ))

#产品
class Product(models.Model):
    #unique为True，name这个filed在这个table里是唯一的
    name = models.CharField('名称', max_length=255, unique=True)
    slug = models.SlugField(
        'Slug',
        max_length=255, unique=True,
        help_text='根据name生成的，用于生成界面url，必须唯一'
    )
    brand = models.CharField('品牌', max_length=50)
    sku = models.CharField("计量单位", max_length=50)
    price = models.DecimalField('价格', max_digits=9, decimal_places=2)
    old_price = models.DecimalField('旧价格', max_digits=9, decimal_places=2, blank=True, default=0)
    image = models.ImageField("图片", max_length=50)
    is_active = models.BooleanField('设为激活', default=True)
    is_bestseller = models.BooleanField('标为畅销', default=False)
    is_featured = models.BooleanField('标为推荐', default=False)
    quantity = models.IntegerField('数量', default=1)
    description = models.TextField('描述')
    meta_keywords = models.CharField('Meta 关键词', max_length=255, help_text='关键字输入区域')
    meta_description = models.CharField('meta 关键字', max_length=255, help_text='关键字输入区域')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-create_time']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug, ))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
