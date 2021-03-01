import 'dart:io';

void main() {
  Process.run("C:\\Program Files\\RaspiMote\\py\\python.exe",
      ["-c", "from webbrowser import open;open('https://localhost:9876')"]);
}
