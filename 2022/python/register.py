from functools import wraps

ALL_SOLUTIONS = {}

def register_solution(year, day, part):
    def decorate(f):
        if year not in ALL_SOLUTIONS:
            ALL_SOLUTIONS[year] = {}
        if day not in ALL_SOLUTIONS[year]:
            ALL_SOLUTIONS[year][day] = {}
        ALL_SOLUTIONS[year][day][part] = f

        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return decorate


def get_solver(year, day, part):
    return ALL_SOLUTIONS.get(year, {}).get(day, {}).get(part)
