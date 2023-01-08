import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.algorithm;
import std.typecons;
import std.container;


alias Replacement = Tuple!(string, "from", string, "to");
alias RedBlackTree!string Set;

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file");
		return 1;
	}

	string filepath = args[1];

	string start;
	Replacement[] replacements;


	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		auto re = regex(`(.+) => (.+)`);
		if (auto captures = matchFirst(line, re)){
			Replacement tmp;
			tmp.from = to!string(captures[1]);
			tmp.to = to!string(captures[2]);
			replacements ~= tmp;
		}else{
			start = to!string(line);
		}
	}

	Set molecules = new Set;

	foreach (replacement; replacements){
		auto re = regex(replacement.from);
		foreach(c; matchAll(start, re)){
			//writefln("%s %s %s", c.pre, c.hit, c.post);
			molecules.insert(c.pre ~ replacement.to ~ c.post);
		}

	}
	writeln(molecules);
	writeln(molecules.length);
   return 0;
}
