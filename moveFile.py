# ID of destination folder 569a5d73-3e2f-4a69-b02f-d5f22497ef86

import os
import requests


def moveFile (node, parent):
    url = "http://ec2-54-87-74-170.compute-1.amazonaws.com/alfresco/api/-default-/public/alfresco/versions/1/nodes/"+node+"/move"

    dat = '{ "targetParentId": "'+ parent +'"}'

    temp = requests.post(url, data = dat, auth = ('admin', 'Alfresco01'))

    print (temp)


moveFile('e2bcf6c4-88e8-44d3-bdf0-41aa80890fa4','569a5d73-3e2f-4a69-b02f-d5f22497ef86')