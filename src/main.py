from picasa import Picasa

albums = Picasa.get_albums_list()


for album in albums:
    print 'Downloading', album
    Picasa.download_album(album, '/home/oleksandr/picasa_albums/')


# Picasa.upload_folder_as_album('/home/oleksandr/Pictures/photo/fototmp/frame/')