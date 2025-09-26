<%*
const os = require('os');
const userName = os.userInfo().username;
const folder = tp.file.folder(true);
await tp.file.create_new(tp.file.find_tfile("Template - New Concept"), "New Concept - by " + userName, true, folder);
%>