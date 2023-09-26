#!/usr/bin/env python3
from os import path, listdir
from subprocess import check_output
from sys import argv


def main():
    files = [f for f in listdir(argv[1]) if path.isfile(path.join(argv[1], f))]
    src_dir = path.dirname(argv[1])
    dest_dir = path.dirname(argv[2])
    for file in files:
        if file.split('.')[1] == 'flac':
            converted_file = file.split('.')[0]+'.mp3'
            print(f'Converting {path.join(src_dir,file)} to file {path.join(src_dir,converted_file)}')
            check_output(f'ffmpeg -i "{path.join(src_dir,file)}" -ab 320k -map_metadata 0 -id3v2_version 3 "{path.join(dest_dir,converted_file)}"',shell=True)
        else:
            print(f'Skipping {file} (not a flac)')
    print('All done')

if __name__ == '__main__':
    main()
