import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emoji_sets = [
            ['🍎', '🍌', '🍊', '🍇', '🍓'],
            ['🐶', '🐱', '🐭', '🐰', '🦊'],
            ['🚗', '🚕', '🚙', '🚌', '🏎️'],
            ['🌞', '🌙', '⭐', '☁️', '🌈'],
            ['🏠', '🏢', '🏫', '🏛️', '🏕️']
        ]
        
        operations = [
            'swap the first and last emoji',
            'reverse the sequence',
            'move the middle emoji to the end',
            'replace all instances of X with Y',
            'insert Z at the beginning'
        ]
        
        def generate_puzzle(emoji_set, operation):
            sequence = random.sample(emoji_set, 3)
            if operation == 'swap the first and last emoji':
                solution = [sequence[-1]] + sequence[1:-1] + [sequence[0]]
            elif operation == 'reverse the sequence':
                solution = sequence[::-1]
            elif operation == 'move the middle emoji to the end':
                solution = [sequence[0], sequence[2], sequence[1]]
            elif operation.startswith('replace all instances of'):
                x, y = random.sample(emoji_set, 2)
                operation = f'replace all instances of {x} with {y}'
                solution = [y if emoji == x else emoji for emoji in sequence]
            else:  # insert Z at the beginning
                z = random.choice([e for e in emoji_set if e not in sequence])
                operation = f'insert {z} at the beginning'
                solution = [z] + sequence
            return ''.join(sequence), operation, ''.join(solution)
        
        tasks = {}
        for i in range(1, 3):
            emoji_set = random.choice(emoji_sets)
            operation = random.choice(operations)
            sequence, operation, solution = generate_puzzle(emoji_set, operation)
            tasks[str(i)] = {
                'sequence': sequence,
                'operation': operation,
                'solution': solution,
                'emoji_set': ''.join(emoji_set)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following emoji logic puzzle:

Given sequence: {t['sequence']}
Operation: {t['operation']}
Available emojis: {t['emoji_set']}

Apply the given operation to the sequence and provide the resulting emoji sequence. Then, create a new puzzle using the same set of emojis and a different operation.

Respond in the following format:

Solution: [Your solution here]
Explanation: [Explain your reasoning for the solution]

New Puzzle:
Sequence: [Your new sequence here]
Operation: [Your new operation here]
Solution: [The solution to your new puzzle]
Explanation: [Explain how to solve your new puzzle]

Ensure that your new puzzle uses only the given set of emojis, has a different operation from the original, and is solvable using the rules established in this task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The solution '{t['solution']}' is correctly provided for the original puzzle.",
            "The reasoning for the original solution is clearly explained and correct.",
            "A new puzzle is created using only the given set of emojis.",
            "The new puzzle uses a different operation from the original.",
            "The new puzzle is solvable and follows the established rules.",
            "A correct solution for the new puzzle is provided.",
            "The reasoning for the new puzzle's solution is clearly explained and correct.",
            "The response follows the specified format exactly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
