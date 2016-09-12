import logging
import os
import tornado.ioloop
import tornado.web
import math


from uniandes.cloud.controller.UserController import UserController
from uniandes.cloud.controller.ContestController import ContestController
from uniandes.cloud.controller.VideoController import VideoController

logging.root.setLevel(logging.INFO)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        if not self.get_secure_cookie("user"):
            return None
        else:
            user = UserController().getUserFromDict(tornado.escape.json_decode(self.get_secure_cookie("user")))
        return user

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.current_user = None
        self.redirect("/")

class LoginHandler(BaseHandler):
    def get(self):
        self.render(settings["static_path"]+"/pages/login.html", error = False)

    def post(self):
        email = self.get_argument("inputEmail")
        password = self.get_argument("inputPassword")

        user = UserController().login_user(email, password)
        if user is not None:
            self.set_secure_cookie("user", tornado.escape.json_encode(user.to_dict()))
            if self.get_argument("next", None) is not None:
                self.redirect(self.get_argument("next"))
            else:
                self.redirect("/")
        else:
            self.clear_cookie("user")
            self.render(settings["static_path"]+"/pages/login.html", error = True)

class UserHandler(BaseHandler):
    def get(self):
        url = self.request.uri.replace("/user/","").split("?")[0]
        if url == "show-all":
            user = UserController().getUsers()
            pages = int(math.ceil(len(user)/9.0))
            self.render(settings["static_path"]+"/pages/all_users.html", user = user, pages=pages)
        else:
            user = UserController().getUserFromUrl(url)
            contest = ContestController().getUserContest(user.id)
            self.render(settings["static_path"]+"/pages/user_page.html", user = user, contest =contest)

class SignUpHandler(BaseHandler):
    def get(self):
        self.render(settings["static_path"]+"/pages/sign_up.html", error = False)

    def post(self):
        names = self.get_argument("userNames")
        lastnames = self.get_argument("userLastnames")
        email = self.get_argument("userEmail")
        password = self.get_argument("userPassword")
       # logo = self.request.files['companyLogo'][0]["body"]

        data = UserController().add_User(names, lastnames, email, password)

        if data is None:
            self.render(settings["static_path"]+"/pages/sign_up.html", error=True)
        else:
            self.render(settings["static_path"]+"/pages/new_user.html", names=data.names,
                        lastnames = data.lastnames, host = self.request.host)

class AdminHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        contest = ContestController().getUserContest(self.current_user.id)
        self.render(settings["static_path"]+"/pages/admin.html", user = self.current_user, contest=contest)

class ContestHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        url = self.request.uri.replace("/contest-admin/","").split("?")[0]
        if url == "new":
            self.render(settings["static_path"]+"/pages/new_contest.html",user = self.current_user)
        elif url == "edit":
            contest_id = self.get_argument("id")
            contest = ContestController().getContest(contest_id)
            if contest.user_id == self.current_user.id:
                self.render(settings["static_path"]+"/pages/edit_contest.html", company = self.current_user, contest = contest)
            else:
                self.render(settings["static_path"]+"/pages/other_user.html")
        elif url == "delete":
            contest_id = self.get_argument("id")
            contest = ContestController().getContest(contest_id)
            if contest.user_id == self.current_user.id:
                ContestController().deleteContest(contest_id)
                self.redirect("/admin")
            else:
                self.render(settings["static_path"]+"/pages/other_user.html")
        elif url == "view":
            contest_id = self.get_argument("id")
            contest = ContestController().getContest(contest_id)
            if contest.user_id == self.current_user.id:
                videos = VideoController().getContestVideo(contest_id)
                pages = int(math.ceil(len(videos)/9.0))
                self.render(settings["static_path"]+"/pages/view_contest.html",user = self.current_user, contest = contest,videos = videos, pages = pages)
            else:
                self.render(settings["static_path"]+"/pages/other_user.html")

    @tornado.web.authenticated
    def post(self):
        url = self.request.uri.replace("/project-admin/","")
        if url == "save":
            user_id = self.get_argument("inputUserId")
            name = self.get_argument("contestName")
           # url = self.get_argument("contestURL")
            date_ini = self.get_argument("contestIni")
            deadline = self.get_argument("contestDeadline")
            description = self.get_argument("contestDescription")

            if user_id == self.current_user.id:
                ContestController().insertContest(user_id, name, date_ini, deadline, description)#MOFDIFICAR
                self.redirect("/admin")
            else:
                self.render(settings["static_path"]+"/pages/other_user.html")
        elif url == "save-edit":
            id = self.get_argument("inputId")
            user_id = self.get_argument("inputUserId")
            name = self.get_argument("contestName")
            date_ini = self.get_argument("contestIni")
            deadline = self.get_argument("contestDeadline")
            description = self.get_argument("contestDescription")
            if user_id == self.current_user.id:
                ContestController().updateContest( id, user_id,  name, date_ini, deadline, description)
                self.redirect("/admin")
            else:
                self.render(settings["static_path"]+"/pages/other_user.html")

class VideoHandler(BaseHandler):
    def get(self):
        url = self.request.uri.replace("/video/","").split("?")[0]
        if url == "add":
            user_id = self.get_argument("user")
            contest_id = self.get_argument("contest")
            user = UserController().getUserId(user_id)
            contest = ContestController().getContest(contest_id)
            self.render(settings["static_path"]+"/pages/video.html", user = user, contest = contest, error = False)
        elif url == "show-all":
            videos = VideoController().getOkVideos()
            pages = int(math.ceil(len(videos)/9.0))
            self.render(settings["static_path"]+"/pages/all_videos.html",videos = videos, pages = pages)


    def post(self):
        url = self.request.uri.replace("/video/","").split("?")[0]
        if url == "save":
            contest_id = self.get_argument("inputId")
            user_id = self.get_argument("inputUserId")
            email = self.get_argument("Email")
            names_user = self.get_argument("Names")
            lastnames_user = self.get_argument("LastNames")

            video_file = self.request.files['fileVideo'][0]["body"]
            video = VideoController().createVideo(user_id, contest_id, email, names_user, lastnames_user, video_file)

            user = UserController().getUserId(user_id)
            contest = ContestController().getContest(contest_id)
            videos = VideoController().getContestOkVideos(contest_id)

            pages = int(math.ceil(len(videos)/9.0))

            if video is None:
                self.render(settings["static_path"]+"/pages/video.html", user = user, contest = contest, error = True)
            else:
                self.render(settings["static_path"]+"/pages/contest.html",user = user, contest = contest,videos = videos, video_upload=True, pages = pages)

class ContestPublicHandler(BaseHandler):
    def get(self):
        url = self.request.uri.replace("/video/","").split("?")[0]
        if url == "view":
            user_id = self.get_argument("user")
            contest_id = self.get_argument("contest")
            user = UserController().getUserId(user_id)
            contest = ContestController().getContest(contest_id)
            videos = VideoController().getContestOkVideos(contest_id)
            pages = int(math.ceil(len(videos)/9.0))
            self.render(settings["static_path"]+"/pages/contest.html",user = user, contest = contest,videos = videos, design_upload=False, pages = pages)

class MainHandler(BaseHandler):
    def get(self):
        user = UserController().getLatestUser()
        videos = VideoController().getLatestVideo()
        if not self.get_secure_cookie("user"):
            self.render(settings["static_path"]+"/index.html",user=user, videos=videos, login=False)
        else:
            self.render(settings["static_path"]+"/index.html",user=user, videos=videos, login=True, current_user=self.current_user)

settings = {"static_path": os.path.join(os.path.dirname(__file__),"web"),
            "debug": True,
            "cookie_secret": "YeEhlzg4S++zgdqmQnZM5a+VxX2TDUHOoiCN84A5D04=",
            "login_url": "/login"}

if __name__ == "__main__":
    logging.log(logging.INFO,'Init App Deployment...')

    logging.log(logging.INFO, 'Deploying service...')

    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/logout", LogoutHandler),
        (r"/sign-up", SignUpHandler),
        (r"/user/.*", UserHandler),
        (r"/contest-admin/.*", ContestHandler),
        (r"/contest/.*", ContestPublicHandler),
        (r"/video/.*", VideoHandler),
        (r"/admin", AdminHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler,
            {"path": settings["static_path"]})
    ], **settings)

    application.listen(8800)

    logging.log(logging.INFO, "Application ready")
    tornado.ioloop.IOLoop.current().start()