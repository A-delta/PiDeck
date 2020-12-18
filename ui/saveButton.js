function saveButtonKey() {
    const Url='http://localhost:12345/';
    var data={'yay': 'yeahyourright'};
    console.log(data);
    $.ajax({
        url: Url,
        type: "POST",
        data: JSON.stringify(data),
	    dataType: "json",
        success: function(result) {
            window.alert(result)
        },
        error: function(error) {
            window.alert(error)
        }
    })
}

function saveButtonText() {
    // Request
}

function saveButtonCustom() {
    // Request
}