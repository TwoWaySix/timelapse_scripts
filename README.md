# ffmpeg

ffmpeg -framerate 30 -pattern_type glob -i "folder-with-photos/*.JPG" -s:v 1440x1080 -c:v libx264 -crf 17 -pix_fmt yuv420p my-timelapse.mp4
