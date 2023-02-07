# Calculator-Application:
A simple calculator application built using Python 3.x.

Technologies Used:
  - Python 3.x
  
Description:

The Calculator Application is a simple calculator that allows users to perform mathematical calculations by entering an expression in the format num1 operator num2. The application is implemented using Python 3.11.1 and uses the eval function to process the user's input and calculate the result.

Key Parts of the Code:

- calculate function: This function takes an expression as an argument and returns the result of the calculation by using the eval function.
- operators list: This list contains the valid operators that the user can use in their calculations.
- while loop: This loop allows the user to repeatedly enter calculations until they decide to exit the application by entering 'exit'.
- try-except block: This block is used to handle any errors that may occur during the calculation process. If an error occurs, the user is prompted to try again.

Design Decisions:

The design of the Calculator Application was kept simple for ease of use. The user interface is minimal, consisting only of the instructions and a prompt to enter the calculation. The user can enter any valid expression and the application will calculate the result.

The choice to use the eval function was made because it is a simple and efficient way to process the user's input and calculate the result. However, it should be noted that the eval function can be dangerous if used improperly, as it can execute arbitrary code. To mitigate this risk, the user input is checked for validity before being passed to the eval function.

Reflection:

Working on the Calculator Application was a great learning experience. I was able to apply my knowledge of Python to build a functional and user-friendly application. One of the challenges I faced was figuring out how to handle invalid inputs, but I was able to overcome this by using a try-except block.

I learned that even simple applications like this can be useful and have a lot of potential for further development. Additionally, I learned the importance of considering security when working with the eval function.

Additional Resources:

Python documentation: https://docs.python.org/3/

Stack Overflow: https://stackoverflow.com/
