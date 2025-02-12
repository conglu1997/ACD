class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cities": ["A", "B", "C", "D", "E"],
                "distances": {
                    ("A", "B"): 10,
                    ("A", "C"): 15,
                    ("A", "D"): 20,
                    ("A", "E"): 25,
                    ("B", "C"): 35,
                    ("B", "D"): 25,
                    ("B", "E"): 30,
                    ("C", "D"): 30,
                    ("C", "E"): 40,
                    ("D", "E"): 50
                }
            },
            "2": {
                "cities": ["W", "X", "Y", "Z", "V"],
                "distances": {
                    ("W", "X"): 12,
                    ("W", "Y"): 23,
                    ("W", "Z"): 34,
                    ("W", "V"): 45,
                    ("X", "Y"): 45,
                    ("X", "Z"): 56,
                    ("X", "V"): 67,
                    ("Y", "Z"): 67,
                    ("Y", "V"): 78,
                    ("Z", "V"): 89
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the Traveling Salesman Problem (TSP) for the given set of cities and distances. The goal is to find the shortest possible route that visits each city exactly once and returns to the starting city. The cities and distances are as follows:\n\nCities: {', '.join(t['cities'])}\nDistances: {', '.join([f'{pair[0]}-{pair[1]}: {distance}' for pair, distance in t['distances'].items()])}\n\nProvide your solution in the following format:\nRoute: [Your sequence of cities starting and ending at the same city, separated by commas]\nTotal Distance: [The total distance of the route as an integer]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import re
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The route should visit each city exactly once and return to the starting city.",
            "The total distance should match the distance calculated from the provided route."]
        # Extract the route and total distance from the submission
        route_match = re.search(r"Route: \[(.*?)\]", submission)
        distance_match = re.search(r"Total Distance: \[(\d+)\]", submission)
        if not route_match or not distance_match:
            return 0.0
        route = route_match.group(1).split(', ')
        try:
            total_distance = int(distance_match.group(1))
        except ValueError:
            return 0.0
        # Check if the route visits each city exactly once and returns to the starting city
        if set(route) != set(t['cities']) or route[0] != route[-1]:
            return 0.0
        # Calculate the total distance of the provided route
        calculated_distance = 0
        for i in range(len(route) - 1):
            pair = (route[i], route[i+1]) if (route[i], route[i+1]) in t['distances'] else (route[i+1], route[i])
            if pair not in t['distances']:
                return 0.0
            calculated_distance += t['distances'][pair]
        # Check if the calculated distance matches the provided total distance
        if calculated_distance != total_distance:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
