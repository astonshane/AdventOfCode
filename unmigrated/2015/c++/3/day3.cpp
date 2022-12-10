#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <set>
#include <string.h>
#include <regex>

using namespace std;

class Coord {
public:
  Coord(): x(0), y(0) {}

  void add(char* c){
    if (strcmp(c, '<') == 0){
      x -= 1;
    }else if (strcmp(c, '^') == 0){
      y += 1;
    }else if (strcmp(c, '>') == 0){
      x += 1;
    }else if (strcmp(c, 'v') == 0){
      y -= 1;
    }
  }

  bool operator<(const Coord& c){
    if (x < c.x){
      return true;
    }
    return false;
  }

  bool operator==(const Coord& c){
    return (x == c.x) && (y == c.y);
  }

  int x, y;
};

void chal5(char * filename) {
  ifstream infile(filename);
  long total = 0;

  set<Coord> visited;

  if (infile.is_open()){
    for (string line; getline(infile, line); ){
      for (int i=0; i<line.size(); i++){

      }
    }
  }

  cout << "part 2: " << total << endl;
}


int main(int argc, char* argv[]){
  char * filename = argv[1];
  chal5(filename);
}
