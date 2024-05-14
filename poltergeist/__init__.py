bl_info = {
    'name'    : 'Poltergeist',
    'description': "I'm warning you, no good can come from using this add-on..."
    'category': 'Generic',
    'version' : (1,0,0),
    'blender' : (4,0,0),
    'author'  : "Björn van der Scheer"
}

#- List all separate module files below
modulesNames = [
    
]

#- Code below will automatically handle the rest based on modulesNames :)
modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

import sys
import importlib

for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)

def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()

if __name__ == "__main__":
    register()
