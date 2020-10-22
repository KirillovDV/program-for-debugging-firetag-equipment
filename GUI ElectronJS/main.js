const path = require('path');
const url = require('url');
const { app, BrowserWindow } = require('electron');

let win;

function createWindow() {
    win = new BrowserWindow({
        width: 1000, //стандартная ширина окна
        height: 800, //стандартная высота окна
        icon: __dirname + "/static/img/icon.png", // добавленик иконки 
        minWidth: 1000, // минимальная ширина окна
        minHeight: 800, // минимальная высота окна
        maxWidth: 1920, // максимальная ширина окна
        maxHeight: 1080, // максимальная высота окна
        resizable: true, // будет ли окно изменять размеры
    });

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'templates/index.html'), // файл первого html шаблона,
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