import os
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import zipfile
import struct
import shutil

AppVersion = "1.0.0"
AppEdition = "py38"

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtWidgets.QStyleFactory, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

os.environ["QT_ENABLE_HIGHDPI_SCALING"]   = "1"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCALE_FACTOR"]             = "1"

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(453, 302)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
        MainWindow.setWindowIcon(QtGui.QIcon("resources/img/icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 391, 121))
        self.groupBox.setObjectName("groupBox")
        self.LabelCombinerInput = QtWidgets.QLabel(self.groupBox)
        self.LabelCombinerInput.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.LabelCombinerInput.setObjectName("LabelCombinerInput")
        self.ComboCombinerInput = QtWidgets.QComboBox(self.groupBox)
        self.ComboCombinerInput.setGeometry(QtCore.QRect(10, 40, 371, 21))
        self.ComboCombinerInput.setObjectName("ComboCombinerInput")
        self.ComboCombinerInput.addItem("")
        self.ComboCombinerInput.addItem("")
        self.ComboCombinerInput.addItem("")
        self.ComboCombinerInput.addItem("")
        self.LabelCombinerOutput = QtWidgets.QLabel(self.groupBox)
        self.LabelCombinerOutput.setGeometry(QtCore.QRect(10, 60, 371, 21))
        self.LabelCombinerOutput.setObjectName("LabelCombinerOutput")
        self.ComboCombinerOutput = QtWidgets.QComboBox(self.groupBox)
        self.ComboCombinerOutput.setGeometry(QtCore.QRect(10, 80, 371, 21))
        self.ComboCombinerOutput.setObjectName("ComboCombinerOutput")
        self.ComboCombinerOutput.addItem("")
        self.ComboCombinerOutput.addItem("")
        self.ComboCombinerOutput.addItem("")
        self.ComboCombinerOutput.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 391, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.LabelPathInput = QtWidgets.QLabel(self.groupBox_2)
        self.LabelPathInput.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.LabelPathInput.setObjectName("LabelPathInput")
        self.LabelPathOutput = QtWidgets.QLabel(self.groupBox_2)
        self.LabelPathOutput.setGeometry(QtCore.QRect(10, 60, 371, 21))
        self.LabelPathOutput.setObjectName("LabelPathOutput")
        self.LinePathInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.LinePathInput.setGeometry(QtCore.QRect(10, 40, 341, 21))
        self.LinePathInput.setObjectName("LinePathInput")
        self.LinePathOutput = QtWidgets.QLineEdit(self.groupBox_2)
        self.LinePathOutput.setGeometry(QtCore.QRect(10, 80, 341, 21))
        self.LinePathOutput.setObjectName("LinePathOutput")
        self.ButtonPathInput = QtWidgets.QPushButton(self.groupBox_2)
        self.ButtonPathInput.setGeometry(QtCore.QRect(349, 39, 33, 23))
        self.ButtonPathInput.setObjectName("ButtonPathInput")
        self.ButtonPathOutput = QtWidgets.QPushButton(self.groupBox_2)
        self.ButtonPathOutput.setGeometry(QtCore.QRect(349, 79, 33, 23))
        self.ButtonPathOutput.setObjectName("ButtonPathOutput")
        self.ButtonFix = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonFix.setGeometry(QtCore.QRect(10, 270, 391, 23))
        self.ButtonFix.setObjectName("ButtonFix")
        self.ButtonLang = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonLang.setGeometry(QtCore.QRect(420, 10, 24, 24))
        self.ButtonLang.setText("")
        self.ButtonLang.setObjectName("ButtonLang")
        self.ButtonLang.setVisible(False)
        self.ButtonInfo = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonInfo.setGeometry(QtCore.QRect(420, 10, 24, 24))
        self.ButtonInfo.setText("")
        self.ButtonInfo.setObjectName("ButtonLang")
        self.ButtonInfo.setIcon(QtGui.QIcon("resources/img/info.png"))
        self.ButtonGitHub = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGitHub.setGeometry(QtCore.QRect(420, 38, 24, 24))
        self.ButtonGitHub.setText("")
        self.ButtonGitHub.setObjectName("ButtonLang")
        self.ButtonGitHub.setIcon(QtGui.QIcon("resources/img/github.png"))
        self.SeparatorOrSmth = QtWidgets.QFrame(self.centralwidget)
        self.SeparatorOrSmth.setGeometry(QtCore.QRect(410, 10, 3, 281))
        self.SeparatorOrSmth.setFrameShape(QtWidgets.QFrame.VLine)
        self.SeparatorOrSmth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SeparatorOrSmth.setObjectName("SeparatorOrSmth")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.ComboCombinerInput.setCurrentIndex(2)
        self.ComboCombinerOutput.setCurrentIndex(1)
        
        self.ButtonPathInput.clicked.connect(self.ChooseInputPath)
        self.ButtonPathOutput.clicked.connect(self.ChooseOutputPath)
        self.ButtonGitHub.clicked.connect(self.OpenGitHubPage)
        self.ButtonFix.clicked.connect(self.Initiate)
        self.ButtonInfo.clicked.connect(self.AboutWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SM64 Save State Fixer {}".format(AppVersion)))
        self.groupBox.setTitle(_translate("MainWindow", "Color combiner command"))
        self.LabelCombinerInput.setText(_translate("MainWindow", "Input:"))
        self.ComboCombinerInput.setItemText(0, _translate("MainWindow", "Solid RGBA texture without fog (FC 12 7E 24 FF FF F9 FC)"))
        self.ComboCombinerInput.setItemText(1, _translate("MainWindow", "Alpha RGBA texture without fog (FC 12 18 24 FF 33 FF FF)"))
        self.ComboCombinerInput.setItemText(2, _translate("MainWindow", "[Default] Solid RGBA texture with fog (FC 12 7F FF FF FF F8 38)"))
        self.ComboCombinerInput.setItemText(3, _translate("MainWindow", "Alpha RGBA texture with fog (FC FF FF FF FF FC F2 38)"))
        self.LabelCombinerOutput.setText(_translate("MainWindow", "Output:"))
        self.ComboCombinerOutput.setItemText(0, _translate("MainWindow", "Solid RGBA texture without fog (FC 12 7E 24 FF FF F9 FC)"))
        self.ComboCombinerOutput.setItemText(1, _translate("MainWindow", "[Default] Alpha RGBA texture without fog (FC 12 18 24 FF 33 FF FF)"))
        self.ComboCombinerOutput.setItemText(2, _translate("MainWindow", "Solid RGBA texture with fog (FC 12 7F FF FF FF F8 38)"))
        self.ComboCombinerOutput.setItemText(3, _translate("MainWindow", "Alpha RGBA texture with fog (FC FF FF FF FF FC F2 38)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Paths"))
        self.LabelPathInput.setText(_translate("MainWindow", "Input:"))
        self.LabelPathOutput.setText(_translate("MainWindow", "Output:"))
        self.ButtonPathInput.setText(_translate("MainWindow", "…"))
        self.ButtonPathOutput.setText(_translate("MainWindow", "…"))
        self.ButtonFix.setText(_translate("MainWindow", "Fix"))
    
    def ChooseInputPath(self, MainWindow):
        InputPath = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Save State", os.getcwd(), "ZIP file (*.zip);;PJ file (*.pj)")
        if InputPath[0] == "":
            return
        else:
            self.LinePathInput.setText(InputPath[0])
    
    def ChooseOutputPath(self, MainWindow):
        ChooseOutputPathAppearAt = os.getcwd()
        if not os.path.isdir(self.RemoveAfterLastSlash(self, self.LinePathInput.text())):
            pass
        else:
            ChooseOutputPathAppearAt = self.SplitFormat(self, self.LinePathInput.text())[0] + "_fixed"
            
        ChooseOutputPathCurrentFormat = ""
        ChooseOutputPathChooseFormat = "ZIP file (*.zip);;PJ file (*.pj)".format(self.SplitFormat(self, self.LinePathInput.text())[1])
        
        OutputPath = QtWidgets.QFileDialog.getSaveFileName(self, "Choose where to save, and what format and name to use", ChooseOutputPathAppearAt, ChooseOutputPathChooseFormat)
        if OutputPath[0] == "":
            return
        else:
            self.LinePathOutput.setText(OutputPath[0])
    
    def RemoveAfterLastSlash(self, MainWindow, String):
        if String.rfind('/') != -1:
            return String[:String.rfind('/')]
        else:
            return String
    
    def SplitFormat(self, MainWindow, FilePath):
        Parts = FilePath.rsplit('.', 1)
        if len(Parts) > 1:
            return Parts[0], Parts[-1]
        else:
            return ''
    
    def OpenGitHubPage(self, MainWindow):
        webbrowser.open("https://github.com/vazhka-dolya/sm64_save_state_fixer")
    
    def Initiate(self, MainWindow):
        self.EnableButtons(self, False)
        # Original bytes to be replaced in big endian
        if self.ComboCombinerInput.currentIndex() == 0: # Solid RGBA texture without fog (FC 12 7E 24 FF FF F9 FC)
            original_bytes_big_endian = b"\xFC\x12\x7E\x24\xFF\xFF\xF9\xFC"
            
        elif self.ComboCombinerInput.currentIndex() == 1: # Alpha RGBA texture without fog (FC 12 18 24 FF 33 FF FF)
            original_bytes_big_endian = b"\xFC\x12\x18\x24\xFF\x33\xFF\xFF"
            
        elif self.ComboCombinerInput.currentIndex() == 2: # Solid RGBA texture with fog (FC 12 7F FF FF FF F8 38)
            original_bytes_big_endian = b"\xFC\x12\x7F\xFF\xFF\xFF\xF8\x38"
            
        elif self.ComboCombinerInput.currentIndex() == 3: # Alpha RGBA texture with fog (FC FF FF FF FF FC F2 38)
            original_bytes_big_endian = b"\xFC\xFF\xFF\xFF\xFF\xFC\xF2\x38"
        
        else:
            print("wtf???")
            
        # Replacement bytes in big endian
        if self.ComboCombinerOutput.currentIndex() == 0: # Solid RGBA texture without fog (FC 12 7E 24 FF FF F9 FC)
            replacement_bytes_big_endian = b"\xFC\x12\x7E\x24\xFF\xFF\xF9\xFC"
            
        elif self.ComboCombinerOutput.currentIndex() == 1: # Alpha RGBA texture without fog (FC 12 18 24 FF 33 FF FF)
            replacement_bytes_big_endian = b"\xFC\x12\x18\x24\xFF\x33\xFF\xFF"
            
        elif self.ComboCombinerOutput.currentIndex() == 2: # Solid RGBA texture with fog (FC 12 7F FF FF FF F8 38)
            replacement_bytes_big_endian = b"\xFC\x12\x7F\xFF\xFF\xFF\xF8\x38"
            
        elif self.ComboCombinerOutput.currentIndex() == 3: # Alpha RGBA texture with fog (FC FF FF FF FF FC F2 38)
            replacement_bytes_big_endian = b"\xFC\xFF\xFF\xFF\xFF\xFC\xF2\x38"
        
        else:
            print("wtf???")

        # Open the input file in binary mode
        if self.LinePathInput.text().endswith(".pj") == True:
            with open(self.LinePathInput.text(), 'rb') as f:
                # Read the entire file
                data = f.read()
        elif self.LinePathInput.text().endswith(".zip") == True:
            if os.path.exists("temp") == False:
                os.mkdir("temp")
            SaveZip = zipfile.ZipFile(self.LinePathInput.text(), "r")
            SaveZipName = zipfile.ZipFile(self.LinePathInput.text(), "r").namelist()[0]
            SaveZip.extractall("temp")
            with open("temp/" + SaveZipName, 'rb') as f:
                # Read the entire file
                data = f.read()
        else:
            return

        # Convert from little endian to big endian (assuming the data is 32-bit integers)
        # Note: The conversion method used here is a simple byte swap for each 4-byte sequence.
        #       This is a simplification and might not apply to all data formats.
        data_big_endian = bytearray()
        for i in range(0, len(data), 4):
            chunk = data[i:i+4]
            # Swap the bytes
            data_big_endian.extend(struct.pack('>I', struct.unpack('<I', chunk)[0]))

        # Convert the bytearray back to bytes
        data_big_endian = bytes(data_big_endian)

        # Replace the specified bytes
        data_modified_big_endian = data_big_endian.replace(original_bytes_big_endian, replacement_bytes_big_endian)

        # Convert back to little endian
        data_modified_little_endian = bytearray()
        for i in range(0, len(data_modified_big_endian), 4):
            chunk = data_modified_big_endian[i:i+4]
            # Swap the bytes back
            data_modified_little_endian.extend(struct.pack('<I', struct.unpack('>I', chunk)[0]))

        # Convert the bytearray back to bytes
        data_modified_little_endian = bytes(data_modified_little_endian)

        # Save the modified data to a new file
        if self.LinePathOutput.text().endswith(".pj") == True:
            with open(self.LinePathOutput.text(), 'wb') as f:
                f.write(data_modified_little_endian)
        else:
            with open(SaveZipName, 'wb') as f:
                f.write(data_modified_little_endian)
                with zipfile.ZipFile(self.LinePathOutput.text(), "w") as ZipFixed:
                    ZipFixed.write(SaveZipName)
        
        # Delete temporary files
        shutil.rmtree("temp")
        if self.LinePathOutput.text().endswith(".zip") == True:
            os.remove(SaveZipName)
        
        global msgbox
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Finished")
        msgbox.setText("The changes were successfully applied to the save state and it was saved as: {}\nDo you want to see it in the file manager?".format(self.LinePathOutput.text()))
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.Yes)
        msgbox.buttonClicked.connect(self.LocateFile)
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowIcon(QtGui.QIcon("img/icon.png"))
        runmsgbox = msgbox.exec_()
        self.EnableButtons(self, True)
    
    def LocateFile(self):
        global msgbox
        if msgbox.clickedButton().text() == "&Yes":
            os.startfile(self.RemoveAfterLastSlash(self, self.LinePathOutput.text()))
        else:
            pass
    
    def EnableButtons(self, MainWindow, Boolean):
        if (Boolean == True) or (Boolean == False):
            self.LinePathInput.setEnabled(Boolean)
            self.LinePathOutput.setEnabled(Boolean)
            self.ButtonPathInput.setEnabled(Boolean)
            self.ButtonPathOutput.setEnabled(Boolean)
            self.ComboCombinerInput.setEnabled(Boolean)
            self.ComboCombinerOutput.setEnabled(Boolean)
            self.ButtonFix.setEnabled(Boolean)
        else:
            #print("Incorrect argument for EnableButtons used: \"{}\"".format(Boolean))
            pass
    
    def AboutWindow(self, MainWindow):
        msgboxabo = QtWidgets.QMessageBox()
        msgboxabo.setWindowTitle("About")
        msgboxabo.setText("SM64 Save State Fixer\nVersion: {}\nEdition: {}\nWritten by vazhka-dolya on GitHub (aka DanilAstroid pretty much anywhere else)\nLicensed under the Do What The Fuck You Want To Public License\n\nCredits:\n• GlitchyPSI – explaining to me how to fix black textures in save states.\n• HuggingChat (an AI) – writing the actual code for fixing black textures because I'm still too dumb to write that myself💀.\n\nThis program is not affiliated with or sponsored by Nintendo and does not use any of Nintendo's intellectual property.".format(AppVersion, AppEdition))
        msgboxabo.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgboxabo.setIconPixmap(QtGui.QPixmap("resources/img/icon.png"))
        msgboxabo.setWindowIcon(QtGui.QIcon("resources/img/info.png"))
        runmsgboxabo = msgboxabo.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
