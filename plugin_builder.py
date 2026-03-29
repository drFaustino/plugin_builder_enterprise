import os
from qgis.PyQt import QtCore, QtGui, QtWidgets
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon

from .wizard.wizard_dialog import PluginWizardDialog

class PluginBuilderEnterprise:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
    
    def initTranslator(self):
        locale = QtCore.QLocale.system().name()
        translator = QtCore.QTranslator()
        path = os.path.join(os.path.dirname(__file__), "resources", "i18n")
        if translator.load(f"plugin_builder_enterprise_{locale}.qm", path):
            QtCore.QCoreApplication.installTranslator(translator)

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "resources", "images", "icon.png")
        icon = QIcon(icon_path)

        self.action = QAction(icon, self.tr("Plugin Builder Enterprise"), self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(self.tr("&Plugin Builder Enterprise"), self.action)
        self.initTranslator()

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu(self.tr("&Plugin Builder Enterprise"), self.action)

    def run(self):
        dlg = PluginWizardDialog(self.iface)
        dlg.exec()

    def tr(self, message):
        return QtCore.QCoreApplication.translate("PluginBuilderEnterprise", message)
