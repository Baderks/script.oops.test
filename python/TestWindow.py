import xbmc
import xbmcaddon
import xbmcgui
from TestDialog import TestDialog

class TestWindow(xbmcgui.WindowXML):

	def __init__(self, xml_filename, xml_path):
		
		xbmc.log("TestWindow.__init__: xmlpath=" + xml_path + "; xmlfile=" + xml_filename, xbmc.LOGWARNING)    
		
		xbmcgui.WindowXML.__init__(self, xml_filename, xml_path)
		
		self.title               = ''
		self.testLabel1          = ''
		self.testLabel2          = ''
		self.testLabel3          = ''
		self.title_label_id      = 1000		
		self.label1_id           = 1019
		self.label2_id           = 1029
		self.label3_id           = 1039
		self.stop_button_id      = 1091
		self.skipping_button_id  = 1092
		self.initedit1_button_id = 1093		
		self.initedit2_button_id = 1094		
		self.initedit3_button_id = 1095		
		self.buttonList          = [self.stop_button_id, self.skipping_button_id, self.initedit1_button_id, self.initedit2_button_id, self.initedit3_button_id]
		self.runningButton       = -1

	def onInit(self):
		
		xbmc.log("TestWindow.onInit: start", xbmc.LOGWARNING)    
		self.setProperty('ShowTestWindow', "true")
		self.getControl(self.title_label_id).setLabel(self.title)
		self.getControl(self.label1_id).setLabel(self.testLabel1)
		self.getControl(self.label2_id).setLabel(self.testLabel2)
		self.getControl(self.label3_id).setLabel(self.testLabel3)
		xbmc.log("TestWindow.onInit: done", xbmc.LOGWARNING)    
	
	def configure(self, title, testLabel1, testLabel2, testLabel3):
		
		xbmc.log("TestWindow.configure: start", xbmc.LOGWARNING)    
		self.title      = title
		self.testLabel1 = testLabel1
		self.testLabel2 = testLabel2
		self.testLabel3 = testLabel3
		xbmc.log("TestWindow.configure: done", xbmc.LOGWARNING)    
	
	def onClick(self, controlID):

		xbmc.log("TestWindow.onClick(controlID=" + str(controlID) + ")", xbmc.LOGWARNING)
		
		if controlID in self.buttonList:
			self.runningButton = self.buttonList.index(controlID)
			
			if self.runningButton == 0:
				self.onClose()
			elif self.runningButton == 1:
				self.showTestDialog(False, False)			
			elif self.runningButton == 2:
				self.showTestDialog(True, False)			
			elif self.runningButton == 3:
				self.showTestDialog(False, True)			
			elif self.runningButton == 4:
				self.showTestDialog(True, True)			
			
	def onClose(self):
		xbmc.log("TestWindow.onClose", xbmc.LOGWARNING)
		self.close()
	
	def close(self):
		xbmc.log("TestWindow.close", xbmc.LOGWARNING)	
		xbmcgui.WindowXML.close(self)
		
	def showTestDialog(self, initLabel, initText):
		
		self.setProperty('ShowTestWindow', "false")
		
		addon     = xbmcaddon.Addon()
		addonname = addon.getAddonInfo('name')
		addonpath = addon.getAddonInfo('path').decode('utf-8')
		xmlfile   = 'TestDialog.xml'
		
		xbmc.log("TestWindow.showTestDialog: create TestDialog", xbmc.LOGWARNING)
		
		testDialog = TestDialog(xmlfile, addonpath)
		
		xbmc.log("TestWindow.showTestDialog: TestDialog.configure", xbmc.LOGWARNING)
		testDialog.configure('testDialog titel', 'init editLabel', 'init editText', initLabel, initText)		
		
		xbmc.log("TestWindow.showTestDialog: TestDialog.doModal", xbmc.LOGWARNING)
		testDialog.doModal()
		
		self.setProperty('ShowTestWindow', "true")
		
		xbmc.log("TestWindow.showTestDialog: delete TestDialog", xbmc.LOGWARNING)
		del testDialog
		
		line1 = "line one"
		line2 = "line two"
		line3 = "line three"
		 
		#xbmcgui.Dialog().ok(addonname, line1, line2, line3)
		
def run():
	
	addon     = xbmcaddon.Addon()
	addonname = addon.getAddonInfo('name')
	addonpath = addon.getAddonInfo('path').decode('utf-8')
	xmlfile   = 'TestWindow.xml'
	
	testWindow = TestWindow(xmlfile, addonpath)
		
	testWindow.configure('title of TestWindow', 'label1 of TestWindow', 'label2 of TestWindow', 'label3 of TestWindow')		
	
	testWindow.doModal()
	
	del testWindow
	
	line1 = "line one"
	line2 = "line two"
	line3 = "line three"

	#xbmcgui.Dialog().ok(addonname, line1, line2, line3)
		