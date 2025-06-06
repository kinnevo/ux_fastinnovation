# main.py
from nicegui import ui, app
from typing import Dict, Callable
from page1 import create_page1
from page2 import create_page2
from page3 import create_page3
from home1 import FloatingMenuApp1 as Home1App
from home2 import setup_page_home2
from landing import setup_page
from design_thinking_platform import DesignThinkingPlatform as DTP
from onboarding import DesignThinkingApp1 as OnboardingApp
from slider import CardSlider as SliderApp

class FloatingMenuApp:
    def __init__(self):
        self.current_page = 'page1'
        self.pages: Dict[str, Callable] = {
            'page1': create_page1,
            'page2': create_page2,
            'page3': create_page3,
            'Home1': Home1App().run_home1,
            'Home2': setup_page_home2,
            'Landing': setup_page,
            'Design Thinking': DTP().build_ui,
            'Onboarding': OnboardingApp().create_ui,
            'Slider': SliderApp().create_ui,
            'Index': self.show_index,
            # Easy to add more pages here:
            # 'page4': create_page4,
            # 'page5': create_page5,
        }
        self.content_container = None
        self.setup_app()
        app.add_static_files('/static', 'static')  # This points to the static directory

    def setup_app(self):
        """Initialize the app with custom CSS and main layout"""
        # Custom CSS for floating menu and smooth transitions
        ui.add_head_html('''
        <style>
            .floating-menu {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1000;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 10px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            .menu-button {
                margin: 5px;
                min-width: 80px;
                border-radius: 10px !important;
                transition: all 0.3s ease;
            }
            .menu-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            }
            .page-content {
                padding: 20px;
                max-width: 1200px;
                margin: 0 auto;
                animation: fadeIn 0.5s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .page-card {
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                margin: 20px 0;
            }
        </style>
        ''')

    def create_floating_menu(self):
        """Create the floating menu with navigation buttons"""
        with ui.element('div').classes('floating-menu'):
            ui.label('Navigate').classes('text-sm font-bold text-gray-600 mb-2')
            
            for page_key in self.pages.keys():
                page_name = page_key.replace('page', 'Page ')
                button_color = 'primary' if page_key == self.current_page else 'secondary'
                
                ui.button(
                    page_name, 
                    on_click=lambda p=page_key: self.navigate_to(p)
                ).classes(f'menu-button').props(f'color={button_color} rounded')

    def navigate_to(self, page_key: str):
        """Navigate to a specific page"""
        if page_key in self.pages:
            self.current_page = page_key
            self.refresh_content()

    def refresh_content(self):
        """Refresh the main content area"""
        if self.content_container:
            self.content_container.clear()
            with self.content_container:
                self.pages[self.current_page]()

    def show_index(self):
        """Show the index.html content"""
        with ui.element('div').classes('page-content'):
            with ui.card().classes('page-card'):
                ui.html('<h1 style="color: #667eea; margin-bottom: 20px;">📑 Index</h1>')
                ui.link('Open index.html', '/static/index.html', new_tab=True).classes('text-blue-500 hover:text-blue-700')

    def run(self):
        """Run the application"""
        # Create main layout
        with ui.column().classes('w-full min-h-screen'):
            # Floating menu
            self.create_floating_menu()
            
            # Main content container
            self.content_container = ui.element('div').classes('flex-1')
            
            # Load initial page
            with self.content_container:
                self.pages[self.current_page]()

# Create and run the app
if __name__ in {"__main__", "__mp_main__"}:
    app = FloatingMenuApp()
    app.run()
    
    # Run the NiceGUI app
    ui.run(
        title='Multi-Page App with Floating Menu',
        favicon='🌟',
        port=8080,
        reload=False
    )