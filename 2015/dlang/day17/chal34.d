import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.algorithm;

int[] copy(int[] arg){
	int[] cpy;
	foreach(item; arg){
		cpy ~= item;
	}
	return cpy;
}

// http://rosettacode.org/wiki/Combinations#D
T[][] comb(T)(in T[] arr, in int k) pure nothrow {
    if (k == 0) return [[]];
    typeof(return) result;
    foreach (immutable i, immutable x; arr)
        foreach (suffix; arr[i + 1 .. $].comb(k - 1))
            result ~= x ~ suffix;
    return result;
}

int sumCombo(int[] combo){
	int sum = 0;
	foreach (num; combo){
		sum += num;
	}
	return sum;
}

int main(string[] args){
	if (args.length != 3){
		writefln("Needs an input file and capacity");
		return 1;
	}

	string filepath = args[1];
	int capacity = to!int(args[2]);

	int[] containers;

	foreach (line; File(filepath, "r").byLine){
		containers ~= to!int(line.strip());
	}
	writeln(containers);
	int num_found = 0;
	for (int i=0; i<containers.length+1; i++){
		auto combos = containers.comb(i);
		foreach (combo; combos){
			if(sumCombo(combo) == capacity){
				num_found += 1;
			}
		}
		if (num_found > 0){
			break;
		}
	}
	writeln(num_found);

   return 0;
}
