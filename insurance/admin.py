from django.contrib import admin
from .models import PostIns, PostThird, PostBody, PostFire, PostOmar, PostBarbarry, PostDoctor, PostAccident, PostResponsibility

# Register your models here.
admin.site.register(PostIns)
admin.site.register(PostThird)
admin.site.register(PostBody)
admin.site.register(PostResponsibility)
admin.site.register(PostOmar)
admin.site.register(PostAccident)
admin.site.register(PostFire)
admin.site.register(PostBarbarry)
admin.site.register(PostDoctor)