import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = [
            "economics", "biology", "physics", "computer science",
            "psychology", "music", "architecture", "literature"
        ]
        target_domains = [
            "social dynamics", "environmental systems", "artificial intelligence",
            "education", "political systems", "art", "medicine", "urban planning"
        ]
        mental_models = [
            "supply and demand", "natural selection", "wave-particle duality",
            "recursion", "cognitive dissonance", "harmony and discord",
            "form follows function", "unreliable narrator"
        ]
        
        tasks = {}
        for i in range(1, 3):
            source = random.choice(source_domains)
            target = random.choice(target_domains)
            model = random.choice(mental_models)
            tasks[str(i)] = {
                "source_domain": source,
                "target_domain": target,
                "mental_model": model
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the mental model of '{t['mental_model']}' from the domain of {t['source_domain']} to the domain of {t['target_domain']}. Your response should include:

1. Original Model (100-150 words):
   Briefly explain the mental model of '{t['mental_model']}' as it is understood in {t['source_domain']}.

2. Translation Process (200-250 words):
   Describe in detail how you would translate this mental model to {t['target_domain']}. Explain your reasoning for each step of the translation process.

3. Translated Model (200-250 words):
   Present your translated mental model in the context of {t['target_domain']}. Provide specific examples or scenarios that illustrate how this translated model functions in the new domain.

4. Implications and Insights (150-200 words):
   Analyze the implications of this translation. What new insights does it provide about both the original and target domains? How might this translation enhance our understanding or approach to problems in {t['target_domain']}?

5. Limitations and Challenges (100-150 words):
   Discuss any limitations or challenges in applying this translated mental model. Are there aspects of the original model that don't translate well? How might these be addressed?

6. Novel Application (100-150 words):
   Propose a novel application or experiment that could be conducted using this translated mental model in {t['target_domain']}. How might it lead to new discoveries or innovations?

Ensure your response demonstrates a deep understanding of both domains, creative problem-solving, and the ability to draw meaningful connections between disparate fields of knowledge. Use domain-specific terminology where appropriate, but explain any complex concepts clearly.

Format your response with clear headings for each section, numbered as above. This will help in the evaluation of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the mental model '{t['mental_model']}' in both {t['source_domain']} and {t['target_domain']}.",
            "The translation process is logical, creative, and well-explained.",
            "The translated model is coherent and applicable in the target domain.",
            "The analysis of implications and insights is thoughtful and reveals new perspectives.",
            "Limitations and challenges of the translation are critically examined.",
            "The proposed novel application is innovative and demonstrates creative problem-solving.",
            "The response is well-formatted with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
