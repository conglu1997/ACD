import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "historical_figure": "Leonardo da Vinci",
                "modern_challenge": "Designing sustainable urban transportation systems"
            },
            {
                "historical_figure": "Ada Lovelace",
                "modern_challenge": "Developing quantum-resistant cryptography"
            },
            {
                "historical_figure": "Nikola Tesla",
                "modern_challenge": "Creating a global wireless energy distribution network"
            },
            {
                "historical_figure": "Marie Curie",
                "modern_challenge": "Designing next-generation nuclear fusion reactors"
            },
            {
                "historical_figure": "Alan Turing",
                "modern_challenge": "Developing artificial general intelligence"
            },
            {
                "historical_figure": "Rosalind Franklin",
                "modern_challenge": "Creating personalized medicine based on genomic data"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Imagine how {t['historical_figure']} would approach the modern technological challenge of {t['modern_challenge']}. Your response should include:\n\n" + \
               "1. Historical Context (150-200 words):\n" + \
               f"   - Briefly describe {t['historical_figure']}'s key achievements and areas of expertise.\n" + \
               "   - Explain the relevant scientific and technological context of their time.\n\n" + \
               "2. Knowledge Transfer (200-250 words):\n" + \
               f"   - Analyze how {t['historical_figure']}'s knowledge and methods might apply to {t['modern_challenge']}.\n" + \
               "   - Identify any key concepts or approaches from their era that could be relevant.\n\n" + \
               "3. Modern Problem Analysis (200-250 words):\n" + \
               f"   - Break down the modern challenge of {t['modern_challenge']} into its core components.\n" + \
               "   - Discuss the current state of technology and obstacles in this area.\n\n" + \
               "4. Hypothetical Solution (250-300 words):\n" + \
               f"   - Propose a detailed solution that {t['historical_figure']} might develop for {t['modern_challenge']}.\n" + \
               "   - Explain how this solution combines historical knowledge with modern technological understanding.\n" + \
               "   - Describe any innovative approaches or technologies that might emerge from this combination.\n\n" + \
               "5. Impact Analysis (150-200 words):\n" + \
               "   - Discuss the potential impact of the proposed solution on society and technology.\n" + \
               "   - Analyze any ethical considerations or potential unintended consequences.\n\n" + \
               "Ensure your response demonstrates a deep understanding of both historical and modern scientific principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from both the historical period and modern technology.\n\n" + \
               "Format your response with clear headings for each section. Your total response should be between 950-1200 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the historical figure's work and the modern technological challenge",
            "The proposed solution effectively combines historical knowledge with modern technological concepts",
            "The analysis shows creativity and original thinking in addressing the complex issue",
            "The response is well-reasoned and logically consistent, maintaining scientific plausibility",
            "The impact analysis considers both potential benefits and ethical concerns",
            "The response falls within the specified word count range (950-1200 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
