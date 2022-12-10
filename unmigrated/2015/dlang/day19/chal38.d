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

	string end = "e";
	string start;
	Replacement[] replacements;


	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		auto re = regex(`(.+) => (.+)`);
		if (auto captures = matchFirst(line, re)){
			Replacement tmp;
			tmp.to = to!string(captures[1]);
			tmp.from = to!string(captures[2]);
			replacements ~= tmp;
		}else{
			start = to!string(line);
		}
	}

	Set molecules = new Set;
	Set all_molecules = new Set;

	molecules.insert(start);
	sort!("a.from.length > b.from.length")(replacements); // sort replacements by size

	int step = 0;
	string mol = start;
	while (mol != end){
		foreach(replacement; replacements){
			auto re = regex(replacement.from);
			string new_mol = replaceFirst(mol, re, replacement.to);
			if (mol != new_mol){
				mol = new_mol;
				step += 1;
			}
		}
	}
	writeln(step);

	/*foreach (replacement; replacements){
		auto re = regex(replacement.from);
		foreach(c; matchAll(start, re)){
			//writefln("%s %s %s", c.pre, c.hit, c.post);
			molecules.insert(c.pre ~ replacement.to ~ c.post);
		}

	}
	//writeln(molecules);
	writeln(molecules.length);*/
   return 0;
}
