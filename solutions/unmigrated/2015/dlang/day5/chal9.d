import std.stdio;
import std.file;
import std.string;
import std.algorithm.searching;

// at least three vowels
bool threeVowels(string word){
	char[] vowels = ['a', 'e', 'i', 'o', 'u'];
	int count = 0;
	foreach (letter; word){
		if (canFind(vowels, letter)){
			count += 1;
			if (count >= 3){
				return true;
			}
		}
	}
	return false;
}

//at least one letter that appears twice in a row
bool doubleLetter(string word){
	for (int i=0; i<word.length-1; i++){
		if (word[i] == word[i+1]){
			return true;
		}
	}
	return false;
}

//none of ab, cd, pq, or xy
bool noPairs(string word){
	string[] pairs = ["ab", "cd", "pq", "xy"];
	foreach (pair; pairs){
		if (canFind(word, pair)){
			return false;
		}
	}
	return true;
}

bool isNice(string word){
	return threeVowels(word) && doubleLetter(word) && noPairs(word);
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
