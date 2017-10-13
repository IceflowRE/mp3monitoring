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

var tmpDir = "@RootDir@/tmp/mp3monitoring/";
var checkPythonArr = new Array("", "if command -v python; then", "    exit 0", "else", "    exit 1", "fi");
var checkPipArr = new Array("", "if command -v pip; then", "    exit 0", "else", "    exit 1", "fi");

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
    var file = tmpDir + "check_python.sh";
    installer.execute(cmdLocation, new Array("/C", "echo #!/bin/sh > " + file));
    for (i = 1; i < checkPythonArr.length; i++) {
        installer.execute(cmdLocation, new Array("/C", "echo " + checkPythonArr[i] + " >> " + file));
    }
    var exists = installer.execute(cmdLocation, new Array("/C", "bash " + file))[1];
    if (exists != 0) {
        cancelInstaller("No Python installation detected.");
        return;
    } else {
        console.log("Check: Python installation detected.");
    }
    
    // check pip
    file = tmpDir + "check_pip.sh"
    installer.execute(cmdLocation, new Array("/C", "echo #!/bin/sh > " + file));
    for (i = 1; i < checkPipArr.length; i++) {
        installer.execute(cmdLocation, new Array("/C", "echo " + checkPipArr[i] + " >> " + file));
    }
    var exists = installer.execute(cmdLocation, new Array("/C", "bash " + file))[1];
    if (exists != 0) {
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
