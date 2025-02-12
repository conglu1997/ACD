import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "culture1": "Japanese",
                "idiom1": "The nail that sticks out gets hammered down",
                "culture2": "American",
                "idiom2": "The squeaky wheel gets the grease",
                "problem_domain": "workplace communication"
            },
            {
                "culture1": "Russian",
                "idiom1": "The first pancake is always lumpy",
                "culture2": "British",
                "idiom2": "Every cloud has a silver lining",
                "problem_domain": "project management"
            },
            {
                "culture1": "Chinese",
                "idiom1": "The journey of a thousand miles begins with a single step",
                "culture2": "German",
                "idiom2": "Who begins too much accomplishes little",
                "problem_domain": "personal goal setting"
            },
            {
                "culture1": "French",
                "idiom1": "After rain comes sunshine",
                "culture2": "Spanish",
                "idiom2": "No hay mal que por bien no venga (There's no bad from which good doesn't come)",
                "problem_domain": "crisis management"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and apply idiomatic expressions from different cultures to solve abstract problems, then create a novel idiom-based problem-solving framework. Your task has the following parts:

1. Idiom Analysis (200-250 words):
   a) Explain the meaning and cultural context of the {t['culture1']} idiom: "{t['idiom1']}".
   b) Explain the meaning and cultural context of the {t['culture2']} idiom: "{t['idiom2']}".
   c) Compare and contrast the problem-solving approaches suggested by these idioms.

2. Problem-Solving Application (250-300 words):
   a) Describe a specific problem scenario in the domain of {t['problem_domain']}.
   b) Apply the problem-solving approach suggested by each idiom to this scenario.
   c) Analyze the strengths and weaknesses of each approach in this context.

3. Cultural Synthesis (200-250 words):
   a) Propose a novel problem-solving strategy that combines elements from both idiomatic approaches.
   b) Explain how this synthesized approach bridges the cultural perspectives represented by the idioms.
   c) Discuss potential challenges in implementing this approach across different cultural contexts.

4. Novel Idiom Creation (150-200 words):
   a) Create a new idiom that encapsulates your synthesized problem-solving approach. This should be entirely original and not simply restate or combine the given idioms.
   b) Explain the meaning of your idiom and how it reflects the combined cultural insights.
   c) Provide an example of how this new idiom could be applied to a different problem domain.

5. Framework Development (200-250 words):
   a) Outline a general framework for using idiomatic expressions in cross-cultural problem-solving.
   b) Describe the steps involved in applying this framework to new problems or cultural contexts.
   c) Discuss the potential benefits and limitations of this idiom-based approach to problem-solving.

Ensure your response demonstrates a deep understanding of linguistic and cultural nuances, creative problem-solving, and analytical reasoning. Be innovative in your synthesis and framework development while maintaining cultural sensitivity and practical applicability.

Format your response with clear headings for each section, and number your paragraphs within each section for easy reference."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the meanings and cultural contexts of both the {t['culture1']} and {t['culture2']} idioms.",
            "The problem-solving application presents a relevant scenario and effectively applies both idiomatic approaches.",
            "The cultural synthesis creatively combines elements from both idiomatic approaches into a novel strategy.",
            "The newly created idiom is original, not a restatement of the given idioms, and effectively encapsulates the synthesized problem-solving approach.",
            "The proposed framework for idiom-based cross-cultural problem-solving is coherent, generally applicable, and considers potential challenges.",
            "The overall response demonstrates strong analytical reasoning, creative problem-solving skills, and cultural sensitivity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
