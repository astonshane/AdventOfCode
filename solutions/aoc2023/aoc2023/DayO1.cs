namespace AdventOfCode;

public class Day01 : BaseDay
{
    private readonly string _input;
    private readonly IDictionary<string, int> numbers;

    public Day01()
    {
        _input = File.ReadAllText(InputFilePath);
        numbers = new Dictionary<string, int>(){
            {"zero", 0},
            {"one", 1},
            {"two", 2},
            {"three", 3},
            {"four", 4},
            {"five", 5},
            {"six", 6},
            {"seven", 7},
            {"eight", 8},
            {"nine", 9}
        };
    }

    public override ValueTask<string> Solve_1() => new($"Solution to {ClassPrefix} {CalculateIndex()}, {Solver()}");

    public override ValueTask<string> Solve_2() => new($"Solution to {ClassPrefix} {CalculateIndex()}, {Solver(true)}");

    private int Solver(bool textToInt=false)
    {
        int total = 0;
        var lines = _input.Split(Environment.NewLine);
        foreach (var line in lines)
        {

            int first = -1;
            int last = -1;
            for (int i = 0; i < line.Length; i++)
            {
                int val;
                if (int.TryParse(line[i].ToString(), out val))
                {
                    if (first == -1)
                    {
                        first = val;
                    }
                    last = val;
                }
                else if (textToInt)
                {
                    string substring = line[i..line.Length];
                    foreach (var kvp in numbers)
                    {
                        if (substring.StartsWith(kvp.Key))
                        {
                            if (first == -1)
                            {
                                first = kvp.Value;
                            }
                            last = kvp.Value;
                        }
                    }
                }
            }

            var subtotal = (first * 10) + last;
            // Console.WriteLine(line);
            // Console.WriteLine(subtotal);
            total += subtotal;
        }
        return total;
    }
}