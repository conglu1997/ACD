import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_periods = [
            {
                "period": "Ancient Agricultural Society",
                "context": "Early farming communities with basic tools and emerging social hierarchies"
            },
            {
                "period": "Medieval Feudal System",
                "context": "Hierarchical society with nobility, clergy, and peasantry; limited literacy"
            },
            {
                "period": "Industrial Revolution",
                "context": "Rapid technological advancement, urbanization, and social change"
            },
            {
                "period": "Information Age",
                "context": "Global digital connectivity, rapid information exchange, and virtual communities"
            },
            {
                "period": "Post-Singularity Era",
                "context": "Advanced AI, transhumanism, and potential interplanetary colonization"
            }
        ]
        return {
            "1": random.choice(historical_periods),
            "2": random.choice(historical_periods)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) and simulate its evolution from its origin to {t['period']}, in the context of {t['context']}. Your task involves the following steps:

1. Conlang Foundation (200-250 words):
   a) Describe the basic features of your conlang (phonology, morphology, syntax).
   b) Explain the cultural and environmental factors that shaped its initial development.
   c) Provide a sample sentence in your conlang with a literal English translation.

2. Historical Evolution (250-300 words):
   a) Trace the evolution of your conlang from its origin to the specified historical period.
   b) Describe at least three significant changes in the language, explaining the historical or cultural reasons for each change.
   c) Provide an example of how a specific word or grammatical feature has evolved.

3. Linguistic Analysis (200-250 words):
   a) Analyze how your conlang reflects the societal structure and values of the specified period.
   b) Explain how technological advancements or historical events have influenced the language.
   c) Compare and contrast features of your evolved conlang with natural languages from similar historical contexts.

4. Vocabulary Expansion (150-200 words):
   a) Create five new words that would have been necessary for the specified historical period.
   b) Explain the etymology of these words and how they fit into the existing language structure.
   c) Provide example sentences using these new words.

5. Speculative Extrapolation (200-250 words):
   a) Predict how your conlang might continue to evolve in the next historical period.
   b) Discuss potential influences from language contact, technological changes, or societal shifts.
   c) Propose a new grammatical feature or linguistic phenomenon that might emerge.

Ensure your response demonstrates a deep understanding of linguistic principles, historical knowledge, and creative language design. Be innovative in your approach while maintaining plausibility within the historical context. Use appropriate linguistic terminology and provide clear examples throughout your response.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design is coherent and demonstrates understanding of linguistic principles.",
            "The language evolution is plausible and reflects the given historical context.",
            "The response includes specific examples of language features and their changes over time.",
            "The analysis demonstrates understanding of how language interacts with society and technology.",
            "The speculative extrapolation is creative yet grounded in linguistic and historical knowledge.",
            "The response follows the specified format and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))