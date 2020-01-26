from django.db import models

# Create your models here.

class Categorie(models.Model):
   categorie_name = models.CharField(max_length=100, verbose_name='Kateqoriya adi')
   categorie_detail = models.CharField(max_length=1000, verbose_name='Kategoriya detallari')
   created_date = models.DateTimeField(auto_now_add=True)
   updated_date = models.DateTimeField(auto_now=True)
   class Meta:
      verbose_name = "Categorie"
      verbose_name_plural = "Categories"

   def __str__(self):
      return self.categorie_name
    
class Posts(models.Model):
   owner_id = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Postun Sahibi ", related_name='posts')
   title = models.CharField(max_length = 100,verbose_name = "Başlıq")
   content = models.CharField(max_length=3000, verbose_name='İçəriyi')
   category = models.ForeignKey(Categorie,on_delete = models.CASCADE,verbose_name = "Post Kategiyasi",related_name="post_category")
   subcategory = models.TextField(verbose_name = "Post Subkategoriyalari", default="None")
   created_date = models.DateTimeField(auto_now_add=True,verbose_name="Paylaşım tarixi")
   updated_date = models.DateTimeField(auto_now=True)
   post_image = models.FileField(blank = True,null = True,verbose_name="Şəkil əlavə edin")
   def __str__(self):
      return self.title
   class Meta:
      ordering = ['-created_date'][:10]

class Comments(models.Model):
   post_id = models.ForeignKey(Posts,on_delete = models.CASCADE,verbose_name = "Paylaşım",related_name="comments")
   author_id = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kommentin sahibi ", related_name='authors')
   comment_content = models.CharField(max_length = 1000,verbose_name = "Komment")
   comment_date = models.DateTimeField(auto_now_add=True)
   update_date = models.DateTimeField(auto_now=True)
   def __str__(self):
      return self.comment_content
   class Meta:
      ordering = ['-comment_date'][:5]

    
class SubCategory(models.Model):
   category = models.ForeignKey(Categorie,on_delete = models.CASCADE, verbose_name='Kategoriyasi', related_name='category')
   name = models.CharField(max_length=100, verbose_name='Kontent adi')
   created_date = models.DateTimeField(auto_now_add=True)
   updated_date = models.DateTimeField(auto_now=True)
   class Meta:
      verbose_name = "SubCategory"
      verbose_name_plural = "SubCategories"

   def __str__(self):
      return self.name
    