import os
import os.path

class OwnMachine():

    url_ori = None
    url_thumb = None
    url_converted = None
    ulr_logo = None

    def __init__(self):
        self.url_ori = os.path.abspath(__file__ + "/../../../../web/data/original")+"/"
        self.url_converted = os.path.abspath(__file__ + "/../../../../web/data/converted")+"/"
        self.ulr_banner = os.path.abspath(__file__ + "/../../../../web/data/banner")+"/"

    def save_contest_banner(self, img, banner_file):
        img.save(self.ulr_banner+banner_file,"png")
        img.close()

    def save_original_video(self, video, file_name, original_file_extension):
        os.mknod(self.url_ori+file_name+"."+original_file_extension)


    def delete_design(self, design):
        if os.path.exists(self.url_ori+design.file_name+'.'+design.original_file_extension):
                os.remove(self.url_ori+design.file_name+'.'+design.original_file_extension)
        if design.status == "OK":
            if os.path.exists(self.url_thumb+design.file_name+'.png'):
                os.remove(self.url_thumb+design.file_name+'.png')
            if os.path.exists(self.url_converted+design.file_name+'.png'):
                os.remove(self.url_converted+design.file_name+'.png')

    def save_converted_image(self, img, design):
        img.save(self.url_converted+design.file_name+'.png','png')
        img.close()

    def save_thumbnail_image(self, img, design):
        img.save(self.url_thumb+design.file_name+'.png','png')
        img.close()

    def get_converted_url(self):
        return self.url_converted

    def get_original_url(self):
        return self.url_ori


