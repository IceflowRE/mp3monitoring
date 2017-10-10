function Component() {
    
}

Component.prototype.createOperations = function() {
    component.createOperations();
    
    var cmdLocation = installer.environmentVariable("WINDIR") + "\\system32\\cmd.exe";
    component.addOperation("Execute", "pip", "install", "--upgrade", "pyqt5");
    component.addOperation("CreateShortcut", cmdLocation, "@StartMenuDir@/MP3 Monitoring Gui.lnk", "/C start mp3monitoring-gui",
                           "workingDirectory=@TargetDir@", "iconPath=%SystemRoot%/system32/SHELL32.dll", "iconId=2",
                           "description=Start the MP3 Monitoring Gui");
    // Create shortcut does not work for the working directory itself, so we have to copy it.
    component.addOperation("Copy", "@StartMenuDir@/MP3 Monitoring Gui.lnk", "@TargetDir@/MP3 Monitoring Gui.lnk");
}
