import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'context': 'Deep space communication',
                'constraints': 'Limited bandwidth, need for error correction',
                'problem': 'Transmit navigation instructions to a distant spacecraft'
            },
            {
                'context': 'Underwater ecosystem monitoring',
                'constraints': 'Low visibility, need for non-invasive communication',
                'problem': 'Alert marine biologists about changes in coral reef health'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a musical language system that can encode and transmit complex information within the following context: {t['context']}. Your system should address these constraints: {t['constraints']}.

1. Musical Language Design (200-250 words):
   a) Describe the basic elements of your musical language (e.g., notes, rhythms, harmonies).
   b) Explain how these elements combine to create meaning.
   c) Discuss how your design addresses the given constraints.

2. Encoding System (150-200 words):
   a) Explain how different types of information are encoded in your musical language.
   b) Provide at least two examples of how specific concepts or data would be represented.

3. Decoding Process (100-150 words):
   Describe how a receiver would interpret and extract information from your musical language.

4. Problem Solution (200-250 words):
   Use your musical language to solve the following problem: {t['problem']}
   a) Explain your approach to encoding the necessary information.
   b) Provide a brief 'musical script' (you can use text to describe the musical elements) that would transmit the solution.
   c) Discuss any challenges in using your system for this specific problem and how you addressed them.

5. Cognitive and Linguistic Implications (100-150 words):
   Analyze how your musical language system might influence cognition and information processing for its users. Consider potential benefits and drawbacks compared to traditional language systems.

Ensure your response is creative, scientifically grounded, and demonstrates a deep understanding of music theory, linguistics, and information encoding. Be specific in your descriptions and explanations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The musical language design is creative, well-structured, and addresses the given constraints.",
            "The encoding system is logical and can represent complex information effectively.",
            "The decoding process is clearly explained and feasible.",
            "The problem solution uses the musical language appropriately and effectively.",
            "The analysis of cognitive and linguistic implications is insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
