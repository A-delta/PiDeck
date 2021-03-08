#![windows_subsystem = "windows"]

use std::process::Command;

fn main() {
    let mut run = Command::new("C:\\Program Files\\RaspiMote\\init.cmd");

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