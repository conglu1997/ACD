import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            ('Ayapaneco', 'Mexico'),
            ('Njerep', 'Cameroon'),
            ('Dumi', 'Nepal'),
            ('Chemehuevi', 'United States')
        ]
        return {
            "1": {"language": random.choice(endangered_languages)},
            "2": {"language": random.choice(endangered_languages)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        language, country = t['language']
        return f"""Design a quantum computing system for preserving and analyzing the endangered language {language} from {country}, then use it to propose novel methods for language revitalization. Your response should include:

1. Quantum Linguistic Architecture (250-300 words):
   a) Describe the key components of your quantum system for language preservation and analysis.
   b) Explain how quantum principles (e.g., superposition, entanglement) are applied to linguistic data.
   c) Discuss how your system integrates cultural context and linguistic features.
   d) Include a diagram or pseudocode representation of your system's architecture (describe it textually).

2. Endangered Language Analysis (200-250 words):
   a) Explain how your quantum system would analyze the structure and features of {language}.
   b) Describe how quantum computing provides unique advantages in this analysis.
   c) Discuss how your system handles ambiguities or context-dependent meanings in the language.

3. Quantum-Enhanced Preservation Techniques (250-300 words):
   a) Propose two novel methods for preserving {language} using your quantum system.
   b) Explain how these methods leverage quantum properties to enhance preservation efforts.
   c) Discuss potential challenges in implementing these techniques and how to overcome them.

4. Language Revitalization Strategies (200-250 words):
   a) Describe two innovative strategies for revitalizing {language} using insights from your quantum analysis.
   b) Explain how these strategies address specific challenges faced by {language}.
   c) Discuss how your quantum system could monitor and adapt these strategies over time.

5. Ethical and Cultural Implications (150-200 words):
   a) Discuss potential ethical concerns related to using quantum technology for language preservation.
   b) Address how your system respects and incorporates the cultural context of {language}.
   c) Propose guidelines for responsible development and use of quantum systems in linguistic and cultural preservation.

6. Future Research Directions (150-200 words):
   a) Suggest two specific research directions to enhance your quantum linguistic preservation system.
   b) Discuss potential applications of your system beyond endangered language preservation.
   c) Speculate on how this technology might influence our understanding of language evolution and cognitive linguistics.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        language, country = t['language']
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing principles and their application to linguistic analysis and preservation of {language}.",
            "The proposed quantum linguistic architecture is innovative, well-explained, and plausible given current quantum computing capabilities.",
            "The language revitalization strategies are creative, culturally sensitive, and address specific challenges faced by the endangered language.",
            "Ethical and cultural implications are thoroughly considered, with thoughtful guidelines proposed.",
            "The response shows interdisciplinary integration of quantum computing, linguistics, and cultural anthropology concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
