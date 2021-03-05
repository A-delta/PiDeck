function saveADCVolume() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'action_type': 'change_volume'};
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




function saveADCCustom() {
    var platform = navigator['platform'].toLowerCase();
    if (platform.includes('linux') || platform.includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/config";
    var data = {'port': document.getElementById('element').value, 'action_type': 'run_custom_function', 'function_name': document.getElementById('functionADCName').value};
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