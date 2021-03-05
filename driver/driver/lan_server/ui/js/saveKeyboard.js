function saveKeyboardKey() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'keyboard_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'press_key', 'key': document.getElementById('keyboardKey').value};
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




function saveKeyboardText() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'keyboard_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'type_text', 'text': document.getElementById('keyboardText').value};
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




function saveKeyboardCommand() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'keyboard_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'run_command', 'command': document.getElementById('keyboardCommand').value};
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



function saveKeyboardCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'keyboard_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionKeyboardName').value};
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