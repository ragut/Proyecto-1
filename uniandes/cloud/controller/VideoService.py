import ffmpy


class VideoService:

    def process_video(self, file_url, converted_url, input_file_name, input_file_extension):
        ff = ffmpy.FFmpeg(inputs={file_url+input_file_name+'.'+input_file_extension: None},
                          outputs={converted_url+input_file_name+'.mp4': None})
        ff.run()