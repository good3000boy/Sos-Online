from django.contrib import admin
from .models import PostEdu, PostEnglish, PostNet, PostIcdl, PostPhoto, PostPython, PostVideo, PostBasicComputer,\
    PostAdvancedComputer, PostSecondaryComputer, PostBourse, PostDesign, PostOffice, PostPhotoShop, PostAccounting, PostAutoCad

# Register your models here.
admin.site.register(PostEdu)
admin.site.register(PostEnglish)
admin.site.register(PostPython)
admin.site.register(PostDesign)
admin.site.register(PostBourse)
admin.site.register(PostPhoto)
admin.site.register(PostPhotoShop)
admin.site.register(PostOffice)
admin.site.register(PostAutoCad)
admin.site.register(PostAccounting)
admin.site.register(PostVideo)
admin.site.register(PostBasicComputer)
admin.site.register(PostSecondaryComputer)
admin.site.register(PostAdvancedComputer)
admin.site.register(PostNet)
admin.site.register(PostIcdl)