from uniandes.cloud.controller.VideoController import VideoController
from uniandes.cloud.controller.VideoService import VideoService
from uniandes.cloud.controller.FileController import FileController
from uniandes.cloud.controller.MailService import MailService


print "Init File Processing"

video = VideoController().getVideoToProcess()
fileSystem = FileController()

if video is not None:
    if video.file_name is not None:
        print "Processing video with id " + video.id

        VideoService.process_video(fileSystem.get_original_url(), fileSystem.get_converted_url(), video.file_name, video.original_file_extension)
        VideoController().updateStatusVideo(video.id)
        MailService().sendMail(video.email, video.names, "contest=" + video.contest_id + "&user=" + video.user_id)
        print "Video processing finish!"
    else:
        print "Video filename corrupted"
else:
    print "All videos are processed"