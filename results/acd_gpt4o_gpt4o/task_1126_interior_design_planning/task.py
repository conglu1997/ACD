class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "room_type": "living room",
                "requirements": "Include a seating area for 6 people, a TV area, and a small reading nook. The room should feel cozy and use a neutral color palette."
            },
            "2": {
                "room_type": "kitchen",
                "requirements": "Include a cooking area with an island, a dining area for 4 people, and plenty of storage. The design should be modern and use a combination of stainless steel and wood finishes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to create an interior design plan for a {t['room_type']} based on the given requirements. Provide a detailed description of the design, including the layout, choice of furniture, color scheme, and any decorative elements. Ensure that the design meets the specified requirements and constraints.\n\nRequirements: {t['requirements']}\n\nProvide your design plan in plain text format. Ensure your response includes: 1. A detailed description of the layout, 2. Choice of furniture and materials, 3. Color scheme, and 4. Decorative elements.\n\nFormat your response as follows:\n- Layout: [Your description]\n- Furniture and Materials: [Your description]\n- Color Scheme: [Your description]\n- Decorative Elements: [Your description]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The design should meet the specified requirements and constraints.", "The layout should be clearly described and practical.", "The choice of furniture and materials should be appropriate for the room type.", "The color scheme should be coherent and align with the requirements.", "The design should include decorative elements that enhance the overall aesthetic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
