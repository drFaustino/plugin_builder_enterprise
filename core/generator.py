import os
import shutil
import datetime

from .utils import slugify, safe_mkdir
from ..toolbelt.file_writer import FileWriter
from . import templates


class PluginGenerator:
    def __init__(self, base_folder, log_callback=None):
        self.base_folder = base_folder
        self.log = []
        self.log_callback = log_callback

    def _log(self, msg):
        self.log.append(msg)
        if self.log_callback:
            self.log_callback(msg)

    def render(self, template, ctx):
        out = template
        for k, v in ctx.items():
            out = out.replace("{{" + k + "}}", str(v))
        return out

    def generate(self, meta, structure, options, paths):
        plugin_dir_name = slugify(meta["name"])
        target = os.path.join(paths["save_dir"], plugin_dir_name)
        safe_mkdir(target)

        writer = FileWriter(target, self.log)

        ctx = {
            "plugin_name": meta["name"],
            "about": meta["about"],
            "description": meta["description"],
            "version": meta["version"],
            "author": meta["author"],
            "email": meta["email"],
            "homepage": meta["homepage"],
            "repository": meta["repository"],
            "tracker": meta["tracker"],
            "tags": meta["tags"],
            "plugin_dependencies": meta["plugin_dependencies"],
            "qgis_min": meta["qgis_min"],
            "qgis_max": meta["qgis_max"],
            "has_processing": "True" if structure["processing"] else "False",
            "experimental": "True" if options["experimental"] else "False",
            "icon_name": options["icon_name"],
            "year": datetime.datetime.now().year,
            "plugin_dir_name": plugin_dir_name,
        }

        # Base UI file
        if options.get("create_ui"):
            ui_dir = os.path.join(target, "ui")
            safe_mkdir(ui_dir)
            ui_name = f"{plugin_dir_name}.ui"
            writer.write(os.path.join("ui", ui_name), self.render(templates.BASE_UI, ctx))
            self._log(f"Created base UI: ui/{ui_name}")

        # Metadata and Readme
        writer.write("metadata.txt", self.render(templates.METADATA, ctx))
        writer.write("README.md", self.render(templates.README, ctx))

        # LICENSE (plain text)
        if options["license_type"] == "MIT License":
            writer.write("LICENSE", self.render(templates.LICENSE_MIT, ctx))
            writer.write("LICENSE.md", self.render(templates.LICENSE_MIT, ctx))

        elif options["license_type"] == "GPL v3 License":
            writer.write("LICENSE", self.render(templates.LICENSE_GPL, ctx))
            writer.write("LICENSE.md", self.render(templates.LICENSE_GPL, ctx))

        if options["changelog"]:
            writer.write("CHANGELOG.md", self.render(templates.CHANGELOG, ctx))

        writer.write("__init__.py", self.render(templates.BASE_INIT, ctx))
       
        # Main plugin file
        main_file = f"{plugin_dir_name}.py"
        writer.write(main_file, self.render(templates.BASE_PLUGIN_MAIN, ctx))
        self._log(f"Created main plugin file: {main_file}")

        # Icon
        if options["icon_path"]:
            img_dir = os.path.join(target, "resources", "images")
            safe_mkdir(img_dir)
            shutil.copy2(options["icon_path"], os.path.join(img_dir, options["icon_name"]))
            self._log(f"Copied icon: {options['icon_name']}")

        # i18n folder
        i18n_dir = os.path.join(target, "resources", "i18n")
        safe_mkdir(i18n_dir)

        # create empty TS files
        for lang in ["en", "it", "es", "fr"]:
            ts_name = f"{plugin_dir_name}_{lang}.ts"
            writer.write(os.path.join("resources", "i18n", ts_name), "")
            self._log(f"Created translation file: resources/i18n/{ts_name}")

        self._log("Plugin generation completed.")
        return self.log
