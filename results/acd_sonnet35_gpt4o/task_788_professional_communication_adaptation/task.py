import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        fields = [
            "Medicine",
            "Law",
            "Engineering",
            "Finance",
            "Education",
            "Technology",
            "Environmental Science"
        ]
        
        communication_types = [
            "Email to colleague",
            "Report to supervisor",
            "Presentation to stakeholders",
            "Public announcement",
            "Technical documentation"
        ]
        
        scenarios = [
            "Proposing a new project or initiative",
            "Addressing a critical issue or problem",
            "Sharing important research findings",
            "Requesting resources or support",
            "Explaining a complex concept to non-experts"
        ]
        
        field_specific_terms = {
            "Medicine": ["differential diagnosis", "etiology", "prognosis"],
            "Law": ["precedent", "statute", "tort"],
            "Engineering": ["stress analysis", "load bearing", "thermal conductivity"],
            "Finance": ["liquidity ratio", "EBITDA", "hedge fund"],
            "Education": ["pedagogy", "differentiated instruction", "formative assessment"],
            "Technology": ["API integration", "blockchain", "machine learning"],
            "Environmental Science": ["biodiversity", "carbon footprint", "ecosystem services"]
        }
        
        tasks = {}
        for i in range(1, 3):
            field = random.choice(fields)
            tasks[str(i)] = {
                "field": field,
                "communication_type": random.choice(communication_types),
                "scenario": random.choice(scenarios),
                "field_terms": random.sample(field_specific_terms[field], 2)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are a professional in the field of {t['field']}. Your task is to create a {t['communication_type']} for the following scenario: {t['scenario']}. Incorporate the following field-specific terms in your communication: {', '.join(t['field_terms'])}. Your response should include:\n\n" \
               f"1. The communication itself (200-250 words):\n" \
               f"   Craft the {t['communication_type']} using appropriate tone, terminology, and format for the field of {t['field']}.\n\n" \
               f"2. Explanation of choices (100-150 words):\n" \
               f"   Explain the rationale behind your choice of language, structure, and content, referencing specific aspects of {t['field']} and the given scenario.\n\n" \
               f"3. Audience consideration (100-150 words):\n" \
               f"   Discuss how you tailored the communication to the intended audience, considering their background, expertise, and expectations in the field of {t['field']}.\n\n" \
               f"4. Alternative approach (100-150 words):\n" \
               f"   Briefly describe how this communication might differ if it were for a different audience (e.g., general public, experts in another field) while addressing the same scenario.\n\n" \
               f"Ensure your response demonstrates a deep understanding of professional communication in {t['field']}, as well as the ability to adapt your communication style to different contexts and audiences. Adhere to the specified word limits for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The communication accurately reflects the conventions and terminology of the {t['field']} field, including the use of the provided field-specific terms.",
            f"The content appropriately addresses the given scenario: {t['scenario']}.",
            f"The communication style and format are suitable for a {t['communication_type']}.",
            "The explanation of choices demonstrates a clear understanding of professional communication principles and is consistent with the actual communication provided.",
            "The response shows a thoughtful consideration of the audience and how to tailor the communication effectively.",
            "The alternative approach demonstrates flexibility in communication strategies.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
