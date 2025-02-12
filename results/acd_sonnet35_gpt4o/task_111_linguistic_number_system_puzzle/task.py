import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        base_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        operations = ['+', '-', '*', '/']
        
        def generate_task():
            word_map = {w: random.randint(1, 10) for w in base_words}
            equation = f"{random.choice(base_words)} {random.choice(operations)} {random.choice(base_words)}"
            return {
                'word_map': word_map,
                'equation': equation,
                'rule': random.choice(['vowels', 'consonants', 'length'])
            }
        
        return {
            "1": generate_task(),
            "2": generate_task()
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        example_word = random.choice(list(t['word_map'].keys()))
        example_value = t['word_map'][example_word]
        
        if t['rule'] == 'vowels':
            example_multiplier = sum(1 for c in example_word if c in 'aeiou')
        elif t['rule'] == 'consonants':
            example_multiplier = sum(1 for c in example_word if c not in 'aeiou')
        else:  # length
            example_multiplier = len(example_word)
        
        example_result = example_value * example_multiplier
        
        return f"""You are given a fictional number system based on words. Each word represents a number, and the value of each word is determined by a specific rule. Your task is to solve the given equation using this system.

The word-to-number mapping is as follows:
{', '.join(f'{w}: {v}' for w, v in t['word_map'].items())}

The rule for calculating the value of a word is based on its {t['rule']}:
- If the rule is 'vowels', the value is multiplied by the number of vowels in the word.
- If the rule is 'consonants', the value is multiplied by the number of consonants in the word.
- If the rule is 'length', the value is multiplied by the length of the word.

For example, the word '{example_word}' has a base value of {example_value}. Using the '{t['rule']}' rule, its final value would be {example_value} * {example_multiplier} = {example_result}.

Your task is to solve the following equation: {t['equation']}

Please provide your answer in the following format:

1. Word values:
   [Word 1]: [Base value] * [Multiplier] = [Final value]
   [Word 2]: [Base value] * [Multiplier] = [Final value]

2. Equation:
   [Final value of Word 1] [Operation] [Final value of Word 2] = [Result]

3. Final answer: [Numerical result]

Show all your steps clearly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        
        def solve_equation(eq, word_map, rule):
            def word_value(word):
                base_value = word_map[word]
                if rule == 'vowels':
                    return base_value * sum(1 for c in word if c in 'aeiou')
                elif rule == 'consonants':
                    return base_value * sum(1 for c in word if c not in 'aeiou')
                else:  # length
                    return base_value * len(word)
            
            w1, op, w2 = eq.split()
            v1, v2 = word_value(w1), word_value(w2)
            if op == '+':
                return v1 + v2
            elif op == '-':
                return v1 - v2
            elif op == '*':
                return v1 * v2
            else:  # division
                return v1 / v2
        
        correct_answer = solve_equation(t['equation'], t['word_map'], t['rule'])
        
        criteria = [
            f"The final numerical answer should be {correct_answer}.",
            "The solution should include step-by-step calculations for both words in the equation, showing how their values were determined.",
            "The calculation steps should correctly apply the given rule for determining word values.",
            "The mathematical operation should be performed correctly and clearly shown.",
            "The response should follow the format specified in the instructions, including word values, equation, and final answer."
        ]
        
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
