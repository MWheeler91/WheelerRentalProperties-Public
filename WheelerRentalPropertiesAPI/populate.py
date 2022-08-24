import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WheelerRentalProperties.settings')

import django
django.setup()


import random
from faker import Faker
from base.models import Property, Person, Application, Address, Employment, Applicant

from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WheelerRentalProperties.settings')


# fake pop script
fakegen = Faker()


def main():
    print("Populating the script!")

    # FakeProperty(10)
    # populate_person_data(150)

    # for my app I want a max of 4 Applicants per Application.  You will need make sure FakeApplicants is less than
    # FakeApplications for the script.  Applications are popped off the list when used to prevent the same one being
    # used move than once. For Example Application(id=25) adds 4 applicants.  20 loops later Application( id=25) is
    # selected again and adds 4 more.
    FakeApplications(100)
    FakeApplicants(99)


    print("Complete!")



# creates Fake address for Person
def FakeAddress(person):
    address = Address.objects.get_or_create(
        person=person,
        address=fakegen.street_address(),
        address_start_date=fakegen.date(),
        address_end_date=fakegen.date(),
        rent=12345,
        city=fakegen.city(),
        state="Tennessee",
        zip=fakegen.postcode(),
        landlord=fakegen.name(),
        landlord_phone=fakegen.msisdn(),
        reason_for_moving=fakegen.paragraph(nb_sentences=10)
    )


# Creates fake Employment History for Person
def FakeEmployment(person):
    employer = Employment.objects.get_or_create(
        # id = employment_id,
        person=person,
        employer=fakegen.company(),
        employer_address=fakegen.street_address(),
        employer_city=fakegen.city(),
        employer_state="Tennessee",
        employer_zip=fakegen.postcode(),
        job_title=fakegen.job(),
        job_start_date=fakegen.date(),
        supervisor_name=fakegen.name(),
        gross_income=fakegen.msisdn(),
    )


def FakeProperty(n):
    for x in range(n):
        property = Property.objects.get_or_create(
            property_num=fakegen.building_number(),
            property_road=fakegen.street_name(),
            rent=random.randint(500, 2500),
            city=fakegen.city(),
            state="Tennessee",
            zip=fakegen.postcode(),
            bedrooms=random.randint(1, 5),
            bathrooms=random.randint(1, 5),
            sq_foot=random.randint(700, 20000),
            description=fakegen.paragraph(nb_sentences=10),
            is_active=True,

            # You have to manually add images
            # thumbnail = Image.open("static/images/stock-vector-vector-graphic-of-no-thumbnail-symbol-1391095985.jpg"),
        )


def FakeApplications(n):
    # list of all Properties
    all_properties = list(Property.objects.all())
    for x in range(n):
        # selects random property from the list
        index = random.randrange(len(all_properties))
        # creates application with the randomly selected Property and sets thate within 2 yeas from today.
        application = Application.objects.get_or_create(
            property = all_properties[index],
            requested_move_in_date=fakegen.date_time_between(start_date = "now", end_date = "+1y"),
            application_date =fakegen.date_time_between(start_date = "-2y", end_date = "now")
        )


def FakeApplicants(n):
    all_persons = list(Person.objects.all())  # list of all Persons
    all_applications = list(Application.objects.all())  # list of all Apps

    # generates N number of applicants
    for x in range(n):
        # selects a random application from the list
        randon_application = random.randrange(len(all_applications))
        # selects the number of applicants
        num_of_people = random.randint(1, 4)

        for y in range(num_of_people):
            # p = random person
            p = random.randrange(len(all_persons))
            # creates my applicant
            applicant, _created = Applicant.objects.get_or_create(
                # person = person at index p in the all_person list
                person=all_persons[p],
                # application = application at index of the all_app list
                application=all_applications[randon_application]
            )

            # print("{} {}".format(applicant.person, applicant.application))
        all_applications.pop(randon_application)


def populate_person_data(n=5):
    for entry in range(n):
        # create person
        person, _created = Person.objects.get_or_create(
            first_name=fakegen.first_name(),
            middle_name=fakegen.first_name(),
            last_name=fakegen.last_name(),
            dob=fakegen.date_of_birth(),
            driver_license=1234563789,
            driver_license_state="Tennessee",
            ssn=123456789,
            phone=fakegen.msisdn(),
            email=fakegen.email(),
            pets="yes",
            requested_move_in_date=fakegen.date(),
            additional_comments=fakegen.paragraph(nb_sentences=10)
        )
        FakeAddress(person)
        FakeAddress(person)
        FakeEmployment(person)





if __name__ == '__main__':
    main()