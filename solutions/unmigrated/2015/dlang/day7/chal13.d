import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.typecons;
import std.array;
import std.algorithm.comparison;
import std.exception;

// % in D doesn't properly handle negatives...
int fmod(int num, int mod){
	if (num >= 0 && num < mod){
		return num;
	}else if(num >= mod){
		return num % mod;
	}else{
		return fmod(num + mod, mod);
	}
}

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	File file = File(filepath, "r");

	string[] lines;
	int[string] values;
	int mod = 65536;

	while (!file.eof()){
		string line = strip(file.readln());
		if (line.length == 0){
			break;
		}
		lines ~= line;
   }
   while (lines.length > 0){
	   string[] new_lines;
	   foreach (line; lines){
		   auto re1 = regex(`^(\d+|[a-z]+) -> ([a-z]+)`); // 123 -> x
		   auto re2 = regex(`NOT ([a-z]+) -> ([a-z]+)`); // NOT x -> y
		   auto re3 = regex(`([a-z]+|\d+) ([A-Z]+) ([a-z]+) -> ([a-z]+)`); // x AND y -> z; x OR y -> z
		   auto re4 = regex(`([a-z]+) ([A-Z]+) (\d+) -> ([a-z]+)`); // x LSHIFT 2 -> z; x RSHIFT 3 -> z
		   if (auto captures = matchFirst(line, re1)){
			   Exception e = collectException(to!int(captures[1]));
			   if (e){
				   // assignment is another value, not a number
				   string base = captures[1];
				   string target = captures[2];
				   if (base in values){
					   values[target] = values[base];
				   }else{
					   new_lines ~= line;
				   }
			   }else{
				   // assignment is a number
				   int value = to!int(captures[1]);
				   string target = captures[2];
				   values[target] = value;
			   }


		   }else if (auto captures = matchFirst(line, re2)) {
			   string base = captures[1];
			   string target = captures[2];
			   if (base in values){
				   values[target] = fmod(~values[base], mod);
			   }else{
				   new_lines ~= line;
			   }
		   }else if (auto captures = matchFirst(line, re3)) {
			   Exception e = collectException(to!int(captures[1]));
 			   if (e){
				   // first base is a string
				   string base1 = captures[1];
				   string operator = captures[2];
				   string base2 = captures[3];
	 			   string target = captures[4];
				   if (base1 in values && base2 in values){
					   if (operator == "AND"){
						   values[target] = fmod(values[base1] & values[base2], mod);
					   }else if (operator == "OR"){
						   values[target] = fmod(values[base1] | values[base2], mod);
					   }
				   }else{
					   new_lines ~= line;
				   }
			   }else{
				   // first base is a number
				   int base1 = to!int(captures[1]);
				   string operator = captures[2];
				   string base2 = captures[3];
	 			   string target = captures[4];
				   if (base2 in values){
					   if (operator == "AND"){
						   values[target] = fmod(base1 & values[base2], mod);
					   }else if (operator == "OR"){
						   values[target] = fmod(base1 | values[base2], mod);
					   }
				   }else{
					   new_lines ~= line;
				   }
			   }

		   }else if (auto captures = matchFirst(line, re4)) {
 			   string base = captures[1];
			   string operator = captures[2];
			   int value = to!int(captures[3]);
			   string target = captures[4];
			   if (base in values){
				   if (operator == "LSHIFT"){
					   values[target] = fmod(values[base] << value, mod);
				   }else if (operator == "RSHIFT"){
					   values[target] = fmod(values[base] >> value, mod);
				   }
			   }else{
				   new_lines ~= line;
			   }
		   }else{
			   writeln("something's wrong...   ", line);
		   }
	   }
	   if (lines == new_lines){
		   writeln("didn't finish... got stuck");
		   break;
	   }
	   lines = new_lines;
   }

   writefln("a: %d", values["a"]);
   return 0;
}
