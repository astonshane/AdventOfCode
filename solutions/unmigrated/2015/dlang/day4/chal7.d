import std.stdio;
import std.string;
import std.digest.md;
import std.conv;
import std.array;

int main(string[] args)
{
   if (args.length != 2){
		writefln("Needs a search length");
		return 1;
	}

   int num_zereos = to!int(args[1]);
   string zeroes = replicate("0", num_zereos);
   string secret = "ckczppom";

   int i = 0;
   while(true){
      i += 1;
      ubyte[16] hash = md5Of(secret ~ to!string(i));
      string hashStr = toHexString(hash);
      string begining = hashStr[0..num_zereos];
      if (begining == zeroes){
         break;
      }
   }
   writeln(i);
   return 0;
}
