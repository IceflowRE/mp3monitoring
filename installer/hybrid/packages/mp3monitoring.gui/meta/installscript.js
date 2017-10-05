function Component() {
    
}

Component.prototype.createOperations = function() {
    component.createOperations();
    
    component.addOperation("Execute", "pip install --upgrade", "pyqt5");
    component.addOperation("CreateShortcut", "@TargetDir@/README.md", "@StartMenuDir@/MP3 Monitoring Gui.lnk",
                           "workingDirectory=@TargetDir@", "iconPath=%SystemRoot%/system32/SHELL32.dll",
                           "iconId=2", "description=Start the MP3 Monitoring Gui");
    component.addOperation("CreateShortcut", "@TargetDir@/README.md", "@TargetDir@/MP3 Monitoring Gui.lnk",
                           "workingDirectory=@TargetDir@", "iconPath=%SystemRoot%/system32/SHELL32.dll",
                           "iconId=2", "description=Start the MP3 Monitoring Gui");
}
