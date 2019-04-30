# Get access to any window on the desktop

from pywinauto import Application #for autowin
import pywinauto.keyboard
import time

lsAppPath = ""

#start the app
app = Application().start(lsAppPath)

#while the window does not exist
while not app.app():
      time.sleep(5)
      
      
#the title from the window we would like to access
lsWindowTitle = ""

#check if the window exists
if app.window_(title_re= lsWindowTitle).Exists():   
  #get the window
  Window = app[lsWindowTitle]
  
  #we imagin there is an edit with the text hallo
  #get the edit
  editCtrl = Window[u'MyEdit'] # we need the name of the edit
  lsText = editCtrl.TextBlock() # thats the important line 
  
  #now we would like to write into the text edit
  editCtrl.TypeKeys(u"Nothing")
