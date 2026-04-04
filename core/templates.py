BASE_INIT = """# -*- coding: utf-8 -*-
def classFactory(iface):
    from .{{plugin_dir_name}} import PluginMain
    return PluginMain(iface)
"""

BASE_PLUGIN_MAIN = """# -*- coding: utf-8 -*-
from qgis.PyQt import QtWidgets


class PluginMain:
    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):
        self.action = QtWidgets.QAction("{{plugin_name}}", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("{{plugin_name}}", self.action)

    def unload(self):
        self.iface.removePluginMenu("{{plugin_name}}", self.action)

    def run(self):
        QtWidgets.QMessageBox.information(
            self.iface.mainWindow(),
            "{{plugin_name}}",
            "Plugin {{plugin_name}} is running."
        )
"""

BASE_UI = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>{{plugin_name}}Widget</class>
 <widget class="QWidget" name="{{plugin_name}}Widget">
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QLabel" name="label">
     <property name="text">
      <string>{{plugin_name}} base UI</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QCheckBox" name="exampleCheckBox">
     <property name="text">
      <string>Example checkbox</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

METADATA = """[general]
name={{plugin_name}}
about={{about}}
category=Plugins
hasProcessingProvider={{has_processing}}
description={{description}}
icon=resources/images/{{icon_name}}
tags={{tags}}

author={{author}}
email={{email}}
homepage={{homepage}}
repository={{repository}}
tracker={{tracker}}

deprecated=False
experimental={{experimental}}
plugin_dependencies={{plugin_dependencies}}
qgisMinimumVersion={{qgis_min}}
qgisMaximumVersion={{qgis_max}}
supportsQt6=True

version={{version}}
changelog=
  Version {{version}}:
    - Initial public release generated with Plugin Builder Enterprise.
"""

README = """# {{plugin_name}}

{{description}}

## About
{{about}}

## Author
{{author}} <{{email}}>

## Repository
- Homepage: {{homepage}}
- Repository: {{repository}}
- Tracker: {{tracker}}
"""

# MIT LICENSE
LICENSE_MIT = """MIT License

Copyright (c) {{year}} {{author}}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

(omitted for brevity)
"""

# GPL v3 LICENSE
LICENSE_GPL = """{{plugin_name}} – QGIS Plugin
Copyright (C) {{year}}
{{author}}
Email: {{email}}

This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.

---

This plugin uses:
- QGIS API (GPL-compatible)
- GDAL/OGR (MIT/X license)
- NumPy (BSD license)
- Matplotlib (PSF license)

By using, modifying, or distributing this software, you agree to the terms of the GPL.

---

Summary (non‑binding):

- You may use, study, modify, and redistribute this software.
- If you distribute modified or unmodified versions, they must remain under the GPL.
- There is no warranty; use at your own risk.
"""

CHANGELOG = """# Changelog

## {{version}}
- Initial public release generated with Plugin Builder Enterprise.
"""
