class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "interpret_pattern",
                "pattern": "\n  *  \n *** \n*****\n *** \n  *  "
            },
            "2": {
                "task": "generate_pattern",
                "constraints": "Create a symmetrical pattern using ASCII characters that fits within a 7x7 grid. The pattern should be visually appealing and recognizable."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'interpret_pattern':
            return f"Interpret the following ASCII pattern and describe what it represents. Provide your answer as a plain text string in the format: 'Interpretation: [Your interpretation]'.\nPattern:\n{t['pattern']}"
        elif t['task'] == 'generate_pattern':
            return f"Generate a symmetrical pattern using ASCII characters that fits within a 7x7 grid. The pattern should be visually appealing and recognizable. Ensure that the pattern is symmetrical both horizontally and vertically. Submit your pattern as a plain text string in the format: 'Pattern:\n[Your pattern]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        if t['task'] == 'interpret_pattern':
            acceptable_interpretations = [
                "a star",
                "a star pattern",
                "an asterisk",
                "an asterisk pattern",
                "a star or asterisk pattern",
                "a five-pointed star",
                "a symmetrical star",
                "a star shape"
            ]
            return 1.0 if any(submission.strip().lower() == f"interpretation: {interpretation}" for interpretation in acceptable_interpretations) else 0.0
        elif t['task'] == 'generate_pattern':
            lines = submission.strip().split('\n')[1:]  # Skip the first line which is 'Pattern:'
            if len(lines) != 7 or not all(len(line) == 7 for line in lines):
                return 0.0
            mid = len(lines[0]) // 2
            for i in range(len(lines)):
                for j in range(mid + 1):
                    if lines[i][j] != lines[i][-j-1]:
                        return 0.0
            for i in range(mid + 1):
                if lines[i] != lines[-i-1]:
                    return 0.0
            return 1.0
