import 'dart:io';

void main() {
  Process.run("python3",
      ["-c", "from webbrowser import open;open('https://localhost:9876')"]);
}
