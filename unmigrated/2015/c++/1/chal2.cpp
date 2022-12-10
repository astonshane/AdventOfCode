#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]){
  char * filename = argv[1];

  string line;
  ifstream infile(filename);

  int count=0;
  int pos=1;

  if (infile.is_open()){
    while (getline(infile, line)){
      for (int i=0; i<line.size(); i++){
        if (line[i] == '('){
          count += 1;
        }else{
          count -= 1;
        }
        if (count < 0){
          cout << count << "  " << pos << endl;
          break;
        } else {
          pos += 1;
        }
      }
    }
  }
}
