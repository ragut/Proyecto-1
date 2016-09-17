
class Project():

    id = None
    company_id = None
    name = None
    description = None
    budget = None
    currency = None
    num_design = -1

    def __init__(self):
        self.id = None
        self.company_id = None
        self.name = None
        self.description = None
        self.budget = None
        self.currency = None
        self.num_design = -1

    def set_num_design(self, num_design):
        self.num_design = num_design

    def set_variables(self, company_id, name, description, budget, currency):
        self.id = None
        self.company_id = str(company_id)
        self.name = name
        self.description = description
        self.budget = budget
        self.currency = currency

    def set_variables_from_mongo(self, dictionary):
        self.id = str(dictionary["_id"])
        self.company_id = str(dictionary["company_id"])
        self.name = dictionary["name"]
        self.description = dictionary["description"]
        self.budget = dictionary["budget"]
        self.currency = dictionary["currency"]

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id), "company_id":self.company_id, "name": self.name, "description": self.description,
                "budget": self.budget, "currency":self.currency}

    def to_save(self):
        return {"company_id":self.company_id, "name": self.name, "description": self.description,
                "budget": self.budget, "currency":self.currency}