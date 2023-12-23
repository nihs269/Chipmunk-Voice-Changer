from media_editor import *
from chipmunk import *

extract_mp3_from_mp4('happybirthday.mp4', 'happybirthday.mp3')
chipmunk_audio('happybirthday.mp3', 'happybirthday.mp3', 12)
merge_mp3_to_mp4('happybirthday.mp4', '1.mp3', 'happybirthday_export.mp4')
