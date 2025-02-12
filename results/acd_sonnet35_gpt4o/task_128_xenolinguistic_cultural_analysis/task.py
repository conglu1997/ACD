import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_traits = [
            {
                'physiology': 'Beings with four eyes and tentacle-like appendages',
                'environment': 'High-gravity planet with dense atmosphere',
                'communication': 'Primarily visual and tactile',
                'cultural_issue': 'Increasing social isolation due to advanced technology'
            },
            {
                'physiology': 'Crystalline entities that absorb and emit light',
                'environment': 'Low-gravity moon orbiting a gas giant',
                'communication': 'Light-based language using color and intensity',
                'cultural_issue': 'Conflict between traditionalists and progressives over energy consumption'
            }
        ]
        
        return {str(i+1): trait for i, trait in enumerate(random.sample(alien_traits, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a xenolinguist tasked with creating and analyzing an alien language and culture. Your task has two parts:

1. Language Creation:
Create a fictional alien language based on the following traits:
- Physiology: {t['physiology']}
- Environment: {t['environment']}
- Primary mode of communication: {t['communication']}

Provide the following details about the language:
a) Name of the language
b) Brief description of its phonology or visual/tactile elements (depending on communication mode)
c) Three key grammatical features
d) Five sample words or expressions with their meanings

2. Cultural Analysis and Problem-Solving:
Using the language you created, analyze and propose a solution to the following cultural issue:
{t['cultural_issue']}

Your analysis should include:
a) A brief explanation of how the issue arose in the context of the alien society
b) A proposed solution using concepts from the created language
c) An explanation of how the language and cultural features influence the proposed solution

Format your response as follows:

Language Creation:
[Your language details here]

Cultural Analysis and Solution:
[Your analysis and proposed solution here]

Ensure that your language creation is coherent and plausible given the alien traits, and that your cultural analysis demonstrates a clear connection between the created language and the proposed solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The created language is coherent and plausibly reflects the given alien traits.",
            "The language creation includes all required elements: name, phonology/communication description, grammatical features, and sample words/expressions.",
            "The cultural analysis demonstrates a clear understanding of how the issue could arise in the alien society.",
            "The proposed solution effectively uses concepts from the created language.",
            "The response shows a strong connection between the language, culture, and proposed solution."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
