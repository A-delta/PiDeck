function init() {
    var items = ["", "GPIO 13", "ADC 1"];
    var items_id = [];
    k = 0;
    for (var item of items) {
        if (k != 0) {
            items_id.push(item.toLowerCase().replace(" ", "_"))
        }
        else {
            items_id.push("none")
        }
        k += 1;
    }
    var str = "";
    k = 0;
    for (var item of items) {
        opt_id = items_id[k];
        str += '<option value="' + opt_id + '">' + item + "</option>";
        k += 1;
    }

    document.getElementById("element").innerHTML = str;
}

window.onload = init;