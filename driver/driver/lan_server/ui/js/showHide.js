function changeElement(element) {

    document.getElementById('typeButton').style.display = element.value.startsWith("gpio") ? 'block' : 'none';

    document.getElementById('typeADC').style.display = element.value.startsWith("adc") ? 'block': 'none';

    document.getElementById('typeGamepad').style.display = element.value == "xbox_controller" ? 'block': 'none';

    if (element.value.startsWith("keyboard") || element.value.startsWith("mouse") || element.value.startsWith("generic_usb")) {
        if (element.value.startsWith("mouse")) {
            var items = ["BUTTON_LEFT", "BUTTON_RIGHT", "BUTTON_PREVIOUS", "BUTTON_NEXT", "SCROLL_UP", "SCROLL_DOWN", "MOVE_X", "MOVE_Y"]
        }
        else {
            var items = ["KEY_ESC", "KEY_1", "KEY_2", "KEY_3", "KEY_4", "KEY_5", "KEY_6", "KEY_7", "KEY_8", "KEY_9", "KEY_0", "KEY_MINUS", "KEY_EQUAL", "KEY_BACKSPACE", "KEY_TAB", "KEY_Q", "KEY_W", "KEY_E", "KEY_R", "KEY_T", "KEY_Y", "KEY_U", "KEY_I", "KEY_O", "KEY_P", "KEY_LEFTBRACE", "KEY_RIGHTBRACE", "KEY_ENTER", "KEY_LEFTCTRL", "KEY_A", "KEY_S", "KEY_D", "KEY_F", "KEY_G", "KEY_H", "KEY_J", "KEY_K", "KEY_L", "KEY_SEMICOLON", "KEY_APOSTROPHE", "KEY_GRAVE", "KEY_LEFTSHIFT", "KEY_BACKSLASH", "KEY_Z", "KEY_X", "KEY_C", "KEY_V", "KEY_B", "KEY_N", "KEY_M", "KEY_COMMA", "KEY_DOT", "KEY_SLASH", "KEY_RIGHTSHIFT", "KEY_KPASTERISK", "KEY_LEFTALT", "KEY_SPACE", "KEY_CAPSLOCK", "KEY_F1", "KEY_F2", "KEY_F3", "KEY_F4", "KEY_F5", "KEY_F6", "KEY_F7", "KEY_F8", "KEY_F9", "KEY_F10", "KEY_NUMLOCK", "KEY_SCROLLLOCK", "KEY_KP7", "KEY_KP8", "KEY_KP9", "KEY_KPMINUS", "KEY_KP4", "KEY_KP5", "KEY_KP6", "KEY_KPPLUS", "KEY_KP1", "KEY_KP2", "KEY_KP3", "KEY_KP0", "KEY_KPDOT", "KEY_102ND", "KEY_F11", "KEY_F12", "KEY_RO", "KEY_HENKAN", "KEY_KATAKANAHIRAGANA", "KEY_MUHENKAN", "KEY_KPJPCOMMA", "KEY_KPENTER", "KEY_RIGHTCTRL", "KEY_KPSLASH", "KEY_SYSRQ", "KEY_RIGHTALT", "KEY_HOME", "KEY_UP", "KEY_PAGEUP", "KEY_LEFT", "KEY_RIGHT", "KEY_END", "KEY_DOWN", "KEY_PAGEDOWN", "KEY_INSERT", "KEY_DELETE", "KEY_MUTE", "KEY_VOLUMEDOWN", "KEY_VOLUMEUP", "KEY_POWER", "KEY_KPEQUAL", "KEY_PAUSE", "KEY_KPCOMMA", "KEY_HANGUEL", "KEY_HANJA", "KEY_YEN", "KEY_LEFTMETA", "KEY_RIGHTMETA", "KEY_COMPOSE", "KEY_STOP", "KEY_AGAIN", "KEY_PROPS", "KEY_UNDO", "KEY_FRONT", "KEY_COPY", "KEY_OPEN", "KEY_PASTE", "KEY_FIND", "KEY_CUT", "KEY_HELP", "KEY_F13", "KEY_F14", "KEY_F15", "KEY_F16", "KEY_F17", "KEY_F18", "KEY_F19", "KEY_F20", "KEY_F21", "KEY_F22", "KEY_F23", "KEY_F24"];
        }
        var items_id = items.map(i => i.toLowerCase());
        items.unshift("&nbsp;");
        items_id.unshift("none");
        var str = "";
        k = 0;
        for (var item of items) {
            opt_id = items_id[k];
            str += '<option value="' + opt_id + '">' + item + "</option>";
            k += 1;
        }
        document.getElementById("physicalKeyboardKey").innerHTML = str;

        document.getElementById('typeKeyboard').style.display = 'block';
    }
    else {
        document.getElementById('typeKeyboard').style.display = 'none';
    }
 
}
