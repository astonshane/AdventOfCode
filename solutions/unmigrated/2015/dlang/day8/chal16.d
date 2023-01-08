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
	int unescaped = 0;
	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		int initial_length = 0;
		int final_length = 0;
		initial_length = to!int(line.length);

		auto re = regex(`\\`);
		line = replaceAll(line, re, "\\\\");

		auto re2 = regex(`"`);
		line = replaceAll(line, re2, "\\\"");

		line = "\"" ~ line ~ "\"";

		final_length = to!int(line.length);
		total += initial_length;
		unescaped += final_length;
	}
	writefln("%d %d", total, unescaped);
	writefln("Total difference = %d", unescaped - total);

   return 0;
}
