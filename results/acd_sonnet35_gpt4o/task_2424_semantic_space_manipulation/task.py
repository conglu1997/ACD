import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time",
            "love",
            "justice",
            "knowledge",
            "freedom"
        ]
        operations = [
            "inversion",
            "negation",
            "amplification",
            "fusion",
            "abstraction"
        ]
        task = {
            "concept": random.choice(concepts),
            "operation": random.choice(operations)
        }
        return {"1": task, "2": task}

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        operation = t["operation"]
        
        return f"Design an AI system that can manipulate and navigate semantic spaces, then use it to perform a semantic operation on a given concept. A semantic space is a conceptual model where words or concepts are represented as points in a multi-dimensional space, with their relationships determined by their relative positions.\n\n" \
               f"Your task has the following parts:\n\n" \
               f"1. Semantic Space Model (250-300 words):\n" \
               f"   a) Describe your AI system's model of semantic space.\n" \
               f"   b) Explain how concepts are represented and related within this space.\n" \
               f"   c) Discuss how your model accounts for context and ambiguity.\n\n" \
               f"2. Semantic Operations (200-250 words):\n" \
               f"   a) Define the semantic operation of {operation}.\n" \
               f"   b) Explain how your AI system performs this operation in the semantic space.\n" \
               f"   c) Discuss any challenges or limitations of implementing this operation.\n\n" \
               f"3. Concept Manipulation (250-300 words):\n" \
               f"   a) Apply the {operation} operation to the concept of '{concept}'.\n" \
               f"   b) Describe the resulting concept or set of concepts.\n" \
               f"   c) Explain how this result relates to the original concept in the semantic space.\n\n" \
               f"4. Abstract Reasoning Application (200-250 words):\n" \
               f"   a) Propose a method for using your semantic space model in abstract reasoning tasks.\n" \
               f"   b) Provide an example of how this could be applied to a specific problem or domain.\n\n" \
               f"5. Novel Concept Generation (200-250 words):\n" \
               f"   a) Describe how your system could use semantic space manipulation to generate novel concepts.\n" \
               f"   b) Generate a novel concept using your system and explain its derivation.\n\n" \
               f"6. Evaluation and Implications (150-200 words):\n" \
               f"   a) Propose methods for evaluating the quality and coherence of your system's semantic operations and concept generations.\n" \
               f"   b) Discuss potential applications and implications of this technology for AI and cognitive science.\n\n" \
               f"Ensure your response demonstrates a deep understanding of semantics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above (1. Semantic Space Model, 2. Semantic Operations, etc.). Include subheadings (a, b, c) where applicable. Your total response should be between 1250-1550 words.\n\n" \
               f"Remember to adhere to the word count guidelines for each section and the overall response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of semantics, cognitive science, and artificial intelligence, with appropriate use of technical terminology.",
            "The semantic space model is well-defined and accounts for context and ambiguity in concept representation.",
            "The semantic operation is clearly explained and applied coherently to the given concept.",
            "The abstract reasoning application and novel concept generation demonstrate creativity and plausibility.",
            "The evaluation methods and implications discussion show critical thinking about the potential impact and limitations of the technology.",
            "The response is well-structured, follows the given format with clear headings and subheadings, and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
