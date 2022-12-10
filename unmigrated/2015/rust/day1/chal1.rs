use std::io::{BufReader,BufRead};
  use std::fs::File;
  use std::path::Path;

  fn main() {
      let path = Path::new("input.txt");
      let file = BufReader::new(File::open(&path).unwrap());
      for line in file.lines() {
        let mut count = 0;
        let unwraped = line.unwrap();
        for c in unwraped.chars(){
          // print!("{} {}\n", c, i);
          if c == '(' {
            count += 1;
          }else if c == ')'{
            count -= 1;
          }
        }
        print!("count: {}\n", count);
      }
  }
