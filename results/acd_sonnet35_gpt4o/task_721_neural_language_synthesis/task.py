class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "brain_region": "Broca's area",
                "linguistic_function": "syntax processing",
                "sample_text": "The cat chased the mouse."
            },
            "2": {
                "brain_region": "Wernicke's area",
                "linguistic_function": "semantic processing",
                "sample_text": "The colorless green ideas sleep furiously."
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets language based on simulated neural activity patterns, focusing on {t['brain_region']} and its role in {t['linguistic_function']}. Then, apply your system to translate between 'neural code' (a hypothetical representation of neural activity patterns) and natural language. Your task has the following parts:

1. Neural-Linguistic Model (250-300 words):
   a) Describe how your AI system models the relationship between neural activity in {t['brain_region']} and {t['linguistic_function']}.
   b) Explain the key components of your system and how they interact.
   c) Discuss how your model incorporates current neuroscientific understanding of language processing.
   d) Provide a text-based visual representation (e.g., ASCII art or structured text) of your neural-linguistic model.

2. Neural Code Generation (200-250 words):
   a) For the sample text: "{t['sample_text']}", generate a hypothetical 'neural code' representation.
   b) Explain your reasoning behind this representation, relating it to the function of {t['brain_region']}.
   c) Describe how your AI system would produce this 'neural code'.

3. Natural Language Interpretation (200-250 words):
   a) Demonstrate how your AI system would interpret the 'neural code' to produce natural language.
   b) Explain the process of translating from 'neural code' to words/sentences.
   c) Discuss any challenges in this interpretation process and how your system addresses them.

4. Comparative Analysis (150-200 words):
   a) Compare your neural-linguistic model to traditional natural language processing approaches.
   b) Discuss potential advantages and limitations of your approach.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss the ethical considerations of simulating brain activity for language processing.
   b) Explore potential applications of your system in neuroscience or AI research.
   c) Address any potential risks or misuses of this technology.

Ensure your response is creative yet grounded in current neuroscientific and linguistic theories. Use appropriate terminology and provide clear explanations of your design choices and reasoning. Your entire response should not exceed 1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neurolinguistics and AI systems.",
            "The neural-linguistic model is innovative yet scientifically plausible.",
            "The 'neural code' generation and interpretation processes are clearly explained and logically consistent.",
            "The comparative analysis shows insightful understanding of both traditional NLP and the proposed neural approach.",
            "Ethical implications are thoughtfully considered and addressed.",
            "The response includes a clear text-based visual representation of the neural-linguistic model.",
            "The entire response adheres to the 1200-word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
