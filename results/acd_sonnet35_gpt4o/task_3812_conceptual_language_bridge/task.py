import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "causality",
            "recursion",
            "emergence",
            "duality",
            "infinity",
            "consciousness",
            "time",
            "complexity"
        ]
        domains = [
            "philosophy",
            "physics",
            "computer science",
            "cognitive science",
            "mathematics",
            "biology"
        ]
        return {
            "1": {"concept": random.choice(concepts), "domain": random.choice(domains)},
            "2": {"concept": random.choice(concepts), "domain": random.choice(domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a conceptual language that bridges human and machine understanding, focusing on the concept of {t['concept']} in the domain of {t['domain']}. Then, use this language to translate a complex idea between natural language and formal logic. Your response should include:

1. Conceptual Language Design (300-350 words):
   a) Describe the key elements and structure of your conceptual language.
   b) Explain how it represents abstract concepts in a way that's understandable to both humans and machines.
   c) Detail how your language incorporates principles from {t['domain']} to represent {t['concept']}.
   d) Provide examples of basic 'vocabulary' and 'grammar' in your language.

2. Representation of {t['concept']} (250-300 words):
   a) Explain how your conceptual language represents {t['concept']} in the context of {t['domain']}.
   b) Provide a specific example of how a complex idea related to {t['concept']} would be expressed in your language.
   c) Discuss any challenges in representing this concept and how your language addresses them.

3. Translation Task (300-350 words):
   a) Present a complex statement about {t['concept']} in natural language.
   b) Translate this statement into your conceptual language.
   c) Then, translate your conceptual language representation into formal logic.
   d) Explain each step of the translation process and any insights gained.

4. Analysis of Translation (200-250 words):
   a) Discuss how your conceptual language preserved or altered the meaning during translation.
   b) Analyze any ambiguities or limitations encountered in the translation process.
   c) Propose how your language could be improved to better capture the nuances of the concept.

5. Potential Applications (150-200 words):
   a) Suggest two potential applications of your conceptual language in AI or cognitive science.
   b) Discuss how this language could facilitate human-AI communication or understanding.

6. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical implications of creating a language that bridges human and machine understanding.
   b) Analyze potential risks or benefits of using such a language for complex reasoning tasks.
   c) Consider the philosophical implications of reducing complex concepts to a formalized language.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and the specific domain and concept you are working with. Be creative and innovative in your language design while maintaining logical consistency. Use appropriate terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear and innovative design for a conceptual language that bridges human and machine understanding, with a focus on {t['concept']} in the domain of {t['domain']}.",
            "The conceptual language effectively represents abstract concepts in a way that's understandable to both humans and machines.",
            f"The translation task successfully converts a complex idea about {t['concept']} from natural language to the conceptual language and then to formal logic.",
            "The analysis of the translation process is insightful and identifies meaningful challenges and potential improvements.",
            "The response addresses ethical and philosophical implications of creating such a conceptual language.",
            "The proposed applications of the conceptual language are innovative and relevant to AI or cognitive science.",
            "The overall response demonstrates deep understanding of linguistics, cognitive science, and the specific domain and concept."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
