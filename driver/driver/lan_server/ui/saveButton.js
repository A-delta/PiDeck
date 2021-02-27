function saveButtonKey() {
    if (navigator['platform'].toLowerCase().includes('linux') == true) {
        var protocol = 'https';
    }
    else if (navigator['platform'].toLowerCase().includes('win') == true) {
        var protocol = 'http';
    }
    else {
        window.alert('Platform not supported.');
        return "PLATFORM_NOT_SUPPORTED";
    }
    const url = protocol + "://localhost:9876/config";
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
            if (error['status'] == 200) {
                window.alert(error['responseText'])
            }
            else {
                window.alert('Something went wrong.')
            }
        }
    })
}




function saveButtonText() {
    if (navigator['platform'].toLowerCase().includes('linux') == true) {
        var protocol = 'https';
    }
    else if (navigator['platform'].toLowerCase().includes('win') == true) {
        var protocol = 'http';
    }
    else {
        window.alert('Platform not supported.');
        return "PLATFORM_NOT_SUPPORTED";
    }
    const url = protocol + "://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'action_type': 'type_text', 'text': document.getElementById('text').value};
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            window.alert(result)
        },
        error: function(error) {
            if (error['status'] == 200) {
                window.alert(error['responseText'])
            }
            else {
                window.alert('Something went wrong.')
            }
        }
    })
}




function saveButtonCommand() {
    if (navigator['platform'].toLowerCase().includes('linux') == true) {
        var protocol = 'https';
    }
    else if (navigator['platform'].toLowerCase().includes('win') == true) {
        var protocol = 'http';
    }
    else {
        window.alert('Platform not supported.');
        return "PLATFORM_NOT_SUPPORTED";
    }
    const url = protocol + "://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'action_type': 'run_command', 'command': document.getElementById('command').value};
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            window.alert(result)
        },
        error: function(error) {
            if (error['status'] == 200) {
                window.alert(error['responseText'])
            }
            else {
                window.alert('Something went wrong.')
            }
        }
    })
}



function saveButtonCustom() {
    if (navigator['platform'].toLowerCase().includes('linux') == true) {
        var protocol = 'https';
    }
    else if (navigator['platform'].toLowerCase().includes('win') == true) {
        var protocol = 'http';
    }
    else {
        window.alert('Platform not supported.');
        return "PLATFORM_NOT_SUPPORTED";
    }
    const url = protocol + "://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionName').value};
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            window.alert(result)
        },
        error: function(error) {
            if (error['status'] == 200) {
                window.alert(error['responseText'])
            }
            else {
                window.alert('Something went wrong.')
            }
        }
    })
}