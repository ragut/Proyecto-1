import unicodedata
import random
#//----- MODELO DEL CONCURSO -----//
class Contest():

    id = None
    user_id = None
    name = None
    banner = None
    url = None
    date_ini = None
    deadline = None
    description = None
    num_video = -1

    def __init__(self):
        self.id = None
        self.user_id = None
        self.name = None
        self.banner = None
        self.url = None
        self.date_ini = None
        self.deadline = None
        self.description = None

        self.num_video = -1

#//-----    FUNCIONES CRUD MODELO CONCURSO    -----//

    def set_num_video(self, num_video):
        self.num_video = num_video

    def set_variables_contest(self, user_id, name, date_ini, deadline, description):
        self.id = None
        self.user_id = str(user_id)
        self.name = name
        self.generate_url()
        self.banner = self.url+".jpg"
        self.date_ini = date_ini
        self.deadline = deadline
        self.description = description


    def set_variables_db(self, dictionary):
        self.id = str(dictionary["_id"])
        self.user_id = str(dictionary["user_id"])
        self.name = dictionary["name"]
        self.banner = dictionary["banner"]
        self.url = dictionary["url"]
        self.date_ini = dictionary["date_ini"]
        self.deadline = dictionary["deadline"]
        self.description = dictionary["description"]

    def generate_url(self):
        if self.name is not None:
            url = unicodedata.normalize('NFKD', self.name).encode('ASCII', 'ignore')
            url = url.lower()
            url = url.replace(" ","_")

            final_url = url
            exist = self.database.user_url_exist(final_url)

            while exist == True:
                final_url = url + "_" + str(random.randrange(1, 101, 2))
                exist = self.database.user_url_exist(final_url)

            self.url = final_url

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id), "user_id":self.user_id, "name": self.name, "banner": self.banner,
                "url": self.url, "date_ini":self.date_ini, "deadline":self.deadline, "description":self.description}

    def to_save(self):
        return {"user_id":self.user_id, "name": self.name, "banner": self.banner,
                "url": self.url, "date_ini":self.date_ini, "deadline":self.deadline, "description":self.description}