function Controller() { }

Controller.prototype.IntroductionPageCallback = function() {
    // disable updater radio buttons
    if (installer.isUninstaller()) {
        var widget = gui.currentPageWidget();
        widget.findChild("UninstallerRadioButton").checked = true;
        widget.findChild("UpdaterRadioButton").updatesEnabled = false;
        widget.findChild("PackageManagerRadioButton").updatesEnabled = false;
    }
}
