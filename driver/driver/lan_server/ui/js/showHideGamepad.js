var xbox_one_coordinates = {
    "abs_z": [0.094866071, 0.251116071, 0, 0.101604278],
    "abs_rz": [0.747767857, 0.915178571, 0, 0.101604278],
    "btn_tl": [0.050223214, 0.301339286, 0.101604278, 0.222816399],
    "btn_tr": [0.680803571, 0.959821429, 0.101604278, 0.222816399],
    "btn_mode": [0.446428571, 0.558035714, 0.213903743, 0.392156863],
    "btn_select": [0.373883929, 0.446428571, 0.445632799, 0.55258467],
    "btn_start": [0.552455357, 0.625, 0.445632799, 0.55258467],
    "btn_thumbl": [0.133928571, 0.189732143, 0.516934046, 0.588235294],
    "abs_x|abs_y": [0.083705357, 0.2734375, 0.383244207, 0.659536542],
    "abs_hat0y>-1.0": [0.306919643, 0.401785714, 0.561497326, 0.704099822],
    "abs_hat0y>1.0": [0.306919643, 0.401785714, 0.77540107, 0.855614973],
    "abs_hat0x>-1.0": [0.256696429, 0.323660714, 0.704099822, 0.77540107],
    "abs_hat0x>1.0": [0.390625, 0.457589286, 0.704099822, 0.77540107],
    "btn_thumbr": [0.630580357, 0.686383929, 0.784313725, 0.846702317],
    "abs_rx|abs_ry": [0.558035714, 0.753348214, 0.64171123, 0.909090909],
    "btn_y": [0.78125, 0.870535714, 0.294117647, 0.427807487],
    "btn_b": [0.870535714, 0.954241071, 0.427807487, 0.55258467],
    "btn_a": [0.78125, 0.870535714, 0.55258467, 0.677361854],
    "btn_x": [0.686383929, 0.78125, 0.427807487, 0.55258467]
}; // Data format: [min_x, max_x, min_y, max_y]

var last_btn = "";
var mouseAbove = null;
var selectedButton = null;

function showGamepadPlus(element) {
    document.getElementById('gamepadPressKey').style.display = element.value == "key" ? 'block' : 'none';
    document.getElementById('gamepadTypeText').style.display = element.value == "text" ? 'block' : 'none';
    document.getElementById('gamepadCommandFunction').style.display = element.value == "command" ? 'block' : 'none';
    document.getElementById('gamepadCustomFunction').style.display = element.value == "custom" ? 'block' : 'none';
}

function gamepadKeyValidation(element) {
    document.getElementById('gamepadKeyValidate').style.display = element.value != "none" ? 'block' : 'none';
}

function gamepadTextValidation(element) {
    document.getElementById('gamepadTextValidate').style.display = element.value != "" ? 'block' : 'none';
}

function gamepadCommandValidation(element) {
    document.getElementById('gamepadCommandValidate').style.display = element.value != "" ? 'block' : 'none';
}

function gamepadCustomValidation(element) {
    document.getElementById('gamepadCustomValidate').style.display = element.value != "" ? 'block' : 'none';
}

function showTypeGamepadKey(element) {
    selectedButton = mouseAbove;
    element.innerHTML = "<!--" + selectedButton + "-->";
    document.getElementById('typeGamepadKey').style.display = 'block';
}

function highlight(element) {
    var width = element.clientWidth;
    var height = element.clientHeight;
    bounds = element.getBoundingClientRect();
    var left = bounds.left;
    var top = bounds.top;
    var x = event.pageX - left;
    var y = event.pageY - top;
    var rel_x = x / width;
    var rel_y = y / height;
    var ctx = element.getContext('2d');
    var k = 0;
    for (var btn in xbox_one_coordinates) {
        btn_coordinates = xbox_one_coordinates[btn];
        if (rel_x >= btn_coordinates[0] && rel_x < btn_coordinates[1] && rel_y >= btn_coordinates[2] && rel_y < btn_coordinates[3]) {
            if (last_btn != btn) {
                mouseAbove = btn;
                ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
                ctx.beginPath();
                ctx.fillStyle = 'rgba(144, 12, 63, 0.5)';
                ctx.arc(((btn_coordinates[0] + btn_coordinates[1]) / 2) * element.width, ((btn_coordinates[2] + btn_coordinates[3]) / 2) * element.height, (((btn_coordinates[3] - btn_coordinates[2]) / 2) + 0.04) * element.height, 0, 2 * Math.PI);
                ctx.fill();
            }
            k = 1;
        }
        if (k == 1) {
            break;
        }
    }
    if (k == 0) {
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        ctx.beginPath();
    }
}

function itMayBeCleared(element) {
    mouseAbove = null;
    if (selectedButton == null) {
        var ctx = element.getContext('2d');
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        ctx.beginPath();
    }
    else {
        var ctx = element.getContext('2d');
        btn_coordinates = xbox_one_coordinates[selectedButton];
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        ctx.beginPath();
        ctx.fillStyle = 'rgba(144, 12, 63, 0.5)';
        ctx.arc(((btn_coordinates[0] + btn_coordinates[1]) / 2) * element.width, ((btn_coordinates[2] + btn_coordinates[3]) / 2) * element.height, (((btn_coordinates[3] - btn_coordinates[2]) / 2) + 0.04) * element.height, 0, 2 * Math.PI);
        ctx.fill();
    }
}