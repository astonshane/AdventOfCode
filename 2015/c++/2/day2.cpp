#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>

using namespace std;

typedef vector<int> dimensions;

std::ostream& operator<<(std::ostream& os, const dimensions& d){
  os << "[";
  for (int i=0; i<d.size(); i++){
    os << d[i];
    if (i != d.size()-1){
      os << ", ";
    }
  }
  os << "]";
  return os;
}

int surfaceArea(dimensions dim){
  sort(dim.begin(), dim.end());
  int surface_area = 0;

  for (int i=0; i<dim.size()-1; i++){
    for (int j=i+1; j<dim.size(); j++){
      surface_area += 2*dim[i]*dim[j];
    }
  }

  return surface_area + dim[0]*dim[1];
}

int perimeter(dimensions dim){
  sort(dim.begin(), dim.end());

  int mult = 1;
  for (int i: dim){
    mult *= i;
  }

  return mult + dim[0]*2 + dim[1]*2;
}

void chal3(char * filename) {
  ifstream infile(filename);
  long total = 0;

  if (infile.is_open()){
    for (string line; getline(infile, line); ){
      regex re("(\\d+)x(\\d+)x(\\d+)");
      smatch match;
      regex_match(line, match, re);
      if (match.size() == 4){
        dimensions d;
        for (int i=1; i<4; i++){
          d.push_back(atoi(match[i].str().c_str()));
        }
        total += surfaceArea(d);
      }
    }
  }

  cout << "part 1: " << total << endl;
}

void chal4(char * filename) {
  ifstream infile(filename);
  long total = 0;

  if (infile.is_open()){
    for (string line; getline(infile, line); ){
      regex re("(\\d+)x(\\d+)x(\\d+)");
      smatch match;
      regex_match(line, match, re);
      if (match.size() == 4){
        dimensions d;
        for (int i=1; i<4; i++){
          d.push_back(atoi(match[i].str().c_str()));
        }
        total += perimeter(d);
      }
    }
  }

  cout << "part 2: " << total << endl;
}


int main(int argc, char* argv[]){
  char * filename = argv[1];
  chal3(filename);
  chal4(filename);
}
