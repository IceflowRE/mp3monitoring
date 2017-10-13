function Component() {
    
}

Component.prototype.createOperations = function() {
    component.createOperations();
    
    component.addOperation("Execute", "pip", "install", "--upgrade", "urllib3", "UNDOEXECUTE", "pip", "uninstall", "-y", "urllib3");
}
