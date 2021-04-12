function saveGamepadKey() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'xbox_one_gamepad', 'button': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''), 'action_type': 'press_key', 'key': document.getElementById('gamepadKey').value};
    var data = {
        'type': 'xbox_one_gamepad',
        'name': "IDK WHAT TO PUT HERE",
        'function': {
            'when': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''),
            'action_type': 'press_key',
            'data': document.getElementById('gamepadKey').value
          },
        };


    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            Swal.fire('Success!', result, 'success')
        },
        error: function(error) {
            if (error['status'] == 200) {
                Swal.fire('Success!', error['responseText'], 'success');
            }
            else {
                Swal.fire('Oops!', 'Something went wrong.', 'error');
            }
        }
    })
}




function saveGamepadText() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'xbox_one_gamepad', 'button': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''), 'action_type': 'type_text', 'text': document.getElementById('gamepadText').value};
    var data = {
        'type': 'xbox_one_gamepad',
        'name': "IDK WHAT TO PUT HERE",
        'function': {
            'when': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''),
            'action_type': 'type_text',
            'data': document.getElementById('gamepadText').value
          },
        };
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            Swal.fire('Success!', result, 'success')
        },
        error: function(error) {
            if (error['status'] == 200) {
                Swal.fire('Success!', error['responseText'], 'success');
            }
            else {
                Swal.fire('Oops!', 'Something went wrong.', 'error');
            }
        }
    })
}




function saveGamepadCommand() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'xbox_one_gamepad', 'button': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''), 'action_type': 'run_command', 'command': document.getElementById('gamepadCommand').value};
    var data = {
        'type': 'xbox_one_gamepad',
        'name': "IDK WHAT TO PUT HERE",
        'function': {
            'when': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''),
            'action_type': 'run_command',
            'data': document.getElementById('gamepadCommand').value
          },
        };
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            Swal.fire('Success!', result, 'success')
        },
        error: function(error) {
            if (error['status'] == 200) {
                Swal.fire('Success!', error['responseText'], 'success');
            }
            else {
                Swal.fire('Oops!', 'Something went wrong.', 'error');
            }
        }
    })
}



function saveGamepadCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'xbox_one_gamepad', 'button': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''), 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionGamepadName').value};
    var data = {
        'type': 'xbox_one_gamepad',
        'name': "IDK WHAT TO PUT HERE",
        'function': {
            'when': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''),
            'action_type': 'run_custom_function',
            'data': document.getElementById('functionGamepadName').value
          },
        };
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            Swal.fire('Success!', result, 'success')
        },
        error: function(error) {
            if (error['status'] == 200) {
                Swal.fire('Success!', error['responseText'], 'success');
            }
            else {
                Swal.fire('Oops!', 'Something went wrong.', 'error');
            }
        }
    })
}




function saveGamepadJoyVolume() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'xbox_one_gamepad', 'button': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''), 'action_type': 'change_volume'};
    var data = {
        'type': 'xbox_one_gamepad',
        'name': "IDK WHAT TO PUT HERE",
        'function': {
            'when': document.getElementById('xbox_one_controller_canvas').innerHTML.replaceAll('<!--', '').replaceAll('-->', ''),
            'action_type': 'change_volume',
            'data': 'None'
          },
        };
    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(result) {
            Swal.fire('Success!', result, 'success')
        },
        error: function(error) {
            if (error['status'] == 200) {
                Swal.fire('Success!', error['responseText'], 'success');
            }
            else {
                Swal.fire('Oops!', 'Something went wrong.', 'error');
            }
        }
    })
}
