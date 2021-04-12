function saveADCVolume() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
<<<<<<< HEAD


    var data = {
      'type': 'adc',
      'name': parseInt(document.getElementById('element').value.replaceAll('adc_', '')),
      'function': {
          'when': 'triggered',
          'action_type': 'type_text',
          'data': document.getElementById('keyboardText').value
        },
      },
    };

=======
    var data = {'type': 'adc', 'channel': parseInt(document.getElementById('element').value.split("adc_").join("")), 'action_type': 'change_volume'};
>>>>>>> dddedfab2d62f51889dba04503948c522446aee2
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




function saveADCCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        Swal.fire('Non-critical error', 'Your platform doesn’t seem to be supported.', 'info');;
    }
    const url = "https://localhost:9876/config";
<<<<<<< HEAD


    var data = {
      'type': 'adc',
      'name': parseInt(document.getElementById('element').value.replaceAll('adc_', '')),
      'function': {
          'when': 'triggered',
          'action_type': run_custom_function,
          'data': document.getElementById('functionADCName').value
        },
      },
    };

=======
    var data = {'type': 'adc', 'channel': parseInt(document.getElementById('element').value.split("adc_").join("")), 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionADCName').value};
>>>>>>> dddedfab2d62f51889dba04503948c522446aee2
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
