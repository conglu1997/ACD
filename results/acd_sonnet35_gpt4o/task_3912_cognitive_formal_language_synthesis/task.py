import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                'process': 'Decision Making',
                'key_feature': 'Probabilistic Reasoning',
                'application': 'Analyzing risk assessment in everyday choices'
            },
            {
                'process': 'Memory Formation',
                'key_feature': 'Temporal Sequencing',
                'application': 'Modeling the creation and recall of episodic memories'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(cognitive_processes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel formal language that models the cognitive process of {t['process']}, with a focus on {t['key_feature']}. Then, use your language to analyze and generate examples of human thought patterns related to {t['application']}. Your response should include:

1. Formal Language Design (300-350 words):
   a) Define the alphabet, grammar rules, and syntax of your formal language.
   b) Explain how your language incorporates {t['key_feature']} in its structure.
   c) Describe how your language models the cognitive process of {t['process']}.
   d) Provide a simple example of a valid 'sentence' in your language and explain its cognitive interpretation.

2. Cognitive Process Modeling (250-300 words):
   a) Explain how your formal language captures key aspects of {t['process']}.
   b) Discuss any limitations of your language in modeling this cognitive process.
   c) Compare your approach to traditional methods of modeling {t['process']} in cognitive science.

3. Thought Pattern Analysis (250-300 words):
   a) Use your formal language to analyze a specific example of {t['application']}.
   b) Explain how your language reveals insights about the underlying cognitive processes.
   c) Discuss how this analysis differs from or extends traditional psychological approaches.

4. Thought Pattern Generation (200-250 words):
   a) Generate a novel 'sentence' in your formal language that represents a plausible thought pattern related to {t['application']}.
   b) Translate this 'sentence' into a natural language description of the thought process.
   c) Explain how this generated thought pattern demonstrates {t['key_feature']}.

5. Turing Machine Implementation (200-250 words):
   a) Describe how a Turing machine could be designed to recognize or generate 'sentences' in your formal language.
   b) Explain any challenges in implementing your language on a Turing machine and how they might be overcome.
   c) Discuss the implications of this implementation for understanding the computational nature of {t['process']}.

6. Interdisciplinary Connections (150-200 words):
   a) Explore how your formal language might inform or be informed by research in neuroscience, linguistics, or artificial intelligence.
   b) Propose a novel research question that arises from the intersection of formal language theory and cognitive science in your model.

7. Ethical Implications (150-200 words):
   a) Discuss potential ethical considerations in modeling cognitive processes with formal languages.
   b) Consider possible misuses of your language and propose safeguards against them.
   c) Reflect on the philosophical implications of reducing {t['process']} to a formal language.

Ensure your response demonstrates a deep understanding of formal language theory, cognitive science, and their potential interactions. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and rigorous in your approach, providing clear examples and justifications throughout your answer.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of formal language theory and cognitive science.",
            "The formal language design is innovative, well-explained, and plausibly models the specified cognitive process.",
            "The thought pattern analysis and generation show creative application of the formal language to real-world cognition.",
            "The Turing machine implementation is correctly conceptualized and its implications are thoughtfully discussed.",
            "Interdisciplinary connections and ethical implications are insightfully explored.",
            "The response includes all required sections with appropriate detail and word count.",
            "Technical terminology is used appropriately and explanations are provided where necessary.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
