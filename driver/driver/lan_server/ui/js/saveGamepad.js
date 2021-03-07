function saveGamepadKey() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'gamepad_button': document.getElementById('physicalGamepadKey').value, 'action_type': 'press_key', 'key': document.getElementById('gamepadKey').value};
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




function saveGamepadText() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'gamepad_button': document.getElementById('physicalGamepadKey').value, 'action_type': 'type_text', 'text': document.getElementById('gamepadText').value};
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




function saveGamepadCommand() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'gamepad_button': document.getElementById('physicalGamepadKey').value, 'action_type': 'run_command', 'command': document.getElementById('gamepadCommand').value};
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



function saveGamepadCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'gamepad_button': document.getElementById('physicalGamepadKey').value, 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionGamepadName').value};
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