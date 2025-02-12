class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "class_diagram", "description": "Design a class diagram for a simple library management system with classes for User, Book, and Loan. Each class should include appropriate attributes and methods and specify relationships between the classes."},
            "2": {"task": "sequence_diagram", "description": "Create a sequence diagram for an online shopping system where a user searches for a product, adds it to the cart, and proceeds to checkout. Specify the interactions between the user, the system, and any other relevant entities."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "class_diagram":
            return "Your task is to design a class diagram for a simple library management system. The system includes the following classes: User, Book, and Loan. Each class should have appropriate attributes (e.g., name, ID) and methods (e.g., borrow(), return()). Specify the relationships between these classes (e.g., one-to-many, many-to-many). Describe the class diagram in detail, specifying the classes, their attributes, methods, and relationships. Provide your response in plain text format, describing the diagram clearly."
        elif t["task"] == "sequence_diagram":
            return "Your task is to create a sequence diagram for an online shopping system. The diagram should depict the interactions when a user searches for a product, adds it to the cart, and proceeds to checkout. Specify the interactions between the user, the system, and any other relevant entities. Describe the sequence diagram in detail, specifying the actors, messages, and the order of interactions. Provide your response in plain text format, describing the diagram clearly."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "class_diagram":
            criteria = [
                "The description should clearly outline the classes, their attributes, methods, and relationships.",
                "The design should follow UML conventions for class diagrams."]
        elif t["task"] == "sequence_diagram":
            criteria = [
                "The description should clearly outline the actors, messages, and order of interactions.",
                "The design should follow UML conventions for sequence diagrams."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
