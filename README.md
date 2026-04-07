# Linear Search Visualizer  
CISC 121: Project  
Name: Blaine Cain  
Date: April 6, 2026  

## Demo Videos  

### 1. Random Input Generator Example:  
https://huggingface.co/spaces/blainecain/cisc-121-linear-search-visualizer/resolve/main/Random%20Input%20Generator%20Example.mp4  

### 2. Target Found Example:  
https://huggingface.co/spaces/blainecain/cisc-121-linear-search-visualizer/resolve/main/Target%20Found%20Example.mp4  

### 3. Target Not Found Example:  
https://huggingface.co/spaces/blainecain/cisc-121-linear-search-visualizer/resolve/main/Target%20Not%20Found%20Example.mp4  

### 4. Invalid Input Example:  
https://huggingface.co/spaces/blainecain/cisc-121-linear-search-visualizer/resolve/main/Invalid%20Input%20Example.mp4  

### 5. Using All Features Example:  
https://huggingface.co/spaces/blainecain/cisc-121-linear-search-visualizer/resolve/main/Using%20All%20Features%20Example.mp4  

---

## 1. Project Overview  
This project demonstrates how a linear search algorithm functions step-by-step using an interactive Gradio interface. Users can input a list of numbers and a target value, and the program displays each step of the search process to either find the index of the target or determine that the target is not present in the provided list. The goal of the app is to help beginners understand how linear search works internally by making the process visual, interactive, and easy to follow.

## 2. Algorithm Explanation  
Linear search is a simple searching algorithm that checks each element in a list one by one until it finds the target value or reaches the end of the list. If the target is found, the algorithm returns its index. If not, it returns a “not found” message.

**How the Algorithm Works:**  
- Begin at index 0  
- Compare the current element to the target  
- If they match, then return the index  
- If not, then move to the next element in the list  
- If the end of the list is reached and the target has not been found, return a “not found” message  

This algorithm is straightforward and does not require the list to be sorted, making it ideal for teaching fundamental algorithmic concepts.

## 3. Problem Breakdown & Computational Thinking  
In regards to my choice of algorithm, I landed on linear search because it is simple, intuitive and ideal for demonstrating algorithmic thinking in a step‑by‑step, with an easily integratable visual component as well.

### Decomposition  
Firstly, before jumping into code-writing, I broke the project into a few smaller, more manageable parts:  
- Input: converting the input from the user into a usable list of integers  
- Search logic: implementing the linear search algorithm  
- Step-by-step output: showing each individual step of the algorithm to reach the result  
- UI design: creating a simple, straightforward interface for users to interact with  

Separating the tasks and sub-tasks made the project less overwhelming and helped me focus on one component at a time.

### Pattern Recognition  
Pattern recognition could be easily applied to this problem, as a linear search algorithm follows a predictable pattern:  
- It will always start at the first index of the list  
- It will always check each element in order (regardless of how/if the list is sorted)  
- It will always stop early if the target value is found  

Recognizing and applying these patterns helped when designing the step-by-step output, since each iteration will inevitably follow the same structure.

### Abstraction  
When designing the UI, I took into account that it is unnecessary for the user to see internal aspects of the algorithm, such as how the loop is implemented and how it deals with errors (e.g. invalid inputs). Instead, I chose for the interface to only display: the list, the target value, the checking at each step (both through the textbox and visual representation outputs), and the final result of either the index of the target or a “not found” message. This abstraction ensures that unnecessary complexity is hidden, while highlighting the most important parts of the algorithm. These considerations are especially crucial, as the app is targeted towards those who are beginners at programming and the basic concepts behind searching algorithms may be overcomplicated by these less relevant details.

### Algorithmic Thinking  
When designing and implementing the step-by-step logic, I had to consider:  
- what information the user needs to see at each step  
- how to format the steps clearly and simply  
- how to return the steps in order to maintain accuracy and coherence  
- how to handle invalid input (e.g. non-numerical characters)  

This required planning the sequence of operations prior to writing the code.

## 4. Program Design  
The user interacts with the interface by entering a list of numbers and a target value, then pressing the “Start Search” button to begin the linear search process. After beginning the search, the user will click the “Next Step” button to manually move through each index of the list. The “Search Steps” output box demonstrates how each index is being checked one by one, while the “Visual Representation” output provides a visualization of moving through the indexes until the target is found. Having both of these representations of the linear search’s steps may benefit learners by allowing those with different types of learning styles to follow the algorithm’s process in a way that best suits them.

Additionally, the inclusion of the generator buttons “Generate a Random List” and “Generate a Random Target” allows users to quickly generate inputs that can test various scenarios. The feature encourages exploration and interaction with the UI. Overall, the interface is intentionally very simple so that the focus remains on understanding the algorithm, rather than having to navigate an overly complex UI.

In terms of the choice of library, Gradio worked well for this project because:  
- it helped to quickly create a clean, interactive interface  
- it handles the user input and output formatting automatically  
- it runs easily both locally and online  
- it is beginner-friendly and ideal for educational demonstrations, which is the purpose of this particular project  

As well, the choice of layout is ideal because it clearly separates:  
- **Input section:** This is where the user either enters or generates a list and target value.  
- **Output section:** This is where the step-by-step search results and visual representation are displayed.  

This separation is beneficial, as it helps users visually see and understand the difference between the data they provide (i.e. input) and what the algorithm produces (i.e. output).

## 5. Testing & Verification  
To confirm that my program worked properly, I tested several different types of inputs. This included cases where the target was found early in the list, found later in the list, and not found at all. Also, I tested cases with invalid input (e.g. letters, as opposed to numbers) to ensure that the program would display the appropriate error message. Additionally, I utilized the random list and random target generator buttons to test them and create unpredictable scenarios. All tests behaved as I would have expected, and the step‑by‑step output (both the text and visual outputs) matched the behaviour of the linear search algorithm.

## 6. How to Run the Project  

### To Run Locally:  
For users who want to run the program on their own computer: pip install gradio, python app.py

### To Run Online:  
The following link will lead users to the Hugging Face App:  
https://huggingface.co/spaces/blainecain/cisc-121-linear-search-visualizer  

## 7. Reflection  
This project gave me the opportunity to develop a deeper and more thorough understanding of linear search because I had to break it down into individual steps and explain each one clearly as if I was teaching it. Creating the visual representation output also allowed me to consider how this searching algorithm would look as it functions, rather than just the way its code is structured.

In terms of challenges I faced, I struggled with managing the state between steps, since the search does not run all at once. However, I was able to solve this issue by utilizing Gradio’s state components in order to store the list, target and current index. Also, another difficulty I encountered was designing the interface in a way that felt clean and easy for new users. To make my app feel more intuitive, I decided to reorganize my layout so that certain buttons were grouped together (i.e. “Generate a Random List” with “Generate a Random Target”, and “Start Search” with “Next Step”) and there were headers above the outputs to add further clarity and distinction between the different sections.

Overall, this project was beneficial in helping me learn how to use algorithm logic and user interface design, as well as providing me with experience in deploying a working online app. I am very content with my final product.

## 8. Acknowledgment  
This project was completed for CISC 121 in the Winter 2026 term. Some parts of the implementation were assisted by prompting AI tools.
