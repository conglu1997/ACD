import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "deep space",
            "underwater"
        ]
        cognitive_aspects = [
            "spatial reasoning",
            "temporal perception",
            "social communication"
        ]
        linguistic_features = [
            "phonology",
            "syntax",
            "semantics"
        ]
        
        tasks = {}
        for i in range(1, 3):
            env = random.choice(environments)
            cog = random.choice(cognitive_aspects)
            ling = random.choice(linguistic_features)
            tasks[str(i)] = {"environment": env, "cognitive_aspect": cog, "linguistic_feature": ling}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical language and cognitive system for intelligent beings evolved in {t['environment']}, focusing on the cognitive aspect of {t['cognitive_aspect']} and the linguistic feature of {t['linguistic_feature']}. Then, propose experiments to test how this environment shapes language and cognition. Your response should include:\n\n1. Environmental Analysis (200-250 words):\n   a) Describe the key characteristics of the {t['environment']} environment, including physical properties and potential challenges for life.\n   b) Explain how these characteristics might influence the evolution of cognition and language.\n   c) Provide a concrete example of how a specific environmental factor could drive cognitive or linguistic adaptation.\n\n2. Cognitive System Design (250-300 words):\n   a) Describe the key features of the cognitive system adapted to this environment.\n   b) Explain how {t['cognitive_aspect']} is uniquely adapted to the environment, providing specific examples.\n   c) Discuss any novel cognitive abilities that might emerge in this setting, and explain their adaptive value.\n   d) Propose a hypothetical scenario demonstrating how these beings would use their adapted cognitive abilities.\n\n3. Language System Design (250-300 words):\n   a) Outline the fundamental structure of the language evolved in this environment.\n   b) Explain how the {t['linguistic_feature']} of this language reflects environmental adaptations.\n   c) Provide at least three examples of unique linguistic constructs in this language, explaining their function and evolution.\n   d) Describe a sample conversation or communication event in this language, highlighting its unique features.\n\n4. Experiment Design (300-350 words):\n   a) Propose an experiment to test how the {t['environment']} environment shapes {t['cognitive_aspect']} and {t['linguistic_feature']}.\n   b) Describe the experimental setup in detail, including control groups, variables, and measurement methods.\n   c) Explain how you would analyze and interpret the results, including potential statistical approaches.\n   d) Discuss potential challenges in conducting such an experiment and propose solutions.\n   e) Describe expected outcomes and their implications for our understanding of language and cognition.\n\n5. Comparative Analysis (200-250 words):\n   a) Compare and contrast your hypothetical cognitive and linguistic systems with those of Earth-based organisms.\n   b) Identify at least three key differences and explain their evolutionary origins.\n   c) Discuss how studying such systems could enhance our understanding of language and cognition in general.\n   d) Propose a specific insight about Earth-based languages or cognition that might be gained from this comparison.\n\n6. Ethical Considerations (150-200 words):\n   a) Discuss ethical implications of studying or potentially communicating with non-Earth based intelligences.\n   b) Propose at least four specific guidelines for responsible research in this field.\n   c) Explore a potential ethical dilemma that might arise in this research and suggest how it could be addressed.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary biology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary biology",
            "The hypothetical cognitive and language systems are creative, plausible, and well-justified given the environmental constraints",
            "The experimental design is comprehensive, well-thought-out, and addresses the specific aspects of cognition and language under investigation",
            "The comparative analysis and ethical considerations show depth of thought, interdisciplinary integration, and consideration of real-world implications",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts",
            "The response is well-structured, following the specified format and word count guidelines",
            "Concrete examples and hypothetical scenarios are provided to illustrate key points",
            "The response demonstrates creativity and original thinking while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
