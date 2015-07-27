#    "ChimeraExtension.py" derives a class from 'chimera.extension.EMO'
#    to define how functionality defined in "__init__.py" may be invoked
#    by the Chimera extension manager.
#
#    .. "ChimeraExtension.py" ToolbarButtonExtension/ChimeraExtension.py
#    .. "__init__.py" ToolbarButtonExtension/__init__.py

import chimera.extension

#    Class 'GorgonEMO' is the derived class.
class GorgonEMO(chimera.extension.EMO):
    # Return the actual name of the extension.
    def name(self):
        return 'Gorgon'

    # Return the short description that typically appears as
    # balloon help or in the Tools preference category.
    def description(self):
        return 'Gorgon'

    # Return the categories in which this extension should appear.
    # It is either a list or a dictionary.  If it is a dictionary
    # then the keys are the category names and the values are
    # category-specific descriptions (and the description() method
    # above is ignored).
    def categories(self):
        return ['Utilities']

    # Return the name of a file containing an icon that may be used
    # on the tool bar to provide a shortcut for launching the extension.
    def icon(self):
        return self.path('design/gorgon.ico')

    # Invoke the extension.  Note that when this method is called,
    # the content of "__init__.py" is not available.  To simplify
    # calling functions, the 'EMO' provides a 'module' method that
    # locates modules in the extension package by name; if no name
    # is supplied, the "__init__.py" module is returned.
    def activate(self):
    # Call the 'mainchain' function in the "__init__.py" module.
        self.module().mainGorgon()

# Register an instance of 'GorgonEMO' with the Chimera
# extension manager.
chimera.extension.manager.registerExtension(GorgonEMO(__file__))
