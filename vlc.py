import os
import subprocess

def play(mov, *subs, **keyword_parameters):
        if ('subs' in keyword_parameters):
#            print 'subs found, it is', keyword_parameters['subs']
            msub="""cp '{}' {}""".format(
                    keyword_parameters['subs'], 
                        os.path.splitext(mov)[0] + '.srt')
            p = subprocess.Popen(msub, shell=True)
            args="""open -a vlc '{}'""".format(mov)
            p = subprocess.Popen(args, shell=True)
        else:
            args="""open -a vlc '{}'""".format(mov)
            p = subprocess.Popen(args, shell=True)

play('movie.mp4',subs='subtitles.srt') # .srt file is optional, will just play without subtitles if left out
# As always, movie and subtitles should be in the same directory, but here they do not have to share the same name.
# The code will rename any subtitle to match video file

