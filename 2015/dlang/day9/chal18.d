import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;

int[string][string] distances;
string[] cities;

string[] copy(string[] arg){
	string[] cpy;
	foreach(item; arg){
		cpy ~= item;
	}
	return cpy;
}

int tsp(int dist, string current, string[] remaining){
	if (remaining.length == 0){
		return dist;
	}
	int max = -1;
	for (int i=0; i<remaining.length; i++){
		auto new_remaining = copy(remaining);
		new_remaining = new_remaining[0..i] ~ new_remaining[i+1..new_remaining.length];
		int ret = tsp(dist + distances[current][remaining[i]], remaining[i], new_remaining);
		if (max == -1 || ret > max){
			max = ret;
		}
	}
	return max;
}

int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}

	foreach (line; File(args[1], "r").byLine){
		line = line.strip();
		auto re = regex(`([A-Za-z]+) to ([A-Za-z]+) = (\d+)`);
		if (auto captures = matchFirst(line, re)){
			string city1 = to!string(captures[1]);
			string city2 = to!string(captures[2]);
			int dist  = to!int(captures[3]);
			//writefln("%s %s %d", city1, city2, dist);
			if (!(city1 in distances)){
				int[string] tmp;
				distances[city1] = tmp;
			}
			distances[city1][city2] = dist;
			if(!(city2 in distances)){
				int[string] tmp;
				distances[city2] = tmp;
			}
			distances[city2][city1] = dist;
		}
	}
	cities = distances.keys;
	int max_dist = -1;
	for (int i=0; i<cities.length; i++){
		string city = cities[i];
		string [] remaining = copy(cities);
		remaining = remaining[0..i] ~ remaining[i+1..cities.length];
		//writeln(city, remaining);
		int ret = tsp(0, city, remaining);
		if (max_dist == -1 || ret > max_dist){
			max_dist = ret;
		}
	}
	writefln("maximum distance: %d", max_dist);

   return 0;
}
