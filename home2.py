from nicegui import ui, app
import asyncio

def create_navigation_card():
    """Create a floating navigation card"""
    with ui.card().classes('fixed bottom-4 right-4 bg-white/90 backdrop-blur-sm shadow-xl rounded-xl p-4 z-50'):
        with ui.column().classes('gap-2'):
            ui.label('Navigation').classes('text-lg font-bold text-gray-800 mb-2')
            
            # List of pages with their display names
            pages = [
                ('Home', '/'),
                ('Landing', '/landing'),
                ('Design Thinking', '/design-thinking'),
                ('Design Thinking Platform', '/design-thinking-platform'),
                ('Onboarding', '/onboarding'),
                ('Slider', '/slider'),
                ('DT 1', '/dt-1'),
                ('DT', '/dt')
            ]
            
            for name, route in pages:
                ui.link(name, route).classes('text-purple-600 hover:text-purple-800 transition-colors duration-200')

def setup_page_home2():
    """Setup the main page"""
    # Page configuration
    ui.page_title('FastInnovation - Navigation')
    
    # Add custom CSS for better styling
    ui.add_head_html('''
    <style>
        body { 
            background: white;
            min-height: 100vh;
        }
        .nicegui-content {
            padding: 2rem 1rem;
        }
    </style>
    ''')
    
    with ui.column().classes('w-full min-h-screen'):
        # Main content
        ui.label('Welcome to FastInnovation').classes('text-4xl font-bold text-gray-800 text-center mt-8')
        ui.label('Use the navigation card in the bottom right to explore different sections').classes('text-xl text-gray-600 text-center mt-4')
        
        # Add the floating navigation card
        create_navigation_card()

# Initialize the app
if __name__ in {"__main__", "__mp_main__"}:
    setup_page_home2()
    ui.run(title='FastInnovation', favicon='🚀', port=8080)
