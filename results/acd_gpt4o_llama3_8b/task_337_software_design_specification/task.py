class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Create a software design specification for a to-do list application. The application should allow users to add, edit, and delete tasks. Each task should have a title, description, due date, and priority level. The application should also allow users to mark tasks as completed. The application should be accessible via both web and mobile platforms and support user authentication."},
            "2": {"requirements": "Create a software design specification for a basic e-commerce website. The website should allow users to browse products, add products to a shopping cart, and checkout. Users should be able to create accounts, log in, and view their order history. The website should support multiple payment methods and have a responsive design for both desktop and mobile devices."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a software design specification based on the following requirements:

{t["requirements"]}

Your specification should include the following sections:
1. Introduction: Provide an overview of the application, its purpose, and its key features.
2. Functional Requirements: List and describe the key functionalities the application must have.
3. Non-Functional Requirements: Describe the performance, usability, and other quality attributes the application must meet.
4. System Architecture: Outline the overall architecture of the application, including the major components and their interactions.
5. Data Model: Define the data structures and relationships that will be used in the application.

Ensure that your specification is clear, detailed, and well-structured. Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The specification should include all required sections.", "The content should be clear, detailed, and well-structured.", "The functional and non-functional requirements should be accurately derived from the given requirements.", "The system architecture and data model should be logical and appropriate for the application.", "The language should be precise and technical.", "The introduction should provide a clear overview and purpose of the application."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
