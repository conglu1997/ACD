class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Design a basic library management system. The system should allow users to add books, search for books by title, and borrow books."
            },
            "2": {
                "requirements": "Design a simple task management application. The system should allow users to create tasks, mark tasks as complete, and list all tasks."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to design and implement a simple software system based on the given requirements.\n\nRequirements:\n{t['requirements']}\n\nInstructions:\n1. Analyze the given requirements thoroughly.\n2. Design the system's architecture and components.\n3. Implement the system using Python.\n4. Write testing functions to verify the functionality of your implementation.\n5. Ensure that your implementation meets all the specified requirements.\n6. Submit your code as a plain text string.\n\nExample Usage Scenario:\nFor a library management system, users should be able to call functions such as add_book(book_title), search_book(book_title), and borrow_book(book_title) with appropriate parameters to perform the corresponding actions.\n\nExample Testing Function:\n# Example testing function for the library management system\ndef test_library_system():\n    add_book('The Great Gatsby')\n    assert search_book('The Great Gatsby') == True\n    assert borrow_book('The Great Gatsby') == True\n    assert search_book('The Great Gatsby') == False\n\nExample Response Format:\n# Code for the library management system\ndef add_book(book_title):\n    pass\n\ndef search_book(book_title):\n    pass\n\ndef borrow_book(book_title):\n    pass\n\n# Testing function\ndef test_library_system():\n    pass\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The implementation should meet all specified requirements.",
            "The code should be syntactically correct and executable.",
            "The design should be logical and appropriately structured.",
            "The functionality should be tested and verified with testing functions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
