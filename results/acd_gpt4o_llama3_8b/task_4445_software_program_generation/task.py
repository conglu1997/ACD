class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Generate a Python program that reads a CSV file containing sales data with columns: Date, Product, Quantity, and Price. The program should calculate the total sales for each product and output the results to a new CSV file with columns: Product and Total Sales. Example input CSV data: 'Date,Product,Quantity,Price\n2023-01-01,Widget,10,2.50\n2023-01-02,Gadget,5,3.00\n2023-01-03,Widget,5,2.50'. Example output CSV data: 'Product,Total Sales\nWidget,37.50\nGadget,15.00'."
            },
            "2": {
                "requirements": "Generate a Python program that implements a simple text-based calculator. The calculator should be able to perform addition, subtraction, multiplication, and division operations. The program should take input from the user in the form of 'number1 operation number2' (e.g., '3 + 4') and output the result. Ensure the program handles invalid inputs gracefully, such as non-numeric values or unsupported operations. Example input: '3 + 4'. Example output: '7'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a Python program based on the specified requirements: 

Requirements:
{t['requirements']}

Ensure the program is functional, well-structured, and meets all specified requirements. Submit your Python code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The program should be functional and run without errors.",
            "The program should meet all specified requirements.",
            "The code should be well-structured and follow best programming practices."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
