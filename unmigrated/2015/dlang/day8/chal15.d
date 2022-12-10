import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	int total = 0;
	int escaped = 0;
	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		//.DS_Storewritefln("\n%s", line);
		int initial_length = 0;
		int final_length = 0;
		initial_length = to!int(line.length);

		line = line[1..line.length-1]; // take out the initial quotes
		auto re = regex(`\\x..|\\.`);
		line = replaceAll(line, re, "l");

		final_length = to!int(line.length);
		total += initial_length;
		escaped += final_length;
	}
	writefln("%d %d", total, escaped);
	writefln("Total difference = %d", total - escaped);

   return 0;
}
