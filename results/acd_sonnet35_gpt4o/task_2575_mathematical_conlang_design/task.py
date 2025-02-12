import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Topology",
            "Abstract algebra",
            "Differential geometry",
            "Complex analysis"
        ]
        linguistic_features = [
            "Agglutination",
            "Evidentiality",
            "Ergative-absolutive alignment",
            "Logographic writing system"
        ]
        
        tasks = {}
        for i in range(1, 3):
            math_concept = random.choice(mathematical_concepts)
            ling_feature = random.choice(linguistic_features)
            tasks[str(i)] = {
                "math_concept": math_concept,
                "linguistic_feature": ling_feature
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a constructed language (conlang) optimized for expressing and solving complex mathematical problems, with a focus on {t['math_concept']} and incorporating the linguistic feature of {t['linguistic_feature']}. Then, use your conlang to solve a related mathematical challenge. Your response should include:\n\n1. Conlang Design (300-350 words):\n   a) Describe the key features of your conlang, explaining how they facilitate mathematical expression and problem-solving.\n   b) Explain how you've incorporated {t['linguistic_feature']} into your language design.\n   c) Provide examples of how basic mathematical operations and concepts are expressed in your conlang.\n   d) Discuss how your conlang specifically addresses the mathematical field of {t['math_concept']}.\n\n2. Mathematical Representation (200-250 words):\n   a) Present a unique mathematical notation or symbolism used in your conlang.\n   b) Explain how this notation system enhances problem-solving in {t['math_concept']}.\n   c) Provide a sample equation or theorem written in your conlang's notation.\n   d) Include a lexicon of at least 10 key mathematical terms in your conlang, with their English translations.\n\n3. Problem-Solving Demonstration (250-300 words):\n   a) Present a challenging problem in {t['math_concept']} using standard mathematical notation.\n   b) Translate this problem into your conlang.\n   c) Solve the problem step-by-step using your conlang, explaining your reasoning. Ensure your solution includes at least 5 distinct steps.\n   d) Translate the solution back into standard mathematical notation.\n\n4. Linguistic Analysis (200-250 words):\n   a) Analyze how your conlang's structure influences mathematical thinking and problem-solving.\n   b) Compare the efficiency of your conlang in expressing mathematical concepts to natural languages and standard mathematical notation.\n   c) Discuss any limitations or potential improvements to your conlang.\n\n5. Interdisciplinary Implications (150-200 words):\n   a) Explore potential applications of your mathematical conlang in fields outside of pure mathematics.\n   b) Discuss how your conlang might influence or enhance mathematical education and research.\n   c) Propose an experiment to test the effectiveness of your conlang in mathematical problem-solving compared to traditional methods.\n\nEnsure your response demonstrates a deep understanding of both linguistics and mathematics, particularly in the field of {t['math_concept']}. Be innovative in your language design while maintaining logical consistency and mathematical rigor. Use appropriate technical terminology from both fields and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1100-1350 words. Include a word count at the end of each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design effectively incorporates {t['linguistic_feature']} and facilitates expression in {t['math_concept']}",
            "The mathematical notation and symbolism in the conlang are unique and well-explained",
            "The problem-solving demonstration shows clear steps and reasoning in the conlang, with at least 5 distinct steps",
            "The linguistic analysis provides insightful comparisons between the conlang and other languages/notations",
            "The response demonstrates strong interdisciplinary knowledge integration across linguistics and mathematics",
            "A lexicon of at least 10 key mathematical terms in the conlang is provided",
            "The mathematical problem presented is solved correctly and completely"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
