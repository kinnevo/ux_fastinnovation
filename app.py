from nicegui import ui

# Define the descriptions for each phase
descriptions = {
    'Empathize': 'In this phase, we focus on understanding the user\'s needs, experiences, and motivations. This involves conducting research, interviews, and observations to gain deep insights into the user\'s perspective.',
    'Define': 'The define phase involves analyzing the information gathered during the empathize phase to identify the core problems and challenges that need to be addressed.',
    'Ideate': 'During ideation, we generate a wide range of creative solutions to the defined problem. This phase encourages thinking outside the box and exploring multiple possibilities.'
}

# Create the header
with ui.header().classes('bg-blue-800 text-white text-center p-4 text-2xl font-bold'):
    ui.label('Design Thinking')

# Create the main container
with ui.row().classes('w-full p-4 gap-4'):
    # Left column (30% width)
    with ui.column().classes('w-1/3'):
        # Create cards
        for phase in ['Empathize', 'Define', 'Ideate']:
            card = ui.card().classes('w-full mb-4 cursor-pointer hover:shadow-lg transition-all duration-200')
            with card:
                ui.label(phase).classes('text-xl font-bold text-blue-800')
                ui.label(descriptions[phase].split('.')[0] + '.').classes('text-gray-600')
            card.on('click', lambda e, p=phase: update_content(p))

    # Right column (70% width)
    with ui.column().classes('w-2/3 bg-gray-50 rounded-lg p-4 min-h-[400px]') as content_area:
        ui.label('Select a card to view details').classes('text-gray-600 text-center w-full')

def update_content(phase):
    content_area.clear()
    with content_area:
        ui.label(phase).classes('text-2xl font-bold text-blue-800 mb-4 text-center w-full')
        ui.label(descriptions[phase]).classes('text-gray-600 text-center w-full')

ui.run(title='Design Thinking') 