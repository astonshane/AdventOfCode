import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.array;

int main(string[] args){
	if (args.length != 3){
		writefln("Needs a starting input and number of rounds!");
		return 1;
	}

	string input = args[1];
	int rounds = to!int(args[2]);

	auto re = regex(`(\d)\1*`);

	for (int rd = 0; rd<rounds; rd++){
		//writeln(input);
		string new_word;
		auto matches = matchAll(input, re);
		foreach(c; matchAll(input, re)){
			new_word ~= to!string(c.hit.length) ~ to!string(c.hit[0]);
		}
		input = new_word;
	}
	writeln(input.length);

   return 0;
}
