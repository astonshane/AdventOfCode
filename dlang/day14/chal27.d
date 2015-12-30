import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;

class Reindeer{

	this(string n, int s, int ft, int rt){
		name = n;
		speed = s;
		fly_time = ft;
		rest_time = rt;
		time = fly_time;
	}

	void print(){
		writefln("{%s (%d)}", name, pos);
	}

	void increment(){
		time -= 1;
		if (flying){
			pos += speed;
		}
		if (time == 0){
			if (flying){
				time = rest_time;
				flying = false;
			}else{
				time = fly_time;
				flying = true;
			}
		}
	}

	string name;
	int speed;
	int fly_time;
	int rest_time;
	int pos = 0;
	int time;
	bool flying = true;
}

void printAllReindeer(Reindeer[] reindeer){
	writeln("\n#####");
	foreach (r; reindeer){
		r.print();
	}
	writeln("#####");
}

Reindeer findLeader(Reindeer[] reindeer){
	Reindeer max;
	int max_val = 0;
	foreach (r; reindeer){
		if (r.pos >= max_val){
			max = r;
			max_val = r.pos;
		}
	}
	return max;
}

int main(string[] args){
	if (args.length != 3){
		writefln("Needs an input file and # of seconds!");
		return 1;
	}

	string filepath = args[1];
	int seconds = to!int(args[2]);

	Reindeer[] all_reindeer;

	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		writeln(line);
		auto re = regex(`(.*) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.`);
		if (auto captures = matchFirst(line, re)){
			string name = to!string(captures[1]);
			int speed = to!int(captures[2]);
			int fly_time = to!int(captures[3]);
			int rest_time = to!int(captures[4]);
			Reindeer reindeer = new Reindeer(name, speed, fly_time, rest_time);
			all_reindeer ~= reindeer;
		}
	}

	for (int i=0; i<seconds; i++){
		foreach (reindeer; all_reindeer){
			reindeer.increment();
		}
	}
	printAllReindeer(all_reindeer);
	Reindeer winner = findLeader(all_reindeer);
	writefln("Winner is %s at distance %d", winner.name, winner.pos);

   return 0;
}
