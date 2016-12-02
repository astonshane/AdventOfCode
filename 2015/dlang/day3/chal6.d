import std.stdio;
import std.file;
import std.string;
import std.typecons;
import std.container;


alias Coord = Tuple!(float, "x", float, "y");
alias RedBlackTree!Coord CoordSet;

int main(string[] args)
{
	if (args.length != 2){
		writefln("Needs an input file!");
		return 1;
	}
	string filepath = args[1];
	File file = File(filepath, "r");

	while (!file.eof()){
		string line = strip(file.readln());
		if (line.length == 0){
			break;
		}

		Coord santa;
		santa.x = santa.y = 0;
		Coord robo;
		robo.x = robo.y = 0;
		CoordSet coords = new CoordSet;
		coords.insert(santa);

		bool turn = true;

		for (int i=0; i<line.length; i++){
			if (turn){
				if (line[i] == '>'){
					santa.x += 1;
				}else if (line[i] == '<'){
					santa.x -= 1;
				}else if (line[i] == '^'){
					santa.y += 1;
				}else if (line[i] == 'v'){
					santa.y -= 1;
				}
				coords.insert(santa);
				turn = false;
			}else{
				if (line[i] == '>'){
					robo.x += 1;
				}else if (line[i] == '<'){
					robo.x -= 1;
				}else if (line[i] == '^'){
					robo.y += 1;
				}else if (line[i] == 'v'){
					robo.y -= 1;
				}
				coords.insert(robo);
				turn = true;
			}

		}
		writefln("%s: %d", line, coords.length);
   }
   return 0;
}
