function send_hello() {

    eel.send_hello();
}

//window.location = ''

async function download() {

    console.log('sending download request to python')
    await eel.download_video()()
    //var output = document.getElementById('output');
    //output.innerHTML = await eel.download_video(link)()

    //var output = document.getElementById('output');
    //output.innerHTML = 'Program finished working (check if the file downloaded properly)';

    var output = document.getElementById('output');
    output.value += '--------------------' + '\n'
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

    var link = document.getElementById('video_link').value;
    var output = document.getElementById('option_link');

    output.innerHTML = await eel.change_link(link)();
}

// Change format
async function change_format() {

    var format = document.getElementById('format').value;
    var format_object = document.getElementById('format');
    var format_text = format_object.options[format_object.selectedIndex].text;
    var output = document.getElementById('option_format');
    console.log('Trying to change format to: ' + format);
    await eel.change_option('format', format);
    output.innerHTML = format_text;

}

// Change download directory
async function change_directory() {

    var directory = document.getElementById('directory').value;
    console.log('Trying to change directory to: ' + directory);
    var output = document.getElementById('option_directory');
    var response = await eel.change_directory(directory)();

    if (response) output.innerHTML = directory;
}

async function save_directory() {

    var directory = document.getElementById('directory').value;
    console.log('Trying to save directory: ' + directory);

    await eel.save_prefs('directory', directory);
}

var res = [1200, 700]

window.onresize = function () {

    if (window.outerWidth < res[0]) window.resizeTo(res[0], window.outerHeight);
    if (window.outerHeight < res[1]) window.resizeTo(window.outerWidth, res[1]);
}