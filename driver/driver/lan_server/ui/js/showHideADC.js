function showADCPlus(element) {
    document.getElementById('adcVolumeValidate').style.display = element.value == "volume" ? 'block' : 'none';
    document.getElementById('adcCustomFunction').style.display = element.value == "custom" ? 'block' : 'none';
}

function adcCustomValidation(element) {
    document.getElementById('adcCustomValidate').style.display = element.value != "" ? 'block' : 'none';
}