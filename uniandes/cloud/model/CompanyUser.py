import base64
import unicodedata
import random
from ..services.DatabasesService import DatabasesServices

class CompanyUser():

    id = None
    name = None
    abbreviation = None
    email = None
    password = None
    url = None
    logo_filename = None

    database = DatabasesServices()

    def __init__(self):
        self.id = None
        self.name = None
        self.abbreviation = None
        self.email = None
        self.password = None
        self.url = None
        self.logo_filename = None

    def set_variables(self, name, abbreviation, email, password):
        self.id = None
        self.name = name
        self.abbreviation = abbreviation
        self.email = email
        self.password = base64.b64encode(password)
        self.generate_url()
        self.logo_filename = self.url+".png"

    def set_variables_from_dictionary(self, dictionary):
        self.id = str(dictionary["_id"])
        self.name = dictionary["name"]
        self.abbreviation = dictionary["abbreviation"]
        if "email" in dictionary:
            if dictionary["email"] is None:
                self.email = None
            else:
                self.email = dictionary["email"]
        else:
            self.email = None

        if "password" in dictionary:
            if dictionary["password"] is None:
                self.password = None
            else:
                self.password = base64.b64decode(dictionary["password"])
        else:
            self.password = None

        self.url = dictionary["url"]
        self.logo_filename = dictionary["logo_filename"]

    def generate_url(self):
        if self.abbreviation is not None:
            url = unicodedata.normalize('NFKD', self.abbreviation).encode('ASCII', 'ignore')
            url = url.lower()
            url = url.replace(" ","_")

            final_url = url
            exist = self.database.company_url_exist(final_url)

            while exist == True:
                final_url = url + "_" + str(random.randrange(1, 101, 2))
                exist = self.database.company_url_exist(final_url)

            self.url = final_url

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id),"name":self.name , "abbreviation": self.abbreviation,
                "email": self.email, "password": self.password, "url": self.url, "logo_filename":self.logo_filename}

    def to_save(self):
        return {"name":self.name , "abbreviation": self.abbreviation,
                "email": self.email, "password": self.password, "url": self.url, "logo_filename":self.logo_filename}