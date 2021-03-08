use std::process::Command;

fn main() {
    let mut run = Command::new("/usr/bin/python3");
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
