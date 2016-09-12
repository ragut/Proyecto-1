from ..model.Contest import Contest
from .VideoController import VideoController
from .DatabasesService import DatabasesController

class ContestController():

    database = None

    def __init__(self):
        self.database = DatabasesController()

#//---- INSERTA CONCURSO    -----//
    def insertContest(self, user_id, name, date_ini, deadline, description):
        contest = Contest()
        contest.set_variables_contest(user_id, name, date_ini, deadline, description)
        return self.database.createContest(contest)

#//---- OBTIENE CONCURSOS POR USUARIO   ----//
    def getUserContest(self, user_id):
        data = self.database.getUserContest(user_id)
        contests = []
        for contest in data:
            newContest = Contest()
            newContest.set_variables_db(contest)
            newContest.set_num_video(self.getContestVideoNumber(newContest.id))
            contests.append(newContest)
        return contests

#//-----    OBTIENE CONCURSO ESPECIFICO ----//
    def getContest(self, contest_id):
        data = self.database.getContest(contest_id)
        contest = Contest()
        contest.set_variables_db(data)
        contest.set_num_video(self.getContestVideoNumber(contest.id))
        return contest

#//-----    ACTUALIZA CONCURSO ESPECIFICO ----//
    def updateContest(self, id, user_id,  name, date_ini, deadline, description):
        contest = Contest()
        contest.set_variables_contest(user_id,  name, date_ini, deadline, description)
        contest.set_id(id)
        return self.database.updateContest(contest)

#//-----    ELIMINA CONCURSO ESPECIFICO ----//
    def deleteContest(self, id):
        VideoController().deleteContestVideo(id)
        return self.database.deleteContest(id)

#//-----    OBTIENE NUMERO DE VIDEOS POR CONCURSO ----//
    def getContestVideoNumber(self, contest_id):
        return self.database.getContestVideoNumber(contest_id)
