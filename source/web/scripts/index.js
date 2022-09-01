function send_hello() {

    eel.send_hello();
}

async function load_prefs() {

    settings = await eel.load_prefs()();
    console.log(settings);
    if (!settings) return;

    for (setting in settings) {

        switch (setting) {

            case 'directory':

                var output = document.getElementById('directory');
                output.value = settings[setting];
        }
    }
}


// Show Youtube-DL Console output in app
eel.expose(logs_from_python);
function logs_from_python(message) {

    var output = document.getElementById('output');
    output.value += message + '\n';
    output.scrollTop = output.scrollHeight;
}

// Change link
async function change_link() {

    var links = document.getElementById('video_link').value.split(/\r?\n/);
    var newLinks = [];

    links.forEach(element => {
        element = element.replace(/\s+/g, '');

        if (element != '') newLinks.push(element);
    });

    if (newLinks.length == 0) {

        console.log('[change_link] ERROR: link is empty');
        return 0;
    }

    console.log('[change_link] detected links: ' + newLinks);
    console.log('[change_link] trying to change link');

    await eel.change_link(newLinks)();
    console.log('[change_link] success');
    return 1;
    /*
    var link = document.getElementById('video_link').value;
    if (link == '' || link == ' ') {
        console.log('[change_link] ERROR: link is empty');
        return 0;
    }
    await eel.change_link(link)();
    console.log('[change_link] success');
    return 1;
    */
}

// Change format
async function change_format() {

    var format = document.getElementById('format').value;
    console.log('[change_format] Trying to change format to: ' + format);
    await eel.change_option('format', format);

}

// Change download directory
async function change_directory() {

    var directory = document.getElementById('directory').value;
    if (directory == '') {

        console.log('[change_directory] No directory selected. skipping...');
        return 1;
    }
    console.log('[change_directory] Trying to change directory to: ' + directory);
    var response = await eel.change_directory(directory)();

    if (response) {
        console.log('[change_directory] success: ' + directory);
        return 1;
    }
    return 0;
}

async function save_directory() {

    var directory = document.getElementById('directory').value;
    console.log('[save_directory] Trying to save directory: ' + directory);

    await eel.save_prefs('directory', directory);
}

async function download() {

    console.log('[download] trying to change options');
    logs_from_python('trying to change options...');
    if (await change_directory() == 0) {

        logs_from_python('directory: ERROR (directory does not exist)');
        logs_from_python('------------------------------------------------------------\n');
        return;
    }
    logs_from_python('directory: OK');
    if (await change_link() == 0) {
        logs_from_python('link: ERROR (link is not valid)');
        logs_from_python('------------------------------------------------------------\n');
        return;
    }
    logs_from_python('link: OK');
    change_format()

    console.log('[download] sending download request to python');
    await eel.download_video()()
    logs_from_python('\nFINISHED\n------------------------------------------------------------\n');
}

var res = [900, 600]

window.onresize = function () {

    if (window.outerWidth < res[0]) window.resizeTo(res[0], window.outerHeight);
    if (window.outerHeight < res[1]) window.resizeTo(window.outerWidth, res[1]);
}