import clingo

def solve_clingo_program(program):
    # Define the program as a string
    try:
        # Create a Clingo control object
        control = clingo.Control()

        # Add the program to the control object
        control.add("base", [], program)

        # Ground the program
        control.ground([("base", [])])

        # Retrieve the solutions
        solutions = []
        with control.solve(yield_=True) as handle:
            for model in handle:
                solution = []
                for symbol in model.symbols(shown=True):
                    solution.append(str(symbol))
                solutions.append(solution)

        return solutions

    except Exception as e:
        return f"Error: {e}"
