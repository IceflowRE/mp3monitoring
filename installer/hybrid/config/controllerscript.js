function Controller() {
    
}

Controller.prototype.IntroductionPageCallback = function() {
    // disable updater radio buttons
    if (installer.isUninstaller()) {
        var widget = gui.currentPageWidget();
        widget.findChild("UninstallerRadioButton").checked = true;
        widget.findChild("UpdaterRadioButton").updatesEnabled = false;
        widget.findChild("PackageManagerRadioButton").updatesEnabled = false;
    }
}

Controller.prototype.ReadyForInstallationPageCallback = function() {
    if (installer.isUninstaller()) {
        var widget = gui.currentPageWidget(); 
        pythonText = "<font color='red'>\n This will uninstall the following python packages if the associated component is installed: tqdm, mutagen - pyqt5 (gui) - urllib3 (updater)!</font>";
        widget.findChild("MessageLabel").setText(widget.findChild("MessageLabel").text + pythonText);
    }
}
