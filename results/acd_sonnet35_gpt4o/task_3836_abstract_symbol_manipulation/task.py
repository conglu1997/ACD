import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        symbol_sets = [
            ['⚪', '⚫', '🔺', '🔻', '◻', '◼'],
            ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘'],
            ['∀', '∃', '∈', '⊆', '∩', '∪', '⊕', '¬']
        ]
        
        operations = [
            'combine',
            'transform',
            'sequence'
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'symbols': random.choice(symbol_sets),
                'operation': random.choice(operations)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        symbols = ' '.join(t['symbols'])
        return f"""You are given a set of abstract symbols: {symbols}

Your task is to analyze these symbols, infer potential rules or patterns governing their relationships, and then use them to perform the operation: {t['operation']}. The operation should be interpreted as a way to manipulate or arrange the symbols based on your inferred rules.

1. Symbol Analysis (100-150 words):
   Describe any patterns, relationships, or properties you observe in the given set of symbols. Consider aspects such as shape, complexity, symmetry, or any other relevant characteristics.

2. Rule Inference (150-200 words):
   Based on your analysis, propose a set of rules that could govern the relationships between these symbols. Your rules should be logical, consistent, and applicable to all symbols in the set. Include at least three distinct rules.
   For example, if the symbols were numbers, a rule might be "Even numbers can only be combined with odd numbers."

3. Operation Execution (200-250 words):
   Using your inferred rules, perform the specified operation ({t['operation']}) with the given symbols. Explain your process step-by-step, showing how you applied your rules. Your result should be a novel arrangement, transformation, or sequence of the symbols that demonstrates a clear application of your inferred rules.
   For example, if the operation was 'combine' and you had a rule about even and odd numbers, you might combine 2 and 3 to create 5, but not 2 and 4.

4. Extrapolation (100-150 words):
   Propose a new symbol that could logically be added to this set based on your inferred rules. Explain how this new symbol fits into the system and how it might interact with the existing symbols.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of abstract pattern recognition and symbolic reasoning. Use clear, concise language to explain your thought process throughout.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if len(submission.split()) < 350:  # Slightly more lenient minimum word count
            return 0.0
        criteria = [
            "The response includes a 100-150 word analysis of the given symbols, describing observed patterns and relationships in a creative and insightful manner.",
            "The response proposes at least three distinct, logical, and consistent rules governing the relationships between the symbols in 150-200 words, showing originality in rule creation.",
            f"The {t['operation']} operation is executed correctly and creatively in 200-250 words, following the inferred rules with a clear, step-by-step explanation that demonstrates novel thinking.",
            "A new symbol is proposed and explained in 100-150 words, fitting logically into the inferred system and showing innovative expansion of the symbolic set.",
            "The overall response demonstrates exceptional abstract reasoning and pattern recognition skills, with a coherent narrative throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
