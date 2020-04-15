#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


cap = cv2.VideoCapture(0)


# In[3]:


cascade_file = 'haarcascade_frontalface_alt.xml' 
cascade = cv2.CascadeClassifier(cascade_file)


# In[4]:


while True:
    _, frame = cap.read()
    frame = cv2.resize(src=frame, dsize=(500,300))
    face_list = cascade.detectMultiScale(frame)
    if len(face_list) == 0:
        quit()
    for (x,y,w,h) in face_list:
        cv2.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(0,0,255), thickness=4)
    cv2.imshow('web_camera', frame)
    if cv2.waitKey(30) == 13:
        break
cap.release()
cv2.destroyAllWindows()

