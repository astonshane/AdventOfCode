import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.algorithm;

int main(string[] args)
{
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	File file = File(filepath, "r");

	int total = 0;

	while (!file.eof()){
		// 2*l*w + 2*w*h + 2*h*l + area of smallest side
		int[3] size;
		string line = strip(file.readln());
		if (line.length == 0){
			break;
		}
		auto re = regex(`(\d+)x(\d+)x(\d+)`);
		if (auto captures = matchFirst(line, re)){
		   for (int i=0; i<3; i++){
			   size[i] = to!int(captures[i+1]);
		   }
	    }
		auto ssize = size.sort;
		int area = 2*ssize[0]*ssize[1] + 2*ssize[0]*ssize[2] + 2*ssize[1]*ssize[2] + ssize[0]*ssize[1];
		//writefln("%s: %d", line, area);
		total += area;
   }
   writefln("Total Area: %d", total);
   return 0;
}
