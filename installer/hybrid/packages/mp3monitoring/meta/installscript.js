var tmpDir = "@RootDir@/tmp/mp3monitoring/"
var wheelName = "MP3_Monitoring-1.0.0-py3-none-any.whl"

function Component() {
    if (installer.value("os") != "win") {
        cancelInstaller("Installation on " + systemInfo.prettyProductName + " is not supported");
        return;
    }
    checkPrerequisite();
}

// extract data to tmp dir
Component.prototype.createOperationsForArchive = function(archive) {
    component.addOperation("Extract", archive, tmpDir);
}

Component.prototype.createOperations = function() {
    component.createOperations();
    
    component.addOperation("Copy", tmpDir + "README.md", "@TargetDir@")
    component.addOperation("Execute", "pip", "install", "--no-deps", tmpDir + wheelName, "UNDOEXECUTE", "pip", "uninstall", "-y", "mp3-monitoring");
    component.addOperation("Execute", "pip", "install", "--upgrade", "mutagen");
    component.addOperation("Execute", "pip", "install", "--upgrade", "tqdm");
}

var checkPythonArr = new Array("", "if command -v python; then", "    exit 0", "else", "    exit 1", "fi")
var checkPipArr = new Array("", "if command -v pip; then", "    exit 0", "else", "    exit 1", "fi")

function checkPrerequisite() {
    var windir = installer.environmentVariable("WINDIR");
    if (windir == "") {
        cancelInstaller("Windows installation path not detected.");
    }
    var cmdLocation = windir + "\\system32\\cmd.exe";
    
    // check python
    var file = "@RootDir@/tmp/check_python.sh"
    installer.execute(cmdLocation, new Array("/C", "echo #!/bin/sh > " + file));
    for (i = 1; i < checkPythonArr.length; i++) {
        installer.execute(cmdLocation, new Array("/C", "echo " + checkPythonArr[i] + " >> " + file));
    }
    var exists = installer.execute(cmdLocation, new Array("/C", "bash " + file))[1];
    if (exists != 0) {
        cancelInstaller("No Python installation detected.");
    } else {
        console.log("Check: Python installation detected.")
    }
    
    // check pip
    file = "@RootDir@/tmp/check_pip.sh"
    installer.execute(cmdLocation, new Array("/C", "echo #!/bin/sh > " + file));
    for (i = 1; i < checkPipArr.length; i++) {
        installer.execute(cmdLocation, new Array("/C", "echo " + checkPipArr[i] + " >> " + file));
    }
    var exists = installer.execute(cmdLocation, new Array("/C", "bash " + file))[1];
    if (exists != 0) {
        cancelInstaller("No Pip installation detected.");
    } else {
        console.log("Check: Pip installation detected.")
    }
}

function cancelInstaller(message) {
    installer.setDefaultPageVisible(QInstaller.Introduction, false);
    installer.setDefaultPageVisible(QInstaller.TargetDirectory, false);
    installer.setDefaultPageVisible(QInstaller.ComponentSelection, false);
    installer.setDefaultPageVisible(QInstaller.ReadyForInstallation, false);
    installer.setDefaultPageVisible(QInstaller.StartMenuSelection, false);
    installer.setDefaultPageVisible(QInstaller.PerformInstallation, false);
    installer.setDefaultPageVisible(QInstaller.LicenseCheck, false);

    var abortText = "<font size='4'><font color='red'>" + message + "</font></font>";
    installer.setValue("FinishedText", abortText);
}
