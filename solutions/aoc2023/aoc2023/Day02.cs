namespace AdventOfCode;

public class Day02 : BaseDay
{
    private readonly string _input;

    public Day02()
    {
        _input = File.ReadAllText(InputFilePath);
    }

    public override ValueTask<string> Solve_1() => new($"Solution to {ClassPrefix} {CalculateIndex()}, {Part1()}");

    public override ValueTask<string> Solve_2() => new($"Solution to {ClassPrefix} {CalculateIndex()}, {Part2()}");

    private int Part1()
    {
        int total = 0;
        var lines = _input.Split(Environment.NewLine);
        for (int i=0; i < lines.Length; i++)
        {
            var line = lines[i];
            // Console.WriteLine(line);
            var pulls = line.Split(':')[1].Split(';');
            var cubes = new Dictionary<string, int>() {
                {"red", 0},
                {"green", 0},
                {"blue", 0}
            };
            foreach (var pull in pulls)
            {
                var draws = pull.Split(',');
                foreach (var draw in draws)
                {
                    var x = draw.Trim().Split(' ');
                    // Console.WriteLine(x[0]);
                    var count = int.Parse(x[0]);
                    var color = x[1];
                    if (count > cubes[color])
                    {
                        cubes[color] = count;
                    }
                }
            }

            if (cubes["red"] <= 12 && cubes["green"] <= 13 && cubes["blue"] <= 14)
            {
                total += i+1;
            }
        }
        return total;
    }

    private int Part2()
    {
        int total = 0;
        var lines = _input.Split(Environment.NewLine);
        for (int i=0; i < lines.Length; i++)
        {
            var line = lines[i];
            // Console.WriteLine(line);
            var pulls = line.Split(':')[1].Split(';');
            var cubes = new Dictionary<string, int>() {
                {"red", 0},
                {"green", 0},
                {"blue", 0}
            };
            foreach (var pull in pulls)
            {
                var draws = pull.Split(',');
                foreach (var draw in draws)
                {
                    var x = draw.Trim().Split(' ');
                    // Console.WriteLine(x[0]);
                    var count = int.Parse(x[0]);
                    var color = x[1];
                    if (count > cubes[color])
                    {
                        cubes[color] = count;
                    }
                }
            }

            int power = cubes.Values.Aggregate(1, (a, b) => a * b);
            total += power;
        }
        return total;
    }
}