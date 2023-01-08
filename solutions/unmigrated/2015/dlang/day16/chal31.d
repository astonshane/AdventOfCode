import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.algorithm;

int main(string[] args){

	int[string] aunt;

	foreach (line; File("aunt.txt", "r").byLine){
		line = line.strip();
		auto re = regex(`(.*): (\d+)`);
		if (auto captures = matchFirst(line, re)){
			string type = to!string(captures[1]);
			int value = to!int(captures[2]);
			aunt[type] = value;
		}
	}

	int[string][int] all_aunts;

	foreach (line; File("input.txt", "r").byLine){
		line = line.strip();
		auto re = regex(`Sue (\d+):`);
		if (auto captures = matchFirst(line, re)){
			int num = to!int(captures[1]);
			int[string] tmp;
			string post = to!string(captures.post).strip();
			auto a = split(post, ",");
			foreach (attr; a){
				attr = attr.strip();
				auto re2 = regex(`(.*): (\d+)`);
				if (auto captures2 = matchFirst(attr, re2)){
					string type = to!string(captures2[1]);
					int val = to!int(captures2[2]);
					tmp[type] = val;
				}
			}
			all_aunts[num] = tmp;
		}
	}

	int[] aunt_nums = all_aunts.keys();

	foreach (key; aunt.keys()){
		int[] new_nums;
		foreach (num; aunt_nums){
			if (key in all_aunts[num]){
				if (all_aunts[num][key] == aunt[key]){
					new_nums ~= num;
				}
			}else{
				new_nums ~= num;
			}
		}
		aunt_nums = new_nums;
	}
	writeln(aunt_nums);


   return 0;
}
