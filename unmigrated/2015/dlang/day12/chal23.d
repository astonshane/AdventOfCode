import std.stdio;
import std.file;
import std.string;
import std.conv;
import std.json;

int count(JSONValue j){
	if (j.type == JSON_TYPE.INTEGER){
		return to!int(j.integer);
	}else if (j.type == JSON_TYPE.ARRAY) {
		int value = 0;
		foreach (item; j.array){
			value += count(item);
		}
		return value;
	}else if (j.type == JSON_TYPE.OBJECT) {
		int value = 0;
		foreach (item; j.object){
			value += count(item);
		}
		return value;
	}
	return 0;
}

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		JSONValue j = parseJSON(line);
		writefln("Count: %d", count(j));
	}

   return 0;
}
