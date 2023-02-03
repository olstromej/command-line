from peewee import *

from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('contacts', user='olstromej', password='123', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class contact(BaseModel):
  name = CharField()
  email = CharField()


def contact_list_begins():
  print("Welcome to your Contact list: ")
  answer = input("What would you like to do? Read Contacts(r) or Add Contacts(a) \n").lower()


  if answer == "r":
    contactList = contact.select()
    print([(contact.name, contact.email) for contact in contactList])

  if answer == "a":
    name = input("What is the contacts name? ")
    email = input("What is the contacts email? ")
    new_contact = contact(name=name, email=email)
    new_contact.save()
    print(f"Contact {name} has been added!")
    
contact_list_begins()


# db.connect()
