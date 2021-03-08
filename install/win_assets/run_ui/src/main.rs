#![windows_subsystem = "windows"]

use std::process::Command;

fn main() {
    let mut run = Command::new("C:\\Program Files\\RaspiMote\\py\\pythonw.exe");
    run.arg("-c");
    run.arg("from webbrowser import open;open('https://localhost:9876')");

    match run.output() {
        Ok(o) => {
            unsafe {
                println!("{}", String::from_utf8_unchecked(o.stdout));
            }
        },
        Err(e) => {
            println!("Something went wrong. {}", e);
        }
    }
}