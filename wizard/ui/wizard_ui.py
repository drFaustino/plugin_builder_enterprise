# -*- coding: utf-8 -*-

from qgis.PyQt import QtCore, QtGui, QtWidgets


class Ui_WizardDialog(object):
    def setupUi(self, WizardDialog):
        WizardDialog.setObjectName("WizardDialog")
        WizardDialog.resize(900, 580)
        WizardDialog.setWindowTitle("Plugin Builder Enterprise")

        # MAIN LAYOUT
        self.mainLayout = QtWidgets.QVBoxLayout(WizardDialog)
        self.mainLayout.setObjectName("mainLayout")

        # ─────────────────────────────────────────────
        # SAVE PATH FRAME
        # ─────────────────────────────────────────────
        self.SaveFrame = QtWidgets.QFrame(WizardDialog)
        self.SaveFrame.setObjectName("SaveFrame")
        self.SaveFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)

        self.saveLayout = QtWidgets.QHBoxLayout(self.SaveFrame)
        self.saveLayout.setObjectName("saveLayout")

        self.SaveLabel = QtWidgets.QLabel(self.SaveFrame)
        self.SaveLabel.setObjectName("SaveLabel")
        self.SaveLabel.setText("Save folder:")
        self.saveLayout.addWidget(self.SaveLabel)

        self.SavePath = QtWidgets.QLineEdit(self.SaveFrame)
        self.SavePath.setObjectName("SavePath")
        self.saveLayout.addWidget(self.SavePath)

        self.BrowseButton = QtWidgets.QPushButton(self.SaveFrame)
        self.BrowseButton.setObjectName("BrowseButton")
        self.BrowseButton.setText("Browse…")
        self.saveLayout.addWidget(self.BrowseButton)

        self.mainLayout.addWidget(self.SaveFrame)

        # ─────────────────────────────────────────────
        # MAIN FRAME (SIDEBAR + STACK)
        # ─────────────────────────────────────────────
        self.MainFrame = QtWidgets.QFrame(WizardDialog)
        self.MainFrame.setObjectName("MainFrame")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # SIDEBAR
        self.Sidebar = QtWidgets.QFrame(self.MainFrame)
        self.Sidebar.setObjectName("Sidebar")
        self.Sidebar.setMinimumWidth(220)
        self.Sidebar.setMaximumWidth(260)
        self.Sidebar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)

        self.sidebarLayout = QtWidgets.QVBoxLayout(self.Sidebar)
        self.sidebarLayout.setObjectName("sidebarLayout")

        self.StepList = QtWidgets.QListWidget(self.Sidebar)
        self.StepList.setObjectName("StepList")
        self.StepList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.sidebarLayout.addWidget(self.StepList)

        self.horizontalLayout.addWidget(self.Sidebar)

        # STACKED WIDGET
        self.Stack = QtWidgets.QStackedWidget(self.MainFrame)
        self.Stack.setObjectName("Stack")
        self.horizontalLayout.addWidget(self.Stack)

        self.mainLayout.addWidget(self.MainFrame)

        # ─────────────────────────────────────────────
        # EXTRA OPTION: CREATE BASE UI
        # ─────────────────────────────────────────────
        self.CreateBaseUiCheckBox = QtWidgets.QCheckBox(WizardDialog)
        self.CreateBaseUiCheckBox.setObjectName("CreateBaseUiCheckBox")
        self.CreateBaseUiCheckBox.setText("Create basic (empty) UI in ui/ folder")
        self.mainLayout.addWidget(self.CreateBaseUiCheckBox)

        # ─────────────────────────────────────────────
        # BUTTON BAR
        # ─────────────────────────────────────────────
        self.ButtonBar = QtWidgets.QFrame(WizardDialog)
        self.ButtonBar.setObjectName("ButtonBar")
        self.ButtonBar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        self.buttonLayout = QtWidgets.QHBoxLayout(self.ButtonBar)
        self.buttonLayout.setObjectName("buttonLayout")

        spacer = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.buttonLayout.addItem(spacer)

        self.Back = QtWidgets.QPushButton(self.ButtonBar)
        self.Back.setObjectName("Back")
        self.Back.setText("< Back")
        self.buttonLayout.addWidget(self.Back)

        self.Next = QtWidgets.QPushButton(self.ButtonBar)
        self.Next.setObjectName("Next")
        self.Next.setText("Next >")
        self.buttonLayout.addWidget(self.Next)

        self.Finish = QtWidgets.QPushButton(self.ButtonBar)
        self.Finish.setObjectName("Finish")
        self.Finish.setText("Generate Plugin")
        self.Finish.setDefault(True)
        self.buttonLayout.addWidget(self.Finish)

        self.Close = QtWidgets.QPushButton(self.ButtonBar)
        self.Close.setObjectName("Close")
        self.Close.setText("Close")
        self.buttonLayout.addWidget(self.Close)

        self.mainLayout.addWidget(self.ButtonBar)

        QtCore.QMetaObject.connectSlotsByName(WizardDialog)
