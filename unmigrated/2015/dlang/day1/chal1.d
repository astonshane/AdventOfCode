import std.stdio;
import std.file;
import std.string;

int main(string[] args)
{
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	File file = File(filepath, "r");
	while (!file.eof()){
		int count = 0;
		string line = strip(file.readln());
	  	//write(line);
	  	for (int i=0; i<line.length; i++){
			if (line[i] == '('){
				count += 1;
			}else{
				count -= 1;
			}
	  	}
		writefln("count: %d", count);
   }
	return 0;
}
