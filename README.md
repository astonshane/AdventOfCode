# Advent of Code

My solutions for Advent Of Code + a helper program I'm working on 
to wrap all of my solutions and automate the initial bootstrapping of each day's solutions

Would eventually like to add:
* Completion stats
* Bulk running of solutions / benchmarking
* Potentially: support for other language solutions within the wrapper
* fixing usage messages so that they work as you'd expect

## Usage

```
./aoc.py -h
usage: aoc.py [-h] {run,stats} ...

Helper code to help organize and manage your Advent of Code solutions

positional arguments:
  {run,stats}  Desired action to perform
    run        Run the solution for the specified year/day/part
    stats      show stats jfjfj

optional arguments:
  -h, --help   show this help message and exit
```
```
./aoc.py run -h
usage: aoc.py run [-h] -y YEAR -d DAY [-p {1,2}] [-t] [--bootstrap]

Run the solution for the specified year/day/part

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR
  -d DAY, --day DAY
  -p {1,2}, --part {1,2}
  -t, --test            use the testing dataset instead of real dataset
  --bootstrap           sets up directories, creates bootstrapped solution file from the template, and downloads dataset (if not done previously)
```
```
./aoc.py stats -h
usage: aoc.py stats [-h] [-y YEAR]

Show stats

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR
```
### Solution Bootstrapping
The bootstrap functionality that downloads your actual AOC input dataset for you requires your session token.

One way to find your session token value:
* In your browser of choice, log into Advent of Code
* Open the developer console and go to network tab
* Open one of the input file pages (while signed in)
    * example: http://adventofcode.com/2022/day/1/input
* Inspect the headers, and take your session token from the cookie

The token needs to be provided in one of the following ways:
1. AOC_SESSION_TOKEN environment variable
2. `.aoc_session_token` file in your present working directory