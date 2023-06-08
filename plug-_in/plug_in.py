# Plugin interface or base class
class Plugin:
    def perform_action(self):
        raise NotImplementedError()

# Plugin 1
class Plugin1(Plugin):
    def perform_action(self):
        print("Plugin 1 is performing an action!")

# Plugin 2
class Plugin2(Plugin):
    def perform_action(self):
        print("Plugin 2 is performing an action!")

# Plugin manager
class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin):
        self.plugins.append(plugin)

    def run_plugins(self):
        for plugin in self.plugins:
            plugin.perform_action()

# Creating plugin instances
plugin1 = Plugin1()
plugin2 = Plugin2()

# Creating plugin manager instance
manager = PluginManager()

# Loading plugins into the manager
manager.load_plugin(plugin1)
manager.load_plugin(plugin2)

# Running the plugins
manager.run_plugins()



# In this example, we define a Plugin interface or base class that all plugins must implement. Each plugin class inherits 
# from the base class and provides its own implementation of the perform_action() method.

# The PluginManager class is responsible for loading and running the plugins. It has a list to store the loaded plugins 
# and provides methods to load plugins into the list and run them.

# We create instances of Plugin1 and Plugin2, and then load them into the plugin manager using the load_plugin() method. 
# Finally, we call the run_plugins() method to execute the perform_action() method of each loaded plugin.

# When you run this code, it will output:

# This example demonstrates a simple plugin architecture where multiple plugins can be loaded and executed dynamically. 
# You can expand on this basic structure to create more complex plugin systems based on your specific requirements.