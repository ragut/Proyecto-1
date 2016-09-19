import time

from ..controller.DatabasesService import DatabasesController

#//----- MODELO DE LOS VIDEOS -----//
class ContestVideo():
    id=None
    user_id = None
    contest_id = None
    video_name = None
    email = None
    names_user = None
    lastnames_user = None
    date = None
    status = None
    original_file = None


    database = DatabasesController()

    def __init__(self):
        self.id=None
        self.user_id = None
        self.contest_id = None
        self.video_name = None
        self.email = None
        self.names_user = None
        self.lastnames_user = None
        self.date = None
        self.status = None
        self.original_file = None


    def set_variables_video(self, user_id, contest_id, email, names_user, lastnames_user,  status, original_file):
        self.id=None
        self.user_id = str(user_id)
        self.contest_id = str(contest_id)
        self.email = email
        self.date = time.strftime("%Y/%m/%d - %H:%M:%S")
        self.video_name =self.date+"_"+self.user_id+"__"+self.contest_id + "__" + self.email.split("@")[0]
        self.names_user = names_user
        self.lastnames_user = lastnames_user

        self.status = status
        self.original_file = original_file


    def set_variables_db(self, dictionary):
        self.id= str(dictionary["_id"])
        self.user_id = str(dictionary["user_id"])
        self.contest_id = str(dictionary["project_id"])
        self.video_name = dictionary["video_name"]
        self.email = dictionary["email"]
        self.names_user = dictionary["names_user"]
        self.lastnames_user = dictionary["lastnames_user"]
        self.date = dictionary["date"]
        self.status = dictionary["status"]
        self.original_file = dictionary["original_file"]

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id), "user_id":self.user_id, "contest_id":self.contest_id, "video_name":self.video_name,
                "email":self.email, "names_user":self.names_user, "lastnames_user":self.lastnames_user,"date":self.date,
                "status":self.status,"original_file":self.original_file}

    def to_save(self):
        return {"user_id":self.user_id, "contest_id":self.contest_id, "video_name":self.video_name, "email":self.email,
                "names_user":self.names_user, "lastnames_user":self.lastnames_user,"date":self.date, "status":self.status,
                "original_file":self.original_file}