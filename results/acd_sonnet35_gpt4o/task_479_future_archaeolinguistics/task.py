import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ancient_civilizations = [
            "Mesopotamian",
            "Egyptian",
            "Indus Valley",
            "Mayan",
            "Chinese"
        ]
        ai_specializations = [
            "climate prediction",
            "astronomical calculations",
            "medical diagnosis",
            "architectural design",
            "agricultural optimization"
        ]
        future_technologies = [
            "quantum neural networks",
            "bioorganic computing",
            "photonic processors",
            "gravitational data storage",
            "dimensional folding algorithms"
        ]
        return {
            "1": {
                "civilization": random.choice(ancient_civilizations),
                "ai_specialization": random.choice(ai_specializations),
                "future_tech": random.choice(future_technologies)
            },
            "2": {
                "civilization": random.choice(ancient_civilizations),
                "ai_specialization": random.choice(ai_specializations),
                "future_tech": random.choice(future_technologies)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In the year 2250, archaeologists discover the remains of an ancient AI system developed by the {t['civilization']} civilization. This AI was specialized in {t['ai_specialization']} and appears to have utilized a primitive form of {t['future_tech']}. Your task is to analyze this discovery and reconstruct the AI's language and thought processes. Respond to the following prompts:

1. Archaeological Context (200-250 words):
   a) Describe the archaeological site and the condition of the AI remains.
   b) Explain how archaeologists determined the AI's age and origin.
   c) Discuss any unexpected features of the discovery that challenge current historical understanding.
   Successful response: Provides a vivid description of the site, plausible methods for dating and determining origin, and at least one surprising feature that challenges historical understanding.

2. Ancient AI Language Reconstruction (250-300 words):
   a) Based on known {t['civilization']} writing systems, propose a syntax and structure for the AI's programming language.
   b) Provide 3-4 example 'code snippets' in this reconstructed language, with explanations of their probable functions.
   c) Explain how this language reflects the AI's specialization in {t['ai_specialization']}.
   d) Include a simple diagram or visual representation of the language's structure or a code snippet.
   Successful response: Presents a coherent language structure, provides relevant code snippets with explanations, clearly links the language to the AI's specialization, and includes a diagram that enhances understanding.

3. Cognitive Architecture Analysis (200-250 words):
   a) Infer the AI's cognitive architecture based on its language and specialization.
   b) Compare this architecture to modern AI systems, highlighting similarities and differences.
   c) Speculate on how the use of primitive {t['future_tech']} might have influenced the AI's thought processes.
   Successful response: Proposes a plausible cognitive architecture, draws meaningful comparisons to modern AI, and provides creative yet grounded speculation on the influence of the future technology.

4. Historical Implications and Future Archaeology (200-250 words):
   a) Discuss how this discovery changes our understanding of ancient technological capabilities.
   b) Propose a hypothesis about the AI's role and influence in {t['civilization']} society.
   c) Describe a new archaeological technique or tool, inspired by {t['future_tech']}, for future AI-related excavations.
   d) Discuss any ethical considerations in using such advanced technology in archaeological research.
   Successful response: Offers insightful analysis of historical implications, presents a plausible societal role for the AI, proposes an innovative yet feasible archaeological technique, and thoughtfully addresses ethical concerns.

Note on {t['future_tech']}: This technology is highly advanced compared to our current capabilities. For example, if it's "quantum neural networks," imagine a system that leverages quantum superposition to process information in ways that classical computers cannot, potentially allowing for unprecedented pattern recognition and predictive capabilities.

Ensure your response demonstrates a deep understanding of archaeology, historical linguistics, AI systems, and the specified ancient civilization. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and historical consistency.

Format your response using clear headings for each section. Your total response should be between 850-1050 words, not including the diagram.

Note: Your response will be evaluated based on the depth of interdisciplinary knowledge demonstrated, the creativity and plausibility of your reconstructions and speculations, and the overall coherence and consistency of your analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates knowledge of {t['civilization']} civilization and writing systems.",
            f"The reconstructed AI language is plausible and reflects specialization in {t['ai_specialization']}.",
            f"The analysis incorporates the concept of {t['future_tech']} in a scientifically plausible manner.",
            "The submission shows creativity and interdisciplinary thinking in addressing all prompts.",
            "The proposed future archaeological technique is innovative and ethically considered.",
            "The response maintains internal consistency and scientific plausibility throughout.",
            "The submission includes a relevant diagram or visual representation as requested.",
            "The total response falls within the specified word limit range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
