from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets=(
        (None,{
            'fields':('title','author','image')

        }),
        ('important dates',{
            'fields':('created','editted')
        }),
        ('content',{
            'fields':('content',)
        }),
        ('status',{
            'fields':('status',"slug")
        }),
         
    )
    readonly_fields=['created','editted',"slug"]
    list_display=['title','author','status']
    list_filter=['status',]
    search_fields=('title','author__username')

