import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "working memory",
            "attention control",
            "cognitive flexibility",
            "processing speed",
            "long-term memory consolidation"
        ]
        return {
            "1": {"cognitive_process": random.choice(cognitive_processes)},
            "2": {"cognitive_process": random.choice(cognitive_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music to enhance {t['cognitive_process']}, then analyze its application for a specific cognitive task. Your response should include:

1. Neuroscientific Foundation (200-250 words):
   a) Explain the neural mechanisms involved in {t['cognitive_process']}.
   b) Discuss how music has been shown to influence this cognitive process.
   c) Identify key auditory features that could potentially enhance this process.

2. AI Composition System (250-300 words):
   a) Design an AI system that can generate music tailored to enhance {t['cognitive_process']}.
   b) Explain how your system incorporates neuroscientific insights into its composition process.
   c) Describe the machine learning algorithms or models you would use for this task.
   d) Discuss how your system would balance cognitive enhancement with musical aesthetics.

3. Music Analysis (200-250 words):
   a) Describe the key characteristics of the music your AI would compose for enhancing {t['cognitive_process']}.
   b) Explain how these characteristics relate to the neural mechanisms discussed earlier.
   c) Provide a short example of a musical phrase or pattern your AI might generate, and explain its intended cognitive effect.

4. Cognitive Task Application (200-250 words):
   a) Choose a specific cognitive task that relies heavily on {t['cognitive_process']}.
   b) Describe how you would apply your AI-generated music to this task.
   c) Predict the potential effects on task performance and explain your reasoning.

5. Evaluation Methodology (150-200 words):
   a) Design an experiment to test the efficacy of your AI-generated music in enhancing {t['cognitive_process']}.
   b) Describe the metrics you would use to measure changes in cognitive performance.
   c) Discuss potential confounding variables and how you would control for them.

6. Ethical Considerations (100-150 words):
   a) Discuss potential risks or ethical concerns associated with using AI-generated music for cognitive enhancement.
   b) Propose guidelines for the responsible development and use of this technology.
   c) Consider potential long-term implications for cognitive development and brain plasticity.

Ensure your response demonstrates a deep understanding of neuroscience, musicology, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive process and its neural mechanisms.",
            "The AI composition system design is innovative, detailed, and scientifically plausible.",
            "The music analysis shows a clear connection between musical elements and cognitive effects.",
            "The cognitive task application is well-reasoned and demonstrates practical understanding.",
            "The evaluation methodology is scientifically sound and addresses potential confounds.",
            "Ethical considerations are thoughtfully explored and addressed.",
            "The response shows strong interdisciplinary reasoning, combining insights from neuroscience, musicology, and AI.",
            "The writing is clear, well-structured, and adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
