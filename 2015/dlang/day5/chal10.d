import std.stdio;
import std.file;
import std.string;
import std.algorithm.searching;

// any pair of two letter that appears at least twice without overlapping
bool twoPairs(string word){
	for (int i=0; i<word.length-3; i++){
		string pair = word[i..i+2];
		string remaining = word[i+2..word.length];
		if (canFind(remaining, pair)){
			return true;
		}
	}
	return false;
}

bool repeatedWithSkip(string word){
	for (int i=0; i<word.length-2; i++){
		if (word[i] == word[i+2]){
			return true;
		}
	}
	return false;
}


bool isNice(string word){
	return twoPairs(word) && repeatedWithSkip(word);
}

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	File file = File(filepath, "r");

	int count = 0;

	while (!file.eof()){
		string line = strip(file.readln());
		if (line.length == 0){
			break;
		}
		if (isNice(line)){
			writefln("%s is Nice", line);
			count += 1;
		}else{
			writefln("%s is Naughty", line);
		}
   }
   writefln("%s Nice Words Found", count);
   return 0;
}
