import random
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Linear Equations Practice Test (2 Variables)', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, text)
        self.ln()

def generate_linear_equations():
    # Keep generating until we get equations with reasonable constants
    while True:
        # Generate random integer solutions with smaller range
        x_solution = random.randint(-5, 5)
        y_solution = random.randint(-5, 5)
        
        # Generate random coefficients with smaller range
        a1 = random.randint(1, 5)
        b1 = random.randint(1, 5)
        a2 = random.randint(1, 5)
        b2 = random.randint(1, 5)
        
        # Calculate the right side of each equation based on the solution
        c1 = a1 * x_solution + b1 * y_solution
        c2 = a2 * x_solution + b2 * y_solution
        
        # Check if the constants are not too large
        if abs(c1) <= 30 and abs(c2) <= 30:
            break
    
    # Format equations for display
    equation1 = format_equation(a1, b1, c1)
    equation2 = format_equation(a2, b2, c2)
    
    # Format solution for verification
    solution = f"x={x_solution}, y={y_solution}"
    
    # Create a single string representation of the system
    equation_system = f"{equation1}, {equation2}"
    
    return equation_system, solution, equation1, equation2

def format_equation(a, b, c):
    """Format the equation in readable form"""
    x_term = f"{a}x" if a != 1 else "x"
    
    if b == 1:
        y_term = " + y"
    elif b == -1:
        y_term = " - y"
    elif b > 0:
        y_term = f" + {b}y"
    else:
        y_term = f" - {abs(b)}y"
    
    return f"{x_term}{y_term} = {c}"

def batch_mode():
    """Generate a PDF with multiple problems at once"""
    # Get number of problems to generate
    while True:
        try:
            num_problems = int(input("How many linear equation problems do you want to generate? "))
            if num_problems > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the problems and solutions
    problems = []
    solutions = []
    
    for i in range(num_problems):
        equation_system, solution, _, _ = generate_linear_equations()
        problems.append(f"{i+1}. {equation_system}")
        solutions.append(f"{i+1}. {solution}")
    
    # Create the PDF
    pdf = PDF()
    
    # Add problem page
    pdf.add_page()
    pdf.chapter_title('Practice Questions')
    pdf.chapter_body('\n'.join(problems))
    
    # Add solutions page
    pdf.add_page()
    pdf.chapter_title('Answer Sheet')
    pdf.chapter_body('\n'.join(solutions))
    
    # Save the PDF
    pdf_path = "linear_equations_practice.pdf"
    pdf.output(pdf_path)
    
    print(f"\nGenerated {num_problems} problems and saved to {pdf_path}")
    print("PDF includes both questions and answers on separate pages.")

def interactive_mode():
    """Generate and solve problems one by one interactively"""
    print("\nInteractive Linear Equations Practice")
    print("You'll be given one problem at a time to solve.")
    
    # Track problems and solutions for optional PDF generation at the end
    problems = []
    solutions = []
    problem_count = 0
    
    while True:
        problem_count += 1
        _, solution, equation1, equation2 = generate_linear_equations()
        
        print(f"\nProblem {problem_count}:")
        print(f"Equation 1: {equation1}")
        print(f"Equation 2: {equation2}")
        print("\nSolve for x and y.")
        
        # Wait for user to solve the problem
        input("\nPress Enter when ready to see the solution...")
        print(f"Solution: {solution}")
        
        # Store the problem and solution for potential PDF generation
        problems.append(f"{problem_count}. {equation1}, {equation2}")
        solutions.append(f"{problem_count}. {solution}")
        
        # Ask if they want another problem
        choice = input("\nDo you want another problem? (y/n): ").strip().lower()
        if choice != 'y':
            break
    
    # Ask if they want to save the practice session to PDF
    if problem_count > 0:
        choice = input("\nDo you want to save these problems to a PDF? (y/n): ").strip().lower()
        if choice == 'y':
            # Create the PDF
            pdf = PDF()
            
            # Add problem page
            pdf.add_page()
            pdf.chapter_title('Practice Questions')
            pdf.chapter_body('\n'.join(problems))
            
            # Add solutions page
            pdf.add_page()
            pdf.chapter_title('Answer Sheet')
            pdf.chapter_body('\n'.join(solutions))
            
            # Save the PDF
            pdf_path = "linear_equations_practice.pdf"
            pdf.output(pdf_path)
            
            print(f"\nSaved {problem_count} problems to {pdf_path}")
    
    print("\nThank you for practicing!")

def main():
    print("Linear Equations Problem Generator")
    print("==================================")
    print("1: Interactive mode - Generate and solve problems one by one")
    print("2: Batch mode - Generate a PDF with multiple problems")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1 or 2): "))
            if choice in [1, 2]:
                break
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter a valid number (1 or 2).")
    
    if choice == 1:
        interactive_mode()
    else:
        batch_mode()

if __name__ == "__main__":
    main()