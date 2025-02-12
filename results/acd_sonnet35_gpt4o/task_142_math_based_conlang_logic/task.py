import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_principles = [
            "non-Euclidean geometry",
            "quantum superposition",
            "fractal dimensions",
            "topology"
        ]
        logical_problems = [
            "Using modal logic, express the concept of necessary and possible worlds.",
            "Formulate the Continuum Hypothesis using your conlang's mathematical basis.",
            "Express Gödel's Incompleteness Theorems in your conlang.",
            "Describe a proof of the Riemann Hypothesis using your conlang's unique features."
        ]
        return {
            "1": {"principle": random.choice(math_principles)},
            "2": {"problem": random.choice(logical_problems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "principle" in t:
            return f"You have 30 minutes to create and iterate on a complex constructed language (conlang) based on the mathematical principle of {t['principle']}. Follow these steps:\n\n1. Initial Design (10 minutes):\n   a) Explanation (100 words): Describe your conlang's basic structure.\n   b) Vocabulary (10 words): Provide initial vocabulary with translations.\n   c) Grammar Rules (5 rules): Outline basic grammatical rules.\n\n2. Peer Review (5 minutes):\n   Critically evaluate your initial design. Identify at least 3 weaknesses or areas for improvement.\n\n3. Iteration (15 minutes):\n   a) Refined Explanation (150-200 words): Describe how your conlang incorporates the mathematical principle, addressing the identified weaknesses.\n   b) Expanded Vocabulary (20 words): Provide an expanded vocabulary, explaining how each word embodies the mathematical principle.\n   c) Advanced Grammar Rules (8 rules): Outline more complex grammatical rules that reflect the mathematical principle.\n   d) Number System: Describe a unique number system that integrates the mathematical principle.\n   e) Sample Paragraph: Write a sample paragraph in your conlang, provide its English translation, and break down how it demonstrates the language's advanced mathematical basis.\n\n4. Potential Applications (100 words):\n   Discuss potential real-world applications of your language system, particularly in scientific or technological domains.\n\n5. Reflection (50 words):\n   Reflect on how the iteration process improved your conlang's integration of the mathematical principle.\n\nEnsure your final conlang is logically consistent, highly creative, and clearly demonstrates the integration of the complex mathematical principle."
        else:
            return f"You have 25 minutes to solve the following intricate logical problem using both your conlang and a traditional mathematical approach: {t['problem']}\n\n1. Problem Restatement (2 minutes):\n   Restate the problem in your own words, in both English and your conlang.\n\n2. Conlang Solution (10 minutes):\n   a) Process (200 words): Explain your reasoning using your conlang's unique features.\n   b) Solution: State your conclusion in both your conlang and English.\n\n3. Traditional Approach (10 minutes):\n   a) Process (200 words): Solve the problem using traditional mathematical notation and reasoning.\n   b) Solution: State your conclusion using standard mathematical language.\n\n4. Comparative Analysis (3 minutes, 150 words):\n   Compare and contrast the two approaches. Discuss any insights, advantages, or challenges unique to each method.\n\n5. Metacognitive Reflection (2 minutes, 100 words):\n   Reflect on how your conlang influenced your problem-solving approach and thought process.\n\nEnsure both solutions are logically sound and demonstrate a deep understanding of the problem. Showcase the unique advantages of your mathematically-based language system while acknowledging the strengths of traditional approaches."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "principle" in t:
            criteria = [
                f"The conlang demonstrates a sophisticated incorporation of the mathematical principle of {t['principle']} in its structure, vocabulary, and grammar.",
                "The iteration process shows significant improvement and addresses identified weaknesses.",
                "The number system is unique and effectively integrates the mathematical principle.",
                "The sample paragraph showcases complex linguistic structures that reflect the advanced mathematical basis.",
                "The potential applications are innovative and demonstrate a deep understanding of the mathematical principle's implications.",
                "The overall conlang design is highly creative, logically consistent, and pushes the boundaries of language-mathematics integration.",
                "The reflection demonstrates insightful self-evaluation and understanding of the design process."
            ]
        else:
            criteria = [
                "The problem restatement in the conlang accurately captures the complexity of the logical issue.",
                "The conlang solution process demonstrates advanced use of the language's unique features to approach the problem.",
                "The traditional approach is sound and uses appropriate mathematical notation and reasoning.",
                "The comparative analysis provides deep insights into the strengths and weaknesses of both approaches.",
                "The metacognitive reflection shows a nuanced understanding of how the conlang influences problem-solving strategies.",
                "Both solutions are logically sound and correctly expressed in their respective languages.",
                "The overall response demonstrates creativity, analytical thinking, and the ability to work with multiple abstract systems simultaneously."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
