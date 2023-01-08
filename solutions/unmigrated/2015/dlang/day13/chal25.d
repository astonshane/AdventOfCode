import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;

int[string][string] happiness;

string[] copy(string[] arg){
	string[] cpy;
	foreach(item; arg){
		cpy ~= item;
	}
	return cpy;
}

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

int tableValue(string[] table){
	writeln(table);
	int value = 0;
	for (int i=0; i<table.length; i++){
		string person = table[i];
		string left = table[fmod(i-1, to!int(table.length))];
		string right = table[fmod(i+1, to!int(table.length))];
		value += happiness[person][left] + happiness[person][right];
	}
	return value;
}

int optimalHappy(string[] current, string[] remaining){
	if (remaining.length == 0){
		return tableValue(current);
	}

	int max_happy = -1;
	for(int i=0; i<remaining.length; i++){
		string[] new_current = copy(current) ~ remaining[i];
		string[] new_remaining = copy(remaining);
		new_remaining = new_remaining[0..i] ~ new_remaining[i+1..new_remaining.length];
		int tmp = optimalHappy(new_current, new_remaining);
		if (tmp == -1 || tmp > max_happy){
			max_happy = tmp;
		}
	}
	return max_happy;
}

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

		auto re = regex(`(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*).`);
		if (auto captures = matchFirst(line, re)){
			//writeln(captures);
			string person1 = to!string(captures[1]);
			string type = to!string(captures[2]);
			int value = to!int(captures[3]);
			string person2 = to!string(captures[4]);

			if (!(person1 in happiness)){
				int[string] tmp;
				happiness[person1] = tmp;
			}
			if (type == "gain"){
				happiness[person1][person2] = value;
			}else{
				happiness[person1][person2] = -value;
			}

		}

	}
	//writeln(happiness);
	string[] people = happiness.keys;
	//writeln(people);

	string[] empty;
	int max_happy = optimalHappy(empty, people);
	writefln("Optimal Happiness: %d", max_happy);

   return 0;
}
