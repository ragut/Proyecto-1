from ..filesystems.OwnMachine import OwnMachine


class FileSystemService():

    fileSystem = None

    def __init__(self):
        self.fileSystem = OwnMachine()

    def save_company_logo(self, img, logo_filename):
        self.fileSystem.save_company_logo(img, logo_filename)

    def save_original_video(self, img, video_name, original_file):
        self.fileSystem.save_original_video(img,video_name,original_file)

    def delete_video(self, video):
        self.fileSystem.delete_video(video)

    def save_converted_image(self, img, design):
        self.fileSystem.save_converted_image(img,design)

    def save_thumbnail_image(self, img, design):
        self.fileSystem.save_thumbnail_image(img,design)

    def get_original_url(self):
        return self.fileSystem.get_original_url()

    def get_converted_url(self):
        return self.fileSystem.get_converted_url()