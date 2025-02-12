class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"app_type": "e-commerce", "requirements": "The interface should include a homepage, product listings, search functionality, and a shopping cart."},
            "2": {"app_type": "social media", "requirements": "The interface should include a user profile, news feed, messaging system, and notification alerts."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        app_type = t["app_type"]
        requirements = t["requirements"]
        return f"""Design a user interface (UI) specification for a {app_type} application. Ensure that your design includes all the necessary components as specified in the requirements below:

Requirements:
{requirements}

Your specification should include the following:
1. A brief description of the overall design concept.
2. A detailed description of each interface component, including its purpose and functionality.
3. A wireframe or layout sketch for each major screen (you can describe the layout in text if you can't provide sketches).

Submit your UI specification as a plain text string in the format:

Design Concept: [Your description here]

Component Descriptions:
1. [Component 1]: [Description]
2. [Component 2]: [Description]
...

Wireframes:
1. Homepage: [Description of layout]
2. Product Listings: [Description of layout]
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The UI design should include all specified components.",
            "The descriptions should accurately convey the purpose and functionality of each component.",
            "The wireframes or layout descriptions should be logical and coherent.",
            "The overall design should be user-friendly and adhere to UI/UX best practices."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
