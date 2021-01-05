function saveButtonKey() {
    if (navigator['platform'].toLowerCase().includes('linux') == true) {
        var protocol = 'https';
    }
    else if (navigator['platform'].toLowerCase().includes('win') == true) {
        var protocol = 'http';
    }
    else {
        window.alert('Platform not supoorted.')
    }
    var protocol = 'http';
    const url = protocol + "://localhost:12345/"; // Must be replaced by the correct port when ready (still in localhost)! For testing purposes only.
    var data = {'port': document.getElementById('element').value, 'action_type': 'press_key', 'key': document.getElementById('key').value};
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
	    dataType: "json",
        success: function(result) {
            window.alert(result)
        },
        error: function(error) {
            window.alert('Something went wrong.')
        }
    })
}

function saveButtonText() {
    // Request
}

function saveButtonCustom() {
    // Request
}