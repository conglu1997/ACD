import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'environment': 'Underwater city',
                'technology': 'Brain-computer interfaces',
                'time_frame': '200 years'
            },
            {
                'environment': 'Martian colony',
                'technology': 'Quantum computing',
                'time_frame': '150 years'
            },
            {
                'environment': 'Orbital space station',
                'technology': 'Nanotechnology',
                'time_frame': '100 years'
            },
            {
                'environment': 'Underground megacity',
                'technology': 'Artificial photosynthesis',
                'time_frame': '250 years'
            }
        ]
        return {str(i+1): random.choice(scenarios) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze the evolution of a hypothetical language for a human population living in an {t['environment']} with widespread use of {t['technology']} over a period of {t['time_frame']}. Your response should include:

1. Language Design (300-350 words):
   a) Describe the key features of your evolved language, including phonology, morphology, syntax, and semantics.
   b) Explain how the environment and technology have influenced these features.
   c) Provide at least three example sentences in your language with translations and explanations.
   d) Include a brief description of the writing system or alternative communication method used.

2. Cognitive Adaptations (250-300 words):
   a) Analyze how the human brain might adapt to process and produce this language efficiently.
   b) Discuss any potential changes in cognitive processes related to memory, attention, or spatial reasoning.
   c) Explain how {t['technology']} might interact with or enhance these cognitive adaptations.

3. Cultural and Social Implications (200-250 words):
   a) Describe how the evolved language reflects and shapes the culture of its speakers.
   b) Discuss potential changes in social structures or interpersonal communication.
   c) Analyze how the language might influence or be influenced by power dynamics in the society.

4. Linguistic Relativity Analysis (200-250 words):
   a) Explore how this language might affect its speakers' perception and conceptualization of their environment.
   b) Discuss any unique concepts or cognitive frameworks that might emerge due to the language's structure.
   c) Compare these effects to known examples of linguistic relativity in existing human languages.

5. Language Acquisition and Education (150-200 words):
   a) Propose how children or newcomers would learn this language.
   b) Describe any unique challenges in language acquisition due to the environmental or technological context.
   c) Suggest potential teaching methods or tools that could aid in language learning.

6. Future Trajectory and Variations (150-200 words):
   a) Predict how the language might continue to evolve beyond the given time frame.
   b) Discuss potential dialectal variations that might emerge in different parts of the {t['environment']}.
   c) Consider how contact with other human languages or potential extraterrestrial communication might influence the language.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and cultural anthropology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of linguistic principles and their potential evolution in the context of an {t['environment']} with {t['technology']}.",
            "The language design is creative, well-explained, and plausible given the environmental and technological context.",
            "The analysis of cognitive adaptations shows a deep understanding of neuroscience and cognitive psychology.",
            "The discussion of cultural and social implications is insightful and considers multiple factors.",
            "The linguistic relativity analysis demonstrates a thorough understanding of the concept and applies it creatively to the hypothetical language.",
            "The proposed language acquisition methods are innovative and appropriate for the given context.",
            "The future trajectory and variations are thoughtfully considered and plausible.",
            "The response adheres to the specified format and word count, and demonstrates appropriate use of technical terminology from linguistics, cognitive science, and cultural anthropology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
