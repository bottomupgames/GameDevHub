<%*
const os = require('os');
const userName = os.userInfo().username;
const folder = tp.file.folder(true);
await tp.file.create_new(tp.file.find_tfile("Template - Nouvel Arc Distinct"), "Nouvel Arc - by " + userName, true, folder);
%>