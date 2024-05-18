Mobile Components Order System

Features:

    Order Creation: Users can send a POST request to the /order endpoint with a JSON payload specifying the components they want to order. The server calculates the total price of the order and returns an order ID along with the total price and the list of selected parts.

    Error Handling: If the user provides an invalid component code, the server returns an error message indicating the invalid component code.

The code is written in Python using the flask framework.

How to Run

    Run the code in Pycharm or any other online IDE for trouble-free working of the program.

    Install Flask by running "pip install flask".

    Run the Flask application by executing python main.py in your terminal.

    Once the server is running, you can send requests to the /order endpoint using a tool like cURL or by running the provided input.py script.

    To interact with the code, inputs can be given to the components list in payload dictionary in the input.py file.

API Endpoints

    POST /order: Create a new order by providing a JSON payload with a list of components.

    GET /: Home endpoint to verify that the server is running.

Unit Tests

    Unit tests are provided in test.py file. These tests cover the creation of orders with valid and invalid components, as well as testing the home endpoint.

    To run the unit tests, execute python test.py in your terminal.
