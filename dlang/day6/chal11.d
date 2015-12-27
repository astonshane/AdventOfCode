import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.typecons;
import std.array;

void printLights(int[][] lights){
	writeln("");
	foreach(line; lights){
		writeln(line);
	}
	writeln("");
}

int countLights(int[][] lights){
	int count = 0;
	for(int i=0; i<lights.length; i++){
		for(int j=0; j<lights.length; j++){
			count += lights[i][j];
		}
	}
	return count;
}

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	File file = File(filepath, "r");

	int size = 1000;
	int[][] lights;

	for (int i=0; i<size; i++){
		int[] row;
		for (int j=0; j<size; j++){
			row ~= 0;
		}
		lights ~= row;
	}

	while (!file.eof()){
		string line = strip(file.readln());
		if (line.length == 0){
			break;
		}
		auto re = regex(`(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)`);
		if (auto captures = matchFirst(line, re)){
			string cmd = captures[1];
			auto start = tuple(to!int(captures[2]), to!int(captures[3]));
			auto end = tuple(to!int(captures[4]), to!int(captures[5]));
			if (cmd == "turn on"){
				for(int i=start[0]; i<end[0]+1; i++){
					for(int j=start[1]; j<end[1]+1; j++){
						lights[i][j] = 1;
					}
				}
			}else if (cmd == "turn off") {
				for(int i=start[0]; i<end[0]+1; i++){
					for(int j=start[1]; j<end[1]+1; j++){
						lights[i][j] = 0;
					}
				}
			}else {
				for(int i=start[0]; i<end[0]+1; i++){
					for(int j=start[1]; j<end[1]+1; j++){
						lights[i][j] = !lights[i][j];
					}
				}
			}

	    }
		//printLights(lights);
		//writefln("Light Count: %d", countLights(lights));
   }
   writefln("Light Count: %d", countLights(lights));
   return 0;
}
