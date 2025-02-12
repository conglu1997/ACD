import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                'language': 'Hopi',
                'feature': 'lacks grammatical tenses for past, present, and future',
                'domain': 'time perception'
            },
            {
                'language': 'Guugu Yimithirr',
                'feature': 'uses absolute spatial references instead of relative ones',
                'domain': 'spatial reasoning'
            },
            {
                'language': 'Pirahã',
                'feature': 'lacks number words and has a "one-two-many" system',
                'domain': 'numerical cognition'
            },
            {
                'language': 'Russian',
                'feature': 'distinguishes between light and dark blue as separate colors',
                'domain': 'color perception'
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the effects of linguistic relativity on artificial cognition and decision-making processes, focusing on the language feature: {t['feature']} in {t['language']}. Your task is to create a novel approach to modeling how this linguistic feature might influence an AI's perception and reasoning in the domain of {t['domain']}.

Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain the principle of linguistic relativity and its relevance to AI systems.
   b) Describe how the specific language feature might influence cognition in humans.
   c) Discuss the challenges and opportunities in applying this concept to artificial intelligence.

2. AI System Architecture (300-350 words):
   a) Design an AI architecture that incorporates the given language feature.
   b) Explain how your system models the influence of this feature on perception and reasoning.
   c) Describe the key components and their interactions within your AI system.
   d) Discuss any novel algorithms or data structures used in your design.

3. Simulation Design (250-300 words):
   a) Propose a specific scenario or task in the given domain to test your AI system.
   b) Describe how you would set up a simulation to compare your AI's performance with a 'control' AI not influenced by the language feature.
   c) Explain what metrics you would use to measure the impact of the language feature on the AI's cognition and decision-making.

4. Predicted Outcomes and Analysis (200-250 words):
   a) Hypothesize how the language feature might affect the AI's performance in the given domain.
   b) Discuss potential advantages or limitations that might arise from this linguistic influence.
   c) Compare your predictions with known effects of this language feature on human cognition.

5. Ethical Implications and Broader Impact (200-250 words):
   a) Discuss the ethical considerations of designing AI systems with specific linguistic biases.
   b) Explore the potential consequences of deploying such AI systems in real-world applications.
   c) Propose guidelines for responsible development and use of linguistically-influenced AI.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or variations of your study.
   b) Discuss how this research might contribute to our understanding of human cognition and language.
   c) Propose a potential application of this research in another field of AI or cognitive science.

Ensure your response demonstrates a deep understanding of linguistic relativity, artificial intelligence, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the concept of linguistic relativity with AI design, focusing on the {t['feature']} of {t['language']}.",
            f"The AI system architecture and simulation design adequately address the influence of the language feature on {t['domain']}.",
            "The response demonstrates creativity and innovation in applying linguistic relativity to AI cognition while maintaining scientific plausibility.",
            "The analysis of predicted outcomes and ethical implications is thoughtful and well-reasoned.",
            "The response shows a high level of understanding in linguistics, cognitive science, and artificial intelligence, using appropriate terminology from all fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
