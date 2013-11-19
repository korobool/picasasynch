import os
import subprocess


class Picasa(object):
    @classmethod
    def get_albums_list(cls):
        p = subprocess.Popen(['google', 'picasa', 'list-albums'], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()

        albums = out.split('\n')

        albums = dict(filter(lambda item: len(item) == 2 and item[0] != '' and item[1] != '',
                             map(lambda item:
                                 item.split(','),
                                 albums)))

        return albums

    @classmethod
    def download_album(cls, album, path):
        cls.verify_path(path)
        cmd = ['google', 'picasa', 'get', album, path]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()

    @classmethod
    def verify_path(cls, path):
        if not os.path.exists(path):
            os.makedirs(path)

    @classmethod
    def upload_folder_as_album(cls, folder_path, name=''):
        #if name != '':
        #    name = folder_path
        #cmd = ['google', 'picasa', 'create', 'aaa', folder_path+'*.jpg']
        #p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
        #                     stderr=subprocess.PIPE)
        #out, err = p.communicate()
        pass


