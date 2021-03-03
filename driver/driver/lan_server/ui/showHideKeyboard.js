function showKeyboardPlus(element) {
    document.getElementById('keyboardPressKey').style.display = element.value == "key" ? 'block' : 'none';
    document.getElementById('keyboardTypeText').style.display = element.value == "text" ? 'block' : 'none';
    document.getElementById('keyboardCommandFunction').style.display = element.value == "command" ? 'block' : 'none';
    document.getElementById('keyboardCustomFunction').style.display = element.value == "custom" ? 'block' : 'none';
}

function keyboardKeyValidation(element) {
    document.getElementById('keyboardKeyValidate').style.display = element.value != "none" ? 'block' : 'none';
}

function keyboardTextValidation(element) {
    document.getElementById('keyboardTextValidate').style.display = element.value != "" ? 'block' : 'none';
}

function keyboardCommandValidation(element) {
    document.getElementById('keyboardCommandValidate').style.display = element.value != "" ? 'block' : 'none';
}

function keyboardCustomValidation(element) {
    document.getElementById('keyboardCustomValidate').style.display = element.value != "" ? 'block' : 'none';
}