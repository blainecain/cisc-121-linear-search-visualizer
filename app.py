import gradio as gr


# Linear Search Algorithm

def linear_search_steps(arr, target_value):
    steps = []
    diagrams = []

    for index in range(len(arr)):
        steps.append(f"Checking index {index}: Value = {arr[index]}")
        diagrams.append(create_list_diagram(arr, current_index=index))

        if arr[index] == target_value:
            steps.append(f"The target, {target_value}, was found at index {index}!")
            diagrams.append(create_list_diagram(arr, current_index=index))
            return "\n".join(steps), diagrams[-1]

    steps.append(f"The target, {target_value}, was not found in the list.")
    diagrams.append(create_list_diagram(arr, current_index=None))
    return "\n".join(steps), diagrams[-1]


# Interface Wrapper

import random

def generate_random_list():
    arr = [random.randint(1, 25) for _ in range(6)]
    return ", ".join(str(x) for x in arr)

def generate_random_target(list_str):
    try:
        arr = [int(x.strip()) for x in list_str.split(",")]
        import random
        return str(random.choice(arr))
    except:
        return "Error: Please either enter or randomly generate a valid list first."

def create_list_diagram(arr, current_index=None):
    html = ""
    for i, val in enumerate(arr):
        if i == current_index:
            # Highlight the current index
            html += f"<div style='display:inline-block; padding:10px; margin:5px; border:2px solid red; background-color:#ffe6e6;'>{val}</div>"
        else:
            html += f"<div style='display:inline-block; padding:10px; margin:5px; border:1px solid black;'>{val}</div>"
    return html

def start_search(list_str, target_str):
    try:
        arr = [int(x.strip()) for x in list_str.split(",")]
        target = int(target_str)
    except:
        return "Invalid input.", "", None, None, None

    # Start at index 0
    idx = 0

    # Create the initial diagram
    diagram = create_list_diagram(arr, current_index=idx)

    message = f"Starting search... Checking index {idx}: Value = {arr[idx]}"

    return message, diagram, arr, target, idx

def next_step(arr, target, idx):
    if arr is None or target is None or idx is None:
        return "Please click 'Start Search' first.", "", None

    # If the index is out of range, then the search is over
    if idx >= len(arr):
        diagram = create_list_diagram(arr, current_index=None)
        return "The target was not found in the list.", diagram, idx

    # Check the current index
    if arr[idx] == target:
        diagram = create_list_diagram(arr, current_index=idx)
        return f"The target, {target}, was found at index {idx}!", diagram, idx

    # Otherwise, move to the next index
    diagram = create_list_diagram(arr, current_index=idx)
    message = f"Checking index {idx}: Value = {arr[idx]}"

    return message, diagram, idx + 1

def linear_search_interface(list_input, target_input):
    # Convert list_input from a string to a list of ints
    try:
        arr = [int(x.strip()) for x in list_input.split(",")]
    except:
        return "Please enter a valid list of numbers separated by commas."

    # Convert target_input to an int
    try:
        target = int(target_input)
    except:
        return "Please enter a valid target number."

    # Run the step-by-step search
    steps, diagram = linear_search_steps(arr, target)
    return steps, diagram


# Gradio UI

with gr.Blocks() as demo:
    gr.Markdown("# Linear Search Visualizer")
    gr.Markdown("Enter a list and a target number to see how linear search works step-by-step.")

    search_array = gr.State()
    search_target = gr.State()
    current_index = gr.State()

    list_input = gr.Textbox(label="Enter a list of numbers separated by commas")
    target_input = gr.Textbox(label="Enter target number")

    with gr.Row():
      random_list_button = gr.Button("Generate a Random List")
      random_target_button = gr.Button("Generate a Random Target")
    
    gr.Markdown("---")

    with gr.Row():
      start_button = gr.Button("Start Search")
      next_button = gr.Button("Next Step")

    gr.Markdown("---")

    gr.Markdown("### Search Steps:")
    output_box = gr.Textbox(label="")

    gr.Markdown("### Visual Representation:")
    diagram_box = gr.HTML(label="")

    # Connecting the buttons
    random_list_button.click(
        generate_random_list,
        inputs=None,
        outputs=list_input
)
    random_target_button.click(
    generate_random_target,
    inputs=list_input,
    outputs=target_input
)
    
    start_button.click(
    start_search,
    inputs=[list_input, target_input],
    outputs=[output_box, diagram_box, search_array, search_target, current_index]
)
    next_button.click(
    next_step,
    inputs=[search_array, search_target, current_index],
    outputs=[output_box, diagram_box, current_index]
)

demo.launch()