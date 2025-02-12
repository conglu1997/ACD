import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_patterns = [
            {
                "pattern": "Holistic Thinking",
                "description": "Emphasizes the interdependence of all things and focuses on the whole rather than parts.",
                "problem": "Design a sustainable city that maximizes resource efficiency and community well-being.",
                "scale": ["small town", "major metropolis", "floating ocean colony"]
            },
            {
                "pattern": "Analytical Thinking",
                "description": "Breaks down complex problems into smaller, manageable parts and analyzes them systematically.",
                "problem": "Develop a strategy to reduce traffic congestion in a major metropolitan area.",
                "scale": ["mid-sized city", "sprawling megalopolis", "multi-planet civilization"]
            },
            {
                "pattern": "Divergent Thinking",
                "description": "Generates multiple, unique ideas or solutions to a problem, emphasizing creativity and unconventional approaches.",
                "problem": "Create an innovative educational system that prepares students for jobs that don't yet exist.",
                "scale": ["local community", "entire country", "interstellar society"]
            },
            {
                "pattern": "Convergent Thinking",
                "description": "Focuses on finding a single, well-established answer to a problem, emphasizing speed, accuracy, and logic.",
                "problem": "Determine the most efficient route for a package delivery service in a complex urban environment.",
                "scale": ["bustling downtown", "entire continent", "global network"]
            }
        ]
        selected_patterns = random.sample(cognitive_patterns, 2)
        for pattern in selected_patterns:
            pattern['problem'] = pattern['problem'].replace('a', f'a {random.choice(pattern["scale"])}')
        return {str(i+1): pattern for i, pattern in enumerate(selected_patterns)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an artificial language based on the cognitive pattern of {t['pattern']}, which {t['description']} Then, use this language to approach and solve the following problem:

{t['problem']}

Follow these steps:

1. Language Design (200-250 words):
   a) Describe the key features of your artificial language that reflect the given cognitive pattern.
   b) Explain how the language's structure, grammar, or vocabulary embodies the thought process.
   c) Provide 3-5 example words or phrases in your language, with translations and explanations of how they reflect the cognitive pattern.

2. Problem-Solving Approach (200-250 words):
   a) Explain how you would approach the given problem using your designed language.
   b) Describe the thought process and problem-solving steps in the context of your language.
   c) Highlight how the language's features influence the problem-solving approach.

3. Solution Presentation (150-200 words):
   a) Present your solution to the problem, incorporating key terms or phrases from your designed language.
   b) Explain how the solution reflects the cognitive pattern embedded in the language.

4. Comparative Analysis (100-150 words):
   a) Compare how this solution might differ from one developed using a language based on a different cognitive pattern.
   b) Discuss the potential advantages and limitations of using this language for problem-solving.

5. Real-World Implications (100-150 words):
   a) Discuss how a widespread adoption of this language might affect society, culture, or technological development.
   b) Propose an area of human endeavor that might benefit most from this language and explain why.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of linguistics, cognitive science, and the specific problem domain. Use clear headings for each section of your response and adhere to the word count guidelines provided.

Format your response as follows:

# 1. Language Design
[Your content here]

# 2. Problem-Solving Approach
[Your content here]

# 3. Solution Presentation
[Your content here]

# 4. Comparative Analysis
[Your content here]

# 5. Real-World Implications
[Your content here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed artificial language based on the {t['pattern']} cognitive pattern",
            "The language design includes key features, structure, and 3-5 example words or phrases with translations and explanations",
            "The problem-solving approach clearly utilizes the designed language and explains the thought process",
            f"The solution is presented using key terms or phrases from the designed language and addresses the problem: {t['problem']}",
            "The response includes a comparative analysis discussing how the solution might differ using a language based on a different cognitive pattern",
            "The real-world implications section discusses societal effects and proposes a beneficial area for language adoption",
            "The overall response demonstrates creativity, logical consistency, and deep understanding of linguistics and cognitive science",
            "The response follows the required format with clear headings and adheres to the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
