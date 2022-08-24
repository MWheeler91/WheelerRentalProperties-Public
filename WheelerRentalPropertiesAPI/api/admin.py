from django.contrib import admin
from .models import Property, Person, PropertyImage, Application, Address, Employment, Applicant, PersonFile, WebsiteStaticImage
# Register your models here.


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 15


class PropertyAdmin1(admin.ModelAdmin):
    inlines = [PropertyImageInline]


admin.site.register(Property, PropertyAdmin1)


admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Employment)
admin.site.register(Application)
admin.site.register(Applicant)
admin.site.register(WebsiteStaticImage)
admin.site.register(PersonFile)
admin.site.register(PropertyImage)
