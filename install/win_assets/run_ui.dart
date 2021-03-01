import 'dart:io';

void main() {
  Process.run("C:\\Program Files\\RaspiMote\\py\\pythonw.exe",
      ["-c", "from webbrowser import open;open('https://localhost:9876')"]);
}
