import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_inputs = ['magnetic fields', 'infrared radiation', 'electric fields', 'quantum fluctuations']
        problem_domains = ['interstellar navigation', 'ecosystem balance prediction', 'quantum entanglement communication', 'multidimensional data visualization']
        
        tasks = [
            {
                "sensory_input": random.choice(sensory_inputs),
                "problem_domain": random.choice(problem_domains)
            },
            {
                "sensory_input": random.choice(sensory_inputs),
                "problem_domain": random.choice(problem_domains)
            }
        ]
        return {"1": tasks[0], "2": tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and using a novel non-human language based on {t['sensory_input']} as the primary sensory input, then use it to solve a complex problem in the domain of {t['problem_domain']}. Your response should include:

1. Xenolinguistic System Design (300-350 words):
   a) Describe the key features of your novel non-human language based on {t['sensory_input']}.
   b) Explain how the language's structure, grammar, or vocabulary is shaped by this unconventional sensory input.
   c) Provide 3-5 example 'words' or 'phrases' in your language, with explanations of their meanings and how they are perceived.
   d) Discuss how your AI system generates and interprets this language.

2. AI Architecture (250-300 words):
   a) Outline the key components of your AI system for creating and using this xenolanguage.
   b) Explain how the system processes and generates communications using {t['sensory_input']}.
   c) Describe any novel AI techniques or architectures you've incorporated to support this unconventional language.
   d) Discuss how your system ensures the language remains consistent and meaningful.

3. Problem-Solving Approach (250-300 words):
   a) Describe how your AI system would approach solving a complex problem in {t['problem_domain']} using the xenolanguage.
   b) Explain the step-by-step process, highlighting how the language influences problem representation and solution generation.
   c) Provide a hypothetical example of the AI's problem-solving process, including sample 'thoughts' or 'communications' in the xenolanguage.

4. Comparative Analysis (200-250 words):
   a) Compare how solutions generated using this xenolanguage might differ from those of a traditional AI system using human language.
   b) Discuss the potential advantages and limitations of using this unconventional language-based approach in {t['problem_domain']}.
   c) Explain how this approach might reveal new insights or methodologies in the problem domain.

5. Implications and Future Research (200-250 words):
   a) Discuss the potential implications of your xenolinguistic AI system for our understanding of language, cognition, and problem-solving.
   b) Explore how this approach might contribute to developing communication systems for non-human intelligence (e.g., alien life, artificial general intelligence).
   c) Propose two specific areas for future research that could extend or apply your xenolinguistic system.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of linguistics, cognitive science, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of how {t['sensory_input']} can be used as a basis for a novel non-human language.",
            f"The AI system design should be innovative and plausible for creating and using a language based on {t['sensory_input']}.",
            f"The problem-solving approach in {t['problem_domain']} should be coherent and demonstrate how the xenolanguage influences the process.",
            "The comparative analysis should offer insightful differences between xenolanguage-based and traditional approaches.",
            "The implications and future research proposals should be thought-provoking and well-reasoned.",
            "The overall response should be creative, logically consistent, and demonstrate deep understanding of linguistics, cognitive science, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
