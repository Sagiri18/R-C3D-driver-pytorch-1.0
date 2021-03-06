# --------------------------------------------------------
# R-C3D
# Copyright (c) 2017 Boston University
# Licensed under The MIT License [see LICENSE for details]
# Written by Huijuan Xu
# --------------------------------------------------------

import json
import os

annotation_file = open('/content/R-C3D-driver-master/preprocess/activitynet/activity_net.v1-3.min.json')
annotation = json.load(annotation_file)

video_database = annotation['database']
videos = annotation['database'].keys()

# Download the ActivityNet videos into the ./videos folder
path = "/content/R-C3D-driver-master/ActivityNet"
os.chdir(path)
command1 = 'mkdir '+'ActivityNetVideos'
os.system(command1)

for i in videos:
    url = video_database[i]['url']
    command3 = "youtube-dl -o " + 'ActivityNetVideos/'+i+' '+url
    print(command3)
    os.system(command3)



