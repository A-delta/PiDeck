function init() {
    var items = ["&nbsp;", "GPIO 13", "ADC 1", "GPIO 12"];
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
    document.getElementById("key").innerHTML = str;
}

window.onload = init;