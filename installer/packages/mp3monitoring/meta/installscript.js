function Component() {

}

Component.prototype.createOperations = function() {
    // call default implementation
    component.createOperations();
    // ... add custom operations
    checkForPython();
}

function checkForPython() {
    //QMessageBox.information("information", "Information", blub, QMessageBox.Yes);
    //installer.setValue("ComponentError", true);
}
