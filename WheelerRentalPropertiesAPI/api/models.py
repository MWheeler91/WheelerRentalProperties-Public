from django.db import models

# Create your models here.
import os
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field

from WheelerRentalPropertiesAPI import settings
from .validators import validate_file_extension




# Create your models here.
# from WheelerRentalProperties import settings

STATE_CHOICE = [
    ("Alaska", "Alaska"),
    ("Alabama", "Alabama"),
    ("Arkansas", "Arkansas"),
    ("Arizona", "Arizona"),
    ("California", "California"),
    ("Colorado", "Colorado"),
    ("Connecticut", "Connecticut"),
    ("Delaware", "Delaware"),
    ("Florida", "Florida"),
    ("Georgia", "Georgia"),
    ("Hawaii", "Hawaii"),
    ("Iowa", "Iowa"),
    ("Idaho", "Idaho"),
    ("Illinois", "Illinois"),
    ("Indiana", "Indiana"),
    ("Kansas", "Kansas"),
    ("Kentucky", "Kentucky"),
    ("Louisiana", "Louisiana"),
    ("Massachusetts", "Massachusetts"),
    ("Maryland", "Maryland"),
    ("Maine", "Maine"),
    ("Michigan", "Michigan"),
    ("Minnesota", "Minnesota"),
    ("Missouri",  "Missouri"),
    ("Mississippi",  "Mississippi"),
    ("Montana", "Montana"),
    ("North Carolina", "North Carolina"),
    ("North Dakota",  "North Dakota"),
    ("Nebraska", "Nebraska"),
    ("New Hampshire", "New Hampshire"),
    ("New Jersey",  "New Jersey"),
    ("New Mexico",  "New Mexico"),
    ("Nevada",  "Nevada"),
    ("New York", "New York"),
    ("Ohio", "Ohio"),
    ("Oklahoma", "Oklahoma"),
    ("Oregon", "Oregon"),
    ("Pennsylvania",  "Pennsylvania"),
    ("Rhode Island", "Rhode Island"),
    ("South Carolina", "South Carolina"),
    ("South Dakota", "South Dakota"),
    ("Tennessee",  "Tennessee"),
    ("Texas",  "Texas"),
    ("Utah", "Utah"),
    ("Virginia", "Virginia"),
    ("Virgin Islands", "Virgin Islands"),
    ("Vermont", "Vermont"),
    ("Washington", "Washington"),
    ("Wisconsin", "Wisconsin"),
    ("West Virginia", "West Virginia"),
    ("Wyoming", "Wyoming")
     ]

PET_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No')
]

# ------------------  Custom Functions -------------------
def rename_upload(instance, filename):
    upload_to = os.path.join(settings.UPLOAD_URL, 'PersonDocuments')
    formatted_file_name = "{}_{}_{}".format(instance.person.first_name, instance.person.last_name, filename)
    return os.path.join(upload_to, formatted_file_name)

def upload_picture(instance, filename):
    upload_to = os.path.join('images/{}'.format(instance.address))
    return os.path.join(upload_to, filename)
#
#
def upload_additional_picture(instance, filename):
    upload_to = os.path.join('images/{}'.format(instance.property.address))
    return os.path.join(upload_to, filename)

# def upload_picture_location_test(instance, filename):
#     if not instance.address:
#         print("uploaded additonal pictures")
#         upload_to = os.path.join('images/{}'.format(instance.property.address))
#         return os.path.join(upload_to, filename)
#     if instance.address:
#         print("uploaded thumbnail")
#         upload_to = os.path.join('images/{}'.format(instance.address))
#         return os.path.join(upload_to, filename)


# ------------------  Models -------------------
class Property(models.Model):
    property_num = models.IntegerField()
    property_road = models.CharField(max_length=200)
    rent = models.IntegerField(default=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICE, max_length=25)
    zip = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField(max_length=3)
    sq_foot = models.IntegerField()
    property_title = models.CharField(max_length=200, blank=True, null=True)
    property_short_description = CKEditor5Field('property short description', config_name='extends', blank=True, null=True)
    description = CKEditor5Field('description', config_name='extends')
    is_active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=upload_picture, blank=True)
    thumbnail_alt_text = models.CharField(max_length=50, default='Property image.')
    # thumbnail = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True, allow_unicode=True)
    available_date = models.DateField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.property_num, self.property_road)

    @property
    def address(self):
        return '{} {}'.format(self.property_num, self.property_road)

    @property
    def full_address(self):
        return f'{self.property_num} {self.property_road}, {self.city}, {self.state}, {self.zip}'

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = slugify(self.address)

            has_slug = Property.objects.filter(slug=slug)
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.address) + '-' + str(count)
                has_slug = Property.objects.filter(slug=slug)
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('properties', kwargs={'slug': self.slug})
        return reverse('base:properties')

    def file_upload_location(self):
        return 'static/images/{}'.format(self.slug)

class Person(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(max_length=200)
    driver_license = models.CharField(max_length=20)
    driver_license_state = models.CharField(choices=STATE_CHOICE, max_length=25)
    ssn = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=200)
    pets = models.CharField(choices=PET_CHOICES, max_length=3)
    number_of_pets = models.IntegerField(blank=True, null=True)
    additional_comments = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_start_date = models.DateField(max_length=10, blank=True, null=True)
    address_end_date = models.DateField(blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICE, max_length=15, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    landlord = models.CharField(max_length=200, blank=True, null=True)
    landlord_phone = models.BigIntegerField(blank=True, null=True)
    reason_for_moving = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.person, self.address)


class Employment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    employer = models.CharField(max_length=200)
    employer_address = models.CharField(max_length=200)
    employer_city = models.CharField(max_length=200)
    employer_state = models.CharField(choices=STATE_CHOICE, max_length=25)
    employer_zip = models.IntegerField()
    job_title = models.CharField(max_length=200)
    job_start_date = models.DateField()
    supervisor_name = models.CharField(max_length=200)
    gross_income = models.BigIntegerField()

    def __str__(self):
        return str(self.person)


class Application(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    requested_move_in_date = models.DateField(max_length=10, null=True)
    application_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "{}, {}, {}".format(self.id, self.property, self.application_date)


class Applicant(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['person', 'application']]

    def __str__(self):
        return "{} {}".format(self.application, self.person)


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_additional_picture)
    alt_text = models.CharField(max_length=200)
    image_description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.property.address}"

class PersonFile(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    files = models.FileField(upload_to=rename_upload, blank=True, null=True, validators=[validate_file_extension])

    def file_name(self):
        return os.path.basename(self.files.name)

    def __str__(self):
        return os.path.basename(self.files.name)


class WebsiteStaticImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/website_static_images', max_length=200)
    image_alt_text = models.CharField(max_length=100, default="image alt text")

    def __str__(self):
        return self.name




