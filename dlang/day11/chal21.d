import std.stdio;
import std.file;
import std.string;
import std.regex;
import std.conv;
import std.array;

string removeSpecial(string password, char toRemove){
	string new_password;
	bool found = false;
	for (int i=0; i<password.length; i++){
		if (!found){
			if (password[i] == toRemove){
				new_password = new_password ~ to!char(password[i]+1);
				found = true;
			}else{
				new_password = new_password ~ password[i] ;
			}
		}else{
			new_password = new_password ~ 'a';
		}
	}
	return new_password;
}

string checkSpecials(string password){
	//i, o, or l
	password = removeSpecial(password, 'i');
	password = removeSpecial(password, 'o');
	password = removeSpecial(password, 'l');
	return password;
}

string increment(string password){
	string new_password;
	bool found = false;
	for(int i=to!int(password.length)-1; i >= 0; i--){
		if (!found){
			if(password[i] != 'z'){
				new_password = to!char(password[i]+1) ~ new_password;
				found = true;
			}else{
				new_password = 'a' ~ new_password;
			}
		}else{
			new_password = password[i] ~ new_password;
		}

	}
	string tmp = checkSpecials(new_password);
	if (tmp != new_password){
		return tmp;
	}
	return new_password;
}

bool threeStraight(string password){
	for (int i=0; i<password.length-2; i++){
		if (to!char(password[i]+1) == password[i+1] && to!char(password[i]+2) == password[i+2]){
			return true;
		}
	}
	return false;
}

bool twoPair(string password){
	bool foundOne = false;
	for (int i=0; i<password.length-1; i++){
		if (password[i] == password[i+1]){
			if (foundOne){
				return true;
			}else{
				foundOne = true;
				i += 1;
			}
		}
	}
	return false;
}

int main(string[] args){
	if (args.length != 2){
		writefln("Needs a starting password!");
		return 1;
	}

	string password = args[1];

	while(true){
		//writeln(password);
		password = increment(password);
		if (threeStraight(password) && twoPair(password)){
			break;
		}
	}
	writefln("New password: %s", password);

   return 0;
}
