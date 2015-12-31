import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.algorithm;

int countNeighbors(char[][] grid, int x, int y){
	int count = 0;
	for (int i=x-1; i<x+2; i++){
		for (int j=y-1; j<y+2; j++){
			//writefln("%d %d", i, j);
			if(i<0 || j<0 || i==grid.length || j==grid.length || (i==x && j==y)){
				//writeln("breaking");
				continue;
			}
			if (grid[i][j] == '#'){
				count += 1;
			}
		}
	}
	return count;
}

int countLights(char[][] grid){
	int count = 0;
	for (int i=0; i<grid.length; i++){
		for (int j=0; j<grid.length; j++){
			if (grid[i][j] == '#'){
				count += 1;
			}
		}
	}
	return count;
}

char[][] setCorners(char[][] grid){
	grid[0][0] = '#';
	grid[0][grid.length-1] = '#';
	grid[grid.length-1][0] = '#';
	grid[grid.length-1][grid.length-1] = '#';
	return grid;
}

char[][] step(char[][] grid){
	char[][] new_grid;
	for (int i=0; i<grid.length; i++){
		char[] new_row;
		for(int j=0; j<grid.length; j++){
			int count = countNeighbors(grid, i, j);
			if (grid[i][j] == '#'){
				if (count == 2 || count == 3){
					new_row ~= '#';
				}else{
					new_row ~= '.';
				}
			}else{
				if (count == 3){
					new_row ~= '#';
				}else{
					new_row ~= '.';
				}
			}
		}
		new_grid ~= new_row;
	}
	return new_grid;
}

void printGrid(char[][] grid){
	foreach (row; grid){
		writeln(row);
	}
	writeln("");
}

int main(string[] args){
	if (args.length != 3){
		writefln("Needs an input file, and # of steps");
		return 1;
	}

	string filepath = args[1];
	int steps = to!int(args[2]);

	char[][] grid;

	foreach (line; File(filepath, "r").byLine){
		line = line.strip();
		char[] row;
		foreach (c; line){
			row ~= c;
		}
		grid ~= row;
	}
	//printGrid(grid);

	int x = 0;
	int y = 3;

	//writeln(grid[x][y], countNeighbors(grid, x, y));
	grid = setCorners(grid);
	for (int i=0; i<steps; i++){
		//writefln("After Step %d:", i+1);
		grid = step(grid);
		//printGrid(grid);
		grid = setCorners(grid);
	}
	writefln("lights on: %d", countLights(grid));


   return 0;
}
