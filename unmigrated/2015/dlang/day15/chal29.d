import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.algorithm;

int teaspoons = 100;
Ingredient[] ingredients;

class Ingredient{

	this(string n, int cap, int dur, int flv, int tex, int cal){
		name = n;
		capacity = cap;
		durability = dur;
		flavor = flv;
		texture = tex;
		calories = cal;
	}

	void print(){
		writefln("{%s}", name);
	}

	string name;
	int capacity;
	int durability;
	int flavor;
	int texture;
	int calories;
}

int[] copy(int[] arg){
	int[] cpy;
	foreach(item; arg){
		cpy ~= item;
	}
	return cpy;
}

int recipeScore(int[] values){
	int capacity = 0;
	int durability = 0;
	int flavor = 0;
	int texture = 0;
	for (int i=0; i<values.length; i++){
		capacity += values[i]*ingredients[i].capacity;
		durability += values[i]*ingredients[i].durability;
		flavor += values[i]*ingredients[i].flavor;
		texture += values[i]*ingredients[i].texture;

	}
	capacity = max(0, capacity);
	durability = max(0, durability);
	flavor = max(0, flavor);
	texture = max(0, texture);
	return capacity * durability * flavor * texture;
}

int assignRemaining(int total, int index, int[] values){
	if (index == values.length-1){
		values[index] = teaspoons-total;
		total += teaspoons - total;
	}
	if (total == teaspoons){
		int score = recipeScore(values);
		return recipeScore(values);
	}
	int max = -1;
	for (int i=teaspoons-total; i>-1; i--){
		auto cpy = copy(values);
		cpy[index] = i;
		int tmp = assignRemaining(total+i, index+1, cpy);
		if (tmp > max){
			max = tmp;
		}
	}
	return max;
}


int main(string[] args){
	if (args.length != 2){
		writefln("Needs an input file");
		return 1;
	}

	string filepath = args[1];


	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		auto re = regex(`(.+): capacity (\d+|-\d+), durability (\d+|-\d+), flavor (\d+|-\d+), texture (\d+|-\d+), calories (\d+|-\d+)`);
		if (auto captures = matchFirst(line, re)){
			Ingredient ing = new Ingredient(to!string(captures[1]), to!int(captures[2]), to!int(captures[3]), to!int(captures[4]), to!int(captures[5]), to!int(captures[6]));
			ingredients ~= ing;
		}
	}
	int[] values;
	for (int i=0; i<ingredients.length; i++){
		values ~= 0;
	}
	int val = assignRemaining(0, 0, values);
	writeln(val);

   return 0;
}
