function range(start, stop, step) {
    if (typeof stop == 'undefined') {
        stop = start;
        start = 0;
    }

    if (typeof step == 'undefined') {
        step = 1;
    }

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
        return [];
    }

    var result = [];
    for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
        result.push(i);
    }

    return result;
};

function init() {

    var platform = navigator['platform'];
    if (platform.toLowerCase().includes('linux') || platform.toLowerCase().includes('win')) {}
    else {
        window.alert("Non-critical error: Your platform doesn't seem to be supported.");
    }
    const url = "https://localhost:9876/get_inventory";
    $.ajax({
        url: url,
        type: "POST",
        success: function(result) {
            var inventory = JSON.parse(result)
            var items = ["&nbsp;"];
            if (inventory != false) {

                for (var button of inventory["GPIO_buttons"]) {
                    items.push("GPIO " + button);
                }
                if ("ADC" in inventory) {
                    var ADC = inventory["ADC"];
                }
                else {
                    var ADC = 0;
                }
                for (var k of range(ADC)) {
                    items.push("ADC " + (k + 1))
                }
                items.push("USB keyboard");
                // var items = ["&nbsp;", "GPIO 13", "ADC 1", "GPIO 12"]; // For test purposes
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


                var items = ["&nbsp;", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "🔊 Volume up", "🔈 Volume down", "🔇 Mute", "⏯️ Play/pause", "⏮️ Previous song", "⏭️ Next song", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "Print screen", "↖ Home", "End", "Delete", "↲ Enter", "⟵ Backspace", "→| Tabulation", "⇞ Page up", "⇟ Page down", "⇧ Shift", "Ctrl", "Alt", "⊞ ⌘ Super"];
                var items_id = ["none", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "volup", "voldown", "mute", "pp", "next", "previous", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24", "psc", "pos1", "end", "del", "enter", "backspace", "tab", "pup", "pdown", "shift", "ctrl", "alt", "super"];
                var str = "";
                k = 0;
                for (var item of items) {
                    opt_id = items_id[k];
                    str += '<option value="' + opt_id + '">' + item + "</option>";
                    k += 1;
                }
                document.getElementById("buttonKey").innerHTML = str;
                document.getElementById("keyboardKey").innerHTML = str;

                var items = ["KEY_ESC", "KEY_1", "KEY_2", "KEY_3", "KEY_4", "KEY_5", "KEY_6", "KEY_7", "KEY_8", "KEY_9", "KEY_0", "KEY_MINUS", "KEY_EQUAL", "KEY_BACKSPACE", "KEY_TAB", "KEY_Q", "KEY_W", "KEY_E", "KEY_R", "KEY_T", "KEY_Y", "KEY_U", "KEY_I", "KEY_O", "KEY_P", "KEY_LEFTBRACE", "KEY_RIGHTBRACE", "KEY_ENTER", "KEY_LEFTCTRL", "KEY_A", "KEY_S", "KEY_D", "KEY_F", "KEY_G", "KEY_H", "KEY_J", "KEY_K", "KEY_L", "KEY_SEMICOLON", "KEY_APOSTROPHE", "KEY_GRAVE", "KEY_LEFTSHIFT", "KEY_BACKSLASH", "KEY_Z", "KEY_X", "KEY_C", "KEY_V", "KEY_B", "KEY_N", "KEY_M", "KEY_COMMA", "KEY_DOT", "KEY_SLASH", "KEY_RIGHTSHIFT", "KEY_KPASTERISK", "KEY_LEFTALT", "KEY_SPACE", "KEY_CAPSLOCK", "KEY_F1", "KEY_F2", "KEY_F3", "KEY_F4", "KEY_F5", "KEY_F6", "KEY_F7", "KEY_F8", "KEY_F9", "KEY_F10", "KEY_NUMLOCK", "KEY_SCROLLLOCK", "KEY_KP7", "KEY_KP8", "KEY_KP9", "KEY_KPMINUS", "KEY_KP4", "KEY_KP5", "KEY_KP6", "KEY_KPPLUS", "KEY_KP1", "KEY_KP2", "KEY_KP3", "KEY_KP0", "KEY_KPDOT", "KEY_102ND", "KEY_F11", "KEY_F12", "KEY_RO", "KEY_HENKAN", "KEY_KATAKANAHIRAGANA", "KEY_MUHENKAN", "KEY_KPJPCOMMA", "KEY_KPENTER", "KEY_RIGHTCTRL", "KEY_KPSLASH", "KEY_SYSRQ", "KEY_RIGHTALT", "KEY_HOME", "KEY_UP", "KEY_PAGEUP", "KEY_LEFT", "KEY_RIGHT", "KEY_END", "KEY_DOWN", "KEY_PAGEDOWN", "KEY_INSERT", "KEY_DELETE", "KEY_MUTE", "KEY_VOLUMEDOWN", "KEY_VOLUMEUP", "KEY_POWER", "KEY_KPEQUAL", "KEY_PAUSE", "KEY_KPCOMMA", "KEY_HANGUEL", "KEY_HANJA", "KEY_YEN", "KEY_LEFTMETA", "KEY_RIGHTMETA", "KEY_COMPOSE", "KEY_STOP", "KEY_AGAIN", "KEY_PROPS", "KEY_UNDO", "KEY_FRONT", "KEY_COPY", "KEY_OPEN", "KEY_PASTE", "KEY_FIND", "KEY_CUT", "KEY_HELP", "KEY_F13", "KEY_F14", "KEY_F15", "KEY_F16", "KEY_F17", "KEY_F18", "KEY_F19", "KEY_F20", "KEY_F21", "KEY_F22", "KEY_F23", "KEY_F24"];
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

                $(".gif-loading").fadeOut("slow");
            }
            else {
                window.location.href="about:blank";
            }
        },
        error: function(error) {
            if (error['status'] == 500 && error['responseText'] == "INVENTORY_NOT_FOUND") {
                window.alert("Critical error: Couldn't retreive the inventory.\nTry to restart the driver.")
                return;
            }
            else {
                window.alert("Critical error: Something went wrong. Unknown error.")
                return;
            }
        }
    })
}

function openEditor() {
    const url = "https://localhost:9876/open_editor";
    $.ajax({
        url: url,
        type: "POST",
    })
}

window.onload = init;