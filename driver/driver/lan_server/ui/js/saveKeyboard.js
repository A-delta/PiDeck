function saveKeyboardKey() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";

    var key = document.getElementById('keyboardKey').value;

    var data = {
      'type': 'usb_hid',
      'name': document.getElementById('element').value,
      'function': {
        key: {
          'action_type': 'press_key',
          'to_press': document.getElementById('physicalKeyboardKey').value,
        },

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




function saveKeyboardText() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'usb_hid', 'name': document.getElementById('element').value, 'device_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'type_text', 'text': document.getElementById('keyboardText').value};

    var key = document.getElementById('keyboardKey').value;
    var data = {
      'type': 'usb_hid',
      'name': document.getElementById('element').value,
      'function': {
        key: {
          'action_type': 'type_text',
          'to_type': document.getElementById('keyboardText').value
        },
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




function saveKeyboardCommand() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'usb_hid', 'name': document.getElementById('element').value, 'device_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'run_command', 'command': document.getElementById('keyboardCommand').value};
    var key = document.getElementById('keyboardKey').value;

    var data = {
      'type': 'usb_hid',
      'name': document.getElementById('element').value,
      'function': {
        key: {
          'action_type': 'run_command',
          'to_run': document.getElementById('keyboardCommand').value,
        },
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



function saveKeyboardCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'usb_hid', 'name': document.getElementById('element').value, 'device_key': document.getElementById('physicalKeyboardKey').value, 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionKeyboardName').value};

    var key = document.getElementById('keyboardKey').value;

    var data = {
      'type': 'usb_hid',
      'name': document.getElementById('element').value,
      'function': {
        key: {
          'action_type': 'run_custom_function',
          'to_run': document.getElementById('functionKeyboardName').value,
        },
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


function saveGenericUSBFunction() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'usb_hid', 'name': document.getElementById('element').value, 'function_name': document.getElementById('genericUSBFunctionName').value};

    var key = document.getElementById('keyboardKey').value;

    var data = {
      'type': 'usb_hid',
      'name': document.getElementById('element').value,
      'function': {
        key: {
          'action_type': 'run_custom_function',
          'to_run': document.getElementById('genericUSBFunctionName').value,
        },
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
