const path = require('path');
const url = require('url');
const { app, BrowserWindow } = require('electron');

let win;

// Function create Window
function createWindow() {
    win = new BrowserWindow({
        width: 1000,
        height: 800,
        icon: __dirname + "/static/icon.png",
        minWidth: 1000, // минимальная ширина окна
        minHeight: 800, // минимальная высота окна
        maxWidth: 1920, // максимальная ширина окна
        maxHeight: 1080, // максимальная высота окна
        resizable: true, // будет ли окно изменять размеры
    });

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }));

    // win.webContents.openDevTools(); // open Dev Tools

    win.on('closed', () => {
        win - null;
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    app.quit();
});