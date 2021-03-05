function changeElement(element) {
    document.getElementById('typeButton').style.display = element.value.startsWith("gpio") ? 'block' : 'none';
    document.getElementById('typeADC').style.display = element.value.startsWith("adc") ? 'block': 'none';
    document.getElementById('typeKeyboard').style.display = element.value == "usb_keyboard" ? 'block': 'none';
}