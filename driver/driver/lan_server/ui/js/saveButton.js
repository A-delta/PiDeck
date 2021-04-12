function saveButtonKey() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'button', 'gpio': parseInt(document.getElementById('element').value.replaceAll('gpio_', '')), 'action_type': 'press_key', 'key': document.getElementById('buttonKey').value};

    var data = {
      'type': 'button',
      'name': parseInt(document.getElementById('element').value.replaceAll('gpio_', '')),
      'function': {
          'when': 'triggered',
          'action_type': 'press_key',
          'data': document.getElementById('buttonKey').value
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




function saveButtonText() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    var data = {
      'type': 'button',
      'name': parseInt(document.getElementById('element').value.replaceAll('gpio_', '')),
      'function': {
          'when': 'triggered',
          'action_type': 'type_text',
          'data': document.getElementById('buttonText').value
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




function saveButtonCommand() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    //var data = {'type': 'button', 'gpio': parseInt(document.getElementById('element').value.replaceAll('gpio_', '')), 'action_type': 'run_command', 'command': document.getElementById('buttonCommand').value};

    var data = {
      'type': 'button',
      'name': parseInt(document.getElementById('element').value.replaceAll('gpio_', '')),
      'function': {
          'when': 'triggered',
          'action_type': 'run_command',
          'data': document.getElementById('buttonCommand').value
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



function saveButtonCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
    var data = {
      'type': 'button',
      'name': parseInt(document.getElementById('element').value.replaceAll('gpio_', '')),
      'function': {
          'when': 'triggered',
          'action_type': 'run_custom_function',
          'data': document.getElementById('functionButtonName').value
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
