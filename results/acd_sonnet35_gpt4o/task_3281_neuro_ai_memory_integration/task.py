import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_types = [
            "episodic memory (memory of personal experiences and events)",
            "semantic memory (memory of facts and general knowledge)",
            "procedural memory (memory of skills and how to perform tasks)",
            "working memory (short-term memory used for temporary storage and manipulation of information)"
        ]
        integration_approaches = [
            "direct neural interface",
            "non-invasive brain-computer interface",
            "nanobot neural augmentation",
            "optogenetic stimulation"
        ]
        return {
            "1": {
                "memory_type": random.choice(memory_types),
                "integration_approach": random.choice(integration_approaches)
            },
            "2": {
                "memory_type": random.choice(memory_types),
                "integration_approach": random.choice(integration_approaches)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As a neurotechnology researcher specializing in the integration of artificial intelligence with biological neural systems, your task is to design a theoretical model for enhancing human {t['memory_type']} using artificial neural networks via {t['integration_approach']}. Provide your response in the following format:

1. Theoretical Model (300-350 words):
   a) Describe your model for integrating artificial neural networks with biological neural systems to enhance {t['memory_type']}.
   b) Explain how your model leverages {t['integration_approach']} for this integration.
   c) Discuss how your model interacts with and enhances the natural processes of memory formation and retrieval.
   d) Provide a conceptual diagram or detailed description of your model's key components and interactions.

2. Neural Mechanisms (200-250 words):
   a) Explain the specific neural mechanisms involved in your model, both biological and artificial.
   b) Describe how these mechanisms work together to enhance {t['memory_type']}.
   c) Address potential challenges in harmonizing artificial and biological neural processes.

3. AI Architecture (200-250 words):
   a) Outline the key components and algorithms of the artificial neural network used in your model.
   b) Explain how this AI architecture is specifically tailored to enhance {t['memory_type']}.
   c) Describe any novel computational approaches needed to implement your model effectively.

4. Predictions and Testable Hypotheses (200-250 words):
   a) Derive at least two specific, testable predictions from your model.
   b) Explain how these predictions differ from current understanding of memory processes.
   c) Propose experiments or clinical trials to verify these predictions, considering both efficacy and safety.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical considerations of enhancing human memory through AI integration.
   b) Consider potential societal impacts, both positive and negative, if such a technology were developed.
   c) Propose guidelines for responsible research and application of this technology.

6. Future Directions and Limitations (100-150 words):
   a) Identify at least two limitations of your model or its potential implementation.
   b) Propose ideas for future development or expansion of your neuro-AI integration concept.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and their potential synergies. Be creative and original in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words, with each section meeting the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both neuroscience and artificial intelligence, particularly in relation to memory processes.",
            f"The theoretical model for enhancing {t['memory_type']} using {t['integration_approach']} is well-explained and scientifically plausible.",
            "The neural mechanisms and AI architecture are described in detail, showing a clear understanding of how they would interact.",
            "The predictions and proposed experiments are specific, testable, and logically derived from the model.",
            "Ethical and societal implications are thoughtfully considered, with balanced discussion of potential benefits and risks.",
            "The response shows creativity and originality while maintaining scientific rigor.",
            "The writing is clear, well-organized, and uses appropriate technical terminology.",
            "All required sections are addressed, and each section meets the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
