import os
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon

from .wizard.wizard_dialog import PluginWizardDialog


class PluginBuilderEnterprise:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.translator = None

    def initTranslator(self):
        locale = QSettings().value("locale/userLocale", "it")[0:2]

        self.translator = QTranslator()

        path = os.path.join(self.plugin_dir, "resources", "i18n")
        filename = f"plugin_builder_enterprise_{locale}.qm"

        print("[PBE] Loading:", os.path.join(path, filename))

        if self.translator.load(filename, path):
            QCoreApplication.installTranslator(self.translator)
            print("[PBE] OK:", filename)
        else:
            print("[PBE] FAIL:", filename)

    def initGui(self):
        self.initTranslator()  # <--- PRIMA DI CREARE QAction

        icon_path = os.path.join(self.plugin_dir, "resources", "images", "icon.png")
        icon = QIcon(icon_path)

        self.action = QAction(icon, self.tr("Plugin Builder Enterprise"), self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(self.tr("&Plugin Builder Enterprise"), self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu(self.tr("&Plugin Builder Enterprise"), self.action)

    def run(self):
        dlg = PluginWizardDialog(self.iface)
        dlg.exec()

    def tr(self, message):
        return QCoreApplication.translate("PluginBuilderEnterprise", message)
