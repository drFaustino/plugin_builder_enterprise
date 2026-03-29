def classFactory(iface):
    from .plugin_builder import PluginBuilderEnterprise
    return PluginBuilderEnterprise(iface)
