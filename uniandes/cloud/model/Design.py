import random
import time

from ..services.DatabasesService import DatabasesServices

class Design():
    id=None
    company_id = None
    project_id = None
    names = None
    lastnames = None
    email = None
    status = None
    price = None
    file_name = None
    original_file_extension = None
    date = None

    database = DatabasesServices()

    def __init__(self):
        self.id=None
        self.company_id = None
        self.project_id = None
        self.names = None
        self.lastnames = None
        self.email = None
        self.status = None
        self.price = None
        self.file_name = None
        self.original_file_extension = None
        self.date = None

    def set_variables(self, company_id, project_id, names, lastnames, email, status, price, original_file_extension):
        self.id=None
        self.company_id = str(company_id)
        self.project_id = str(project_id)
        self.names = names
        self.lastnames = lastnames
        self.email = email
        self.status = status
        self.price = price
        file_name = self.company_id+"__"+self.project_id+"__"+self.email.split("@")[0]
        exist = self.database.design_file_name_exist(file_name)
        final_file_name = file_name
        while exist is True:
            final_file_name = file_name+"__"+str(random.randrange(1, 10000, 2))
            exist = self.database.company_url_exist(final_file_name)
        self.file_name = final_file_name
        self.original_file_extension = original_file_extension
        self.date = time.strftime("%Y/%m/%d - %H:%M:%S")

    def set_variables_from_dictionary(self, dictionary):
        self.id= str(dictionary["_id"])
        self.company_id = str(dictionary["company_id"])
        self.project_id = str(dictionary["project_id"])
        self.names = dictionary["names"]
        self.lastnames = dictionary["lastnames"]
        self.email = dictionary["email"]
        self.status = dictionary["status"]
        self.file_name = dictionary["file_name"]
        self.original_file_extension = dictionary["original_file_extension"]
        self.date = dictionary["date"]
        self.price = dictionary["price"]

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id), "company_id":self.company_id, "project_id":self.project_id,"names":self.names,
                "lastnames":self.lastnames,"email":self.email,"status":self.status,"file_name":self.file_name,
                "original_file_extension":self.original_file_extension, "date":self.date,"price":self.price}

    def to_save(self):
        return {"company_id":self.company_id, "project_id":self.project_id,"names":self.names,
                "lastnames":self.lastnames,"email":self.email,"status":self.status,"file_name":self.file_name,
                "original_file_extension":self.original_file_extension,"date":self.date,"price":self.price}