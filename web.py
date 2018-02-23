# -*- coding: utf-8 -*-
#!/usr/bin/python
# filename: GETPOST_test.py
# codedtime: 2014-9-20 19:07:04
 
 
import bottle
import base64
import re
import cv2
import numpy as np
 
@bottle.route('/login')
def login():
  return ''' <form action="/login" method="post">
         Username: <input name="username" type="text" />
         Password: <input name="password" type="password" />
         <input value="Login" type="submit">
        </form>
      '''
 
@bottle.route('/login', method='POST')
def do_login():

  #第二种方式
    #postValue = bottle.request.POST.decode('utf-8')
    #hintDataURL = bottle.request.POST.get('hide')
    hintDataURL = bottle.request.forms.get("hint")
    hintDataURL = re.sub('^data:image/.+;base64,', '', hintDataURL)
    hintDataURL = base64.urlsafe_b64decode(hintDataURL)
    hintDataURL = np.fromstring(hintDataURL, dtype=np.uint8)
    hintDataURL = cv2.imdecode(hintDataURL, -1)
    hstr = str(np.random.randint(100, 999))
    cv2.imwrite('record/' + hstr + '.hint.png', hintDataURL)  
  
    return 'record/' + '_' + hstr + '.hint.png'
 
bottle.run(host='localhost', port=8080)                                          #表示本机，接口是8080 