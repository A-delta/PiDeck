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
    // document.getElementById('typeGamepadKey').style.display = element.value != "none" ? 'block' : 'none';
    document.getElementById('typeGamepadKey').style.display = 'block';
}


function test(element) {
    var width = element.clientWidth;
    var height = element.clientHeight;
    bounds=element.getBoundingClientRect();
    var left=bounds.left;
    var top=bounds.top;
    var x = event.pageX - left;
    var y = event.pageY - top;
    console.log(x + " " + y);
    console.log(width + " " + height)
}