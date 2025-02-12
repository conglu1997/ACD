import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        base_sentences = [
            "The cat sat on the mat.",
            "Time flies like an arrow.",
            "All that glitters is not gold.",
            "The early bird catches the worm."
        ]
        transformation_rules = [
            {
                "name": "Adjective Expansion",
                "rule": "Replace each noun with 'the [adjective] [noun]'"
            },
            {
                "name": "Verb Nesting",
                "rule": "Replace each verb with '[subject] [verb] that [full sentence]'"
            },
            {
                "name": "Prepositional Fractal",
                "rule": "Add 'with [noun]' after each noun, where [noun] is derived from the previous noun"
            }
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "base_sentence": random.choice(base_sentences),
                "transformation_rule": random.choice(transformation_rules)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a linguistic fractal based on the following:

Base sentence: "{t['base_sentence']}"
Transformation rule: {t['transformation_rule']['name']} - {t['transformation_rule']['rule']}

Instructions:
1. Apply the transformation rule to the base sentence to create the first iteration.
2. Apply the same rule to the result of step 1 to create the second iteration.
3. Continue this process for a total of 4 iterations.

For each iteration:
- Clearly label the iteration number.
- Present the transformed sentence.
- Explain how you applied the rule, highlighting the changes made.

After completing the iterations:
1. Describe any patterns or self-similarities you observe in the resulting fractal (2-3 sentences).
2. Explain how this linguistic fractal relates to mathematical fractals in terms of structure and complexity (2-3 sentences).
3. Create a simple ASCII art representation of your linguistic fractal, showing its branching structure. Use characters like '|', '-', and '+' to represent the hierarchical relationships between elements.
4. Propose your own novel transformation rule that could generate an interesting linguistic fractal. Explain how it works and what patterns it might produce (2-3 sentences).

Ensure your transformations are consistent and follow the given rule precisely. Be creative in your application of the rule while maintaining grammatical coherence.

Format your response as follows:

Iterations:
[Your 4 iterations with explanations]

Analysis:
[Your analysis of patterns and relation to mathematical fractals]

Visualization:
[Your ASCII art representation]

Novel Transformation Rule:
[Your proposed rule and explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes 4 clearly labeled iterations",
            "Each iteration correctly applies the given transformation rule",
            "The response explains the application of the rule for each iteration",
            "The response describes patterns or self-similarities in the resulting fractal",
            "The response relates the linguistic fractal to mathematical fractals",
            "The transformations maintain grammatical coherence",
            "The response includes an ASCII art visualization of the fractal structure",
            "The response proposes a novel, coherent transformation rule"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
