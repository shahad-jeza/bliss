from django.db import models

# category --------------

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children' , on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)  
        verbose_name_plural = "categories"       
                                              

    def __str__(self):                          
        full_path = [self.name]              
                                               
        k = self.parent

        while k is not None:
            full_path.append(k.name)         
            k = k.parent

        return ' -> '.join(full_path[::-1])     


# products ----------

class products(models.Model):
     name = models.CharField(max_length=200)
     image = models.CharField(max_length=1083)  
     price = models.FloatField()
     slug = models.SlugField(unique=True)
     category = models.ManyToManyField('Category')  #did it succsefully
     short_describe = models.CharField(max_length=500)
     long_describe = models.CharField(max_length=3000)
     size = models.FloatField()
     skin_type = models.CharField(max_length=1000)


def __str__(self):
        return self.title
