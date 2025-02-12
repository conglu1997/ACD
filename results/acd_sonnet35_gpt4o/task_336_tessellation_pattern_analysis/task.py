class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "culture": "Islamic",
                "pattern_name": "Star and Cross",
                "new_constraint": "Include at least one curved element and maintain 4-fold rotational symmetry"
            },
            "2": {
                "culture": "Ancient Greek",
                "pattern_name": "Meander (Greek Key)",
                "new_constraint": "Incorporate a rotational symmetry of order 3 and include a fractal element"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the tessellation pattern '{t['pattern_name']}' from {t['culture']} culture and design a new tessellation based on it. Your response should adhere to the following structure and word limits:

1. Pattern Analysis (250 words max):
   a) Describe the visual appearance of the original pattern.
   b) Explain its cultural significance and historical context.
   c) Analyze its mathematical properties (e.g., symmetry groups, fundamental region).
   d) Discuss the pattern's wallpaper group classification and explain why it belongs to that group.

Note: Wallpaper groups are a mathematical classification of two-dimensional repetitive patterns based on their symmetries. There are 17 distinct wallpaper groups, each characterized by specific combinations of translations, rotations, reflections, and glide reflections.

2. Mathematical Representation (200 words max):
   a) Provide a mathematical description of the pattern using appropriate geometric terminology and notation.
   b) Include at least one formula or equation relevant to the pattern's construction or properties.
   c) Describe the transformations (e.g., translations, rotations, reflections) that generate the pattern.

3. New Tessellation Design (300 words max):
   a) Design a new tessellation pattern inspired by the original, incorporating the following constraint: {t['new_constraint']}.
   b) Describe your new pattern in detail, explaining how it relates to the original and how you incorporated the given constraint.
   c) Analyze the mathematical properties of your new pattern, comparing them to the original.
   d) Classify your new pattern according to the wallpaper group system and justify your classification.
   e) Provide a step-by-step construction method for your new pattern, including any necessary measurements or angles.

4. ASCII Art Representation:
   Create an ASCII art representation of your new tessellation pattern, using a 20x20 character grid. Ensure that the fundamental region and key features of your pattern are clearly visible. Use the following characters to represent different elements:
   - '*' for vertices or intersections
   - '-', '|', '/', '\' for straight lines
   - '(', ')', '{', '}' for curved elements
   - Letters A-Z for distinct regions or shapes

5. Potential Applications (200 words max):
   a) Discuss potential real-world applications of your new tessellation pattern in fields such as art, architecture, materials science, or computer graphics.
   b) Explain how the mathematical properties of your pattern contribute to its potential uses.
   c) Propose an innovative application that leverages the unique features of your design.

Ensure your response demonstrates a deep understanding of geometry, symmetry, and cultural context while showcasing creativity in pattern design. Adhere to the word limits for each section, and use clear, concise language throughout."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately analyzes the original pattern's visual appearance, cultural significance, and mathematical properties, including a correct wallpaper group classification with proper justification.",
            "The mathematical representation is correct, uses appropriate terminology and notation, and includes relevant formulas or equations that accurately describe the pattern's properties or construction.",
            "The new tessellation design incorporates the given constraint, is clearly described, and its mathematical properties are correctly analyzed, including a valid wallpaper group classification.",
            "The step-by-step construction method for the new pattern is clear, logical, and mathematically sound.",
            "The ASCII art representation is a valid 20x20 grid, uses the specified characters, and accurately depicts the described new pattern, clearly showing the fundamental region.",
            "The potential applications discussed are relevant, creative, and clearly linked to the pattern's mathematical properties, with at least one innovative proposal.",
            "The response adheres to the specified word limits for each section and demonstrates a comprehensive understanding of tessellation patterns, their cultural contexts, and advanced geometric concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
