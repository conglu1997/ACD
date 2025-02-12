import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            {"inspiration": "lotus leaf", "property": "superhydrophobicity"},
            {"inspiration": "gecko feet", "property": "adhesion"},
            {"inspiration": "spider silk", "property": "strength-to-weight ratio"},
            {"inspiration": "butterfly wings", "property": "structural coloration"},
            {"inspiration": "shark skin", "property": "drag reduction"},
            {"inspiration": "mussel adhesive", "property": "underwater adhesion"},
            {"inspiration": "firefly bioluminescence", "property": "light emission"},
            {"inspiration": "cuttlefish skin", "property": "adaptive camouflage"},
            {"inspiration": "desert beetle exoskeleton", "property": "water harvesting"},
            {"inspiration": "plant cell walls", "property": "selective permeability"}
        ]
        return {
            "1": random.choice(biological_inspirations),
            "2": random.choice(biological_inspirations)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel biomimetic material inspired by the {t['inspiration']}, focusing on its {t['property']} property. Your response should include:\n\n1. Material Composition (100-150 words):\n   Describe the chemical composition and structure of your biomimetic material. Explain how it mimics the biological inspiration.\n\n2. Fabrication Process (100-150 words):\n   Outline a potential manufacturing process for your material. Consider scalability and feasibility.\n\n3. Key Properties (100-150 words):\n   Detail the primary properties of your material, focusing on how it achieves the specified {t['property']} property. Include quantitative estimates where possible.\n\n4. Potential Applications (100-150 words):\n   Propose at least two innovative applications for your biomimetic material in different fields (e.g., medicine, construction, energy).\n\n5. Limitations and Challenges (100-150 words):\n   Discuss potential drawbacks or challenges in developing or using this material. Suggest approaches to address these issues.\n\n6. Sustainability Analysis (100-150 words):\n   Evaluate the environmental impact and sustainability of your material compared to existing alternatives.\n\n7. Future Research Directions (50-100 words):\n   Propose a specific area for further research to enhance the material's performance or expand its applications.\n\nEnsure your response demonstrates a deep understanding of the biological inspiration, material science principles, and engineering design considerations. Be creative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['inspiration']} and how it achieves {t['property']}.",
            "The proposed material composition and structure are scientifically plausible and well-explained.",
            "The fabrication process is feasible and considers scalability.",
            "The material properties are quantitatively described where possible.",
            "The proposed applications are innovative and span different fields.",
            "Limitations and challenges are realistically assessed with thoughtful solutions proposed.",
            "The sustainability analysis compares the material to existing alternatives.",
            "The future research direction is specific and relevant to enhancing the material's performance or applications.",
            "The response demonstrates creativity while maintaining scientific accuracy.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
