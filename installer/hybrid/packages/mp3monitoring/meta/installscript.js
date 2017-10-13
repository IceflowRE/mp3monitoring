var tmpDir = "@RootDir@/tmp/mp3monitoring/";
var wheelName = "MP3_Monitoring-1.0.0-py3-none-any.whl";

function Component() {
    
}

// extract data to tmp dir
Component.prototype.createOperationsForArchive = function(archive) {
    component.addOperation("Extract", archive, tmpDir);
}

Component.prototype.createOperations = function() {
    component.createOperations();
    
    component.addOperation("Copy", tmpDir + "README.md", "@TargetDir@");
    component.addOperation("Execute", "pip", "install", "--no-deps", tmpDir + wheelName, "UNDOEXECUTE", "pip", "uninstall", "-y", "mp3-monitoring");
    component.addOperation("Execute", "pip", "install", "--upgrade", "mutagen", "UNDOEXECUTE", "pip", "uninstall", "-y", "mutagen");
    component.addOperation("Execute", "pip", "install", "--upgrade", "tqdm", "UNDOEXECUTE", "pip", "uninstall", "-y", "tqdm");
}
