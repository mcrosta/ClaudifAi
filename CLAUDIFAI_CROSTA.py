#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os 
from PIL import Image

#Make the directory for images
os.mkdir("Final_Images")

ims = os.listdir("images")
xmls = os.listdir("xmldata")

for ii,im in enumerate(ims):
    pic = Image.open("images/"+im)
    xm = xmls[ii]
    
    tree = ET.parse("xmldata/"+xm) 
    root = tree.getroot() 
    
    width = int(root.find("size")[0].text)
    height = int(root.find("size")[1].text)
    
    #Define the bndbox boundaries
    xmin = int(root.find("bndbox")[0].text)
    ymin = int(root.find("bndbox")[1].text)
    xmax = int(root.find("bndbox")[2].text)
    ymax = int(root.find("bndbox")[3].text)
    
    x,y = pic.size
    if x > 800 or y > 450:
        smaller_pic = pic.resize((800,450))
        smaller_pic.save("Final_Images/"+im)
        
        #Change the bndbox boundaries
        #I'm not sure on how the image resize works
        xmin = xmin * (800/width)
        xmax = xmax * (800/width)
        ymin = ymin * (450/height)
        ymax = ymax * (450/height)
        
    else:
        pic.save("Final_Images/"+im)
        
    #Dovrei ora per ogni immagine salvare le informazioni all'interno del file. Non conosco questo formato di file e non 
    # riesco in questo a farlo.

