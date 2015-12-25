extern crate regex;
use regex::Regex;
use std::io::{BufReader,BufRead};
use std::fs::File;
use std::path::Path;

fn parse_num(num: &str) -> i32 {
    let d1: i32 = match num.parse() {
        Ok(n) => {
            n
        }, Err(_) => {
            println!("error: second argument not an integer");
            return 0;
        },
    };
    return d1;
}

fn chal3() {
    let path = Path::new("src/input.txt");
    let file = BufReader::new(File::open(&path).unwrap());
    let mut total = 0;
    for line in file.lines() {
      let unwraped = line.unwrap();
      let re = Regex::new(r"(\d+)x(\d+)x(\d+)").unwrap();

      for cap in re.captures_iter(&unwraped) {
        let d1 = parse_num(cap.at(1).unwrap_or(""));
        let d2 = parse_num(cap.at(2).unwrap_or(""));
        let d3 = parse_num(cap.at(3).unwrap_or(""));
        let mut v = vec![d1, d2, d3];
        v.sort();
        let area = 2*v[0]*v[1] + 2*v[0]*v[2] + 2*v[1]*v[2] + v[0]*v[1];
        total += area;
      }
    }
    println!("Total Area: {}", total);
}

fn chal4() {
    let path = Path::new("src/input.txt");
    let file = BufReader::new(File::open(&path).unwrap());
    let mut total = 0;
    for line in file.lines() {
      let unwraped = line.unwrap();
      let re = Regex::new(r"(\d+)x(\d+)x(\d+)").unwrap();

      for cap in re.captures_iter(&unwraped) {
        let d1 = parse_num(cap.at(1).unwrap_or(""));
        let d2 = parse_num(cap.at(2).unwrap_or(""));
        let d3 = parse_num(cap.at(3).unwrap_or(""));
        let mut v = vec![d1, d2, d3];
        v.sort();
        let ribbon = 2*(v[0]+v[1]) + v[0]*v[1]*v[2];
        total += ribbon;
        println!("{} {}", unwraped, ribbon);
      }
    }
    println!("Total Ribbon: {}", total);
}

fn main() {
    chal3();
    chal4();
}
