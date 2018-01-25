import xbmc
import xbmcgui


class TestDialog(xbmcgui.WindowXMLDialog):

	def __init__(self, xml_filename, xml_path):
		
		xbmc.log("TestDialog.__init__: xmlpath=" + xml_path + "; xmlfile=" + xml_filename, xbmc.LOGWARNING)    
		
		xbmcgui.WindowXMLDialog.__init__(self, xml_filename, xml_path)
		
		self.title       = ''
		self.editLabel   = ''
		self.editText    = ''
		self.initLabel   = False
		self.initText    = False
		self.closeButton = 0
		
		self.title_label_id      = 1001		
		self.editor_id           = 1012
		self.close_button_id     = 1091
		self.initedit1_button_id = 1092
		self.initedit2_button_id = 1093
		self.buttonList          = [self.close_button_id, self.initedit1_button_id, self.initedit2_button_id]
		self.runningButton       = -1
		
		xbmc.log("TestDialog.__init__: done", xbmc.LOGWARNING)    

	def onInit(self):
		
		xbmc.log("TestDialog.onInit: setTitleLabel", xbmc.LOGWARNING)    
		self.getControl(self.title_label_id).setLabel(self.title)
		if self.initLabel:
			xbmc.log("TestDialog.onInit: setEditorLabel", xbmc.LOGWARNING)    
			self.getControl(self.editor_id).setLabel(self.editLabel)
		if self.initText:
			xbmc.log("TestDialog.onInit: setEditorText", xbmc.LOGWARNING)    
			self.getControl(self.editor_id).setText(self.editText)
		xbmc.log("TestDialog.onInit: done", xbmc.LOGWARNING)    
	
	def configure(self, title, editLabel, editText, initLabel, initText):
		
		xbmc.log("TestDialog.configure: begin", xbmc.LOGWARNING)    
		self.title     = title
		self.editLabel = editLabel
		self.editText  = editText
		self.initLabel = initLabel
		self.initText  = initText
		xbmc.log("TestDialog.configure: done", xbmc.LOGWARNING)    
		
	def onClick(self, controlID):

		xbmc.log("TestDialog.onClick(controlID=" + str(controlID) + ")", xbmc.LOGWARNING)
		
		if controlID == self.close_button_id:
			self.close()
			
		elif controlID in self.buttonList:
			self.runningButton = self.buttonList.index(controlID)
		
			if self.runningButton == 0:
				self.close()
			elif self.runningButton == 1:
				xbmc.log("TestDialog.onClick: setEditorLabel", xbmc.LOGWARNING)    
				self.getControl(self.editor_id).setLabel('button editLabel')
			elif self.runningButton == 2:
				xbmc.log("TestDialog.onClick: setEditorText", xbmc.LOGWARNING)    
				self.getControl(self.editor_id).setText('button editText')

			
	def onClose(self):
		xbmc.log("TestDialog.onClose", xbmc.LOGWARNING)
		self.close()
	
	def close(self):
		xbmc.log("TestDialog.close", xbmc.LOGWARNING)	
		xbmcgui.WindowXMLDialog.close(self)
