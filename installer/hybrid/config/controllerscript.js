function Controller() {
    
}

Controller.prototype.FinishedPageCallback = function() {
    if (installer.value("prerequisiteError", false)) {
        installer.interrupt(); // fixes asking for admin rights
    }
}

Controller.prototype.IntroductionPageCallback = function() {
    checkPrerequisite();
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
        pythonText = "<br><br><font color='red'>\n This will uninstall the following python packages if the associated component is installed: tqdm, mutagen - pyqt5 (gui) - urllib3 (updater)!</font>";
        widget.findChild("MessageLabel").setText(widget.findChild("MessageLabel").text + pythonText);
    }
}

checkPrerequisite = function() {
    if (installer.value("os") != "win") {
        cancelInstaller("Installation on " + systemInfo.prettyProductName + " is not supported");
        return;
    }
    var windir = installer.environmentVariable("WINDIR");
    if (windir == "") {
        cancelInstaller("Windows installation path not detected.");
        return;
    }
    var cmdLocation = windir + "\\system32\\cmd.exe";
    
    // check python
    var exists = installer.execute(cmdLocation, "/C where python >nul 2>&1 && exit 0 || exit 1");
    if (exists.length == 0) {
        cancelInstaller("No Python installation detected.");
        return;
    } else if (exists[1] != 0) {
        cancelInstaller("No Python installation detected.");
        return;
    } else {
        console.log("Check: Python installation detected.");
    }
    
    // check pip
    var exists = installer.execute(cmdLocation, "/C where pip >nul 2>&1 && exit 0 || exit 1");
    if (exists.length == 0) {
        cancelInstaller("No Pip installation detected.");
        return;
    } else if (exists[1] != 0) {
        cancelInstaller("No Pip installation detected.");
        return;
    } else {
        console.log("Check: Pip installation detected.");
    }
}

cancelInstaller = function(message) {
    var abortText = "<font size='4'><font color='red'>" + message + "</font></font>";
    installer.setValue("FinishedText", abortText);
    installer.setDefaultPageVisible(QInstaller.TargetDirectory, false);
    installer.setDefaultPageVisible(QInstaller.ReadyForInstallation, false);
    installer.setDefaultPageVisible(QInstaller.ComponentSelection, false);
    installer.setDefaultPageVisible(QInstaller.StartMenuSelection, false);
    installer.setDefaultPageVisible(QInstaller.PerformInstallation, false);
    installer.setDefaultPageVisible(QInstaller.LicenseCheck, false);
    gui.clickButton(buttons.NextButton);
    
    installer.setValue("prerequisiteError", true);
}
