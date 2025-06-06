from nicegui import ui, app
from typing import Dict, Callable

class FloatingMenuApp1: 
    def __init__(self):
        self.current_page = 'page1'
        self.pages: Dict[str, Callable] = {
            'page1': self.create_page1,
            'page2': self.create_page2,
            'page3': self.create_page3,
            # Easy to add more pages here:
            # 'page4': self.create_page4,
            # 'page5': self.create_page5,
        }
        self.content_container = None
        self.setup_app()

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

    def create_page1(self):
        """Create content for Page 1 - Welcome/Home"""
        with ui.element('div').classes('page-content'):
            with ui.card().classes('page-card'):
                ui.html('<h1 style="color: #667eea; margin-bottom: 20px;">🏠 Welcome to Page 1</h1>')
                
                ui.markdown('''
                ### Welcome to Our Multi-Page Application!
                
                This is the **home page** of our NiceGUI application with a floating menu system.
                
                **Features:**
                - 🎯 Floating navigation menu (top-right corner)
                - 🎨 Modern glassmorphism design
                - 📱 Responsive layout
                - ⚡ Smooth transitions between pages
                - 🔧 Easy to expand with more pages
                
                Use the floating menu to navigate between pages. The menu stays accessible 
                from anywhere in the application!
                ''')
                
                with ui.row().classes('gap-4 mt-6'):
                    with ui.card().classes('p-4 bg-blue-50'):
                        ui.icon('home', size='2em').classes('text-blue-500')
                        ui.label('Home Base').classes('font-bold')
                        ui.label('Your starting point for navigation')
                    
                    with ui.card().classes('p-4 bg-green-50'):
                        ui.icon('explore', size='2em').classes('text-green-500')
                        ui.label('Easy Navigation').classes('font-bold')
                        ui.label('Floating menu for quick access')

    def create_page2(self):
        """Create content for Page 2 - Features/About"""
        with ui.element('div').classes('page-content'):
            with ui.card().classes('page-card'):
                ui.html('<h1 style="color: #764ba2; margin-bottom: 20px;">⚡ Page 2 - Features</h1>')
                
                ui.markdown('''
                ### Application Features & Technical Details
                
                This page demonstrates the **features and capabilities** of our floating menu system.
                ''')
                
                # Interactive elements
                with ui.row().classes('gap-6 mt-6'):
                    with ui.column().classes('flex-1'):
                        ui.label('🛠️ Technical Stack').classes('text-lg font-bold mb-3')
                        
                        tech_items = [
                            ('NiceGUI', 'Modern Python web framework'),
                            ('CSS3', 'Custom animations and glassmorphism'),
                            ('JavaScript', 'Smooth transitions'),
                            ('Responsive Design', 'Works on all devices')
                        ]
                        
                        for tech, desc in tech_items:
                            with ui.card().classes('p-3 mb-2 bg-purple-50'):
                                ui.label(tech).classes('font-semibold text-purple-700')
                                ui.label(desc).classes('text-sm text-gray-600')
                    
                    with ui.column().classes('flex-1'):
                        ui.label('📊 Interactive Demo').classes('text-lg font-bold mb-3')
                        
                        # Counter example
                        counter = ui.number('Counter', value=0).classes('mb-3')
                        
                        with ui.row():
                            ui.button('➕', on_click=lambda: counter.set_value(counter.value + 1)).props('dense')
                            ui.button('➖', on_click=lambda: counter.set_value(max(0, counter.value - 1))).props('dense')
                        
                        # Progress bar
                        ui.label('Progress Demo').classes('mt-4 font-semibold')
                        progress = ui.linear_progress(value=0.3).classes('mt-2')
                        ui.button('Update Progress', 
                                on_click=lambda: progress.set_value((progress.value + 0.1) % 1.1)).classes('mt-2')

    def create_page3(self):
        """Create content for Page 3 - Contact/Settings"""
        with ui.element('div').classes('page-content'):
            with ui.card().classes('page-card'):
                ui.html('<h1 style="color: #e74c3c; margin-bottom: 20px;">📞 Page 3 - Contact & Expansion</h1>')
                
                ui.markdown('''
                ### Contact Information & How to Expand
                
                This page shows how **easy it is to add more pages** to the application.
                ''')
                
                with ui.row().classes('gap-6 mt-6'):
                    # Contact form
                    with ui.column().classes('flex-1'):
                        ui.label('📬 Contact Form').classes('text-lg font-bold mb-4')
                        
                        with ui.card().classes('p-4 bg-red-50'):
                            name_input = ui.input('Your Name').classes('mb-3')
                            email_input = ui.input('Email Address').classes('mb-3')
                            message_input = ui.textarea('Message').classes('mb-3')
                            
                            def submit_form():
                                ui.notify(f'Thank you {name_input.value}! Message received.', 
                                        type='positive', position='top')
                            
                            ui.button('Send Message', on_click=submit_form).props('color=red')
                    
                    # Expansion guide
                    with ui.column().classes('flex-1'):
                        ui.label('🚀 Adding More Pages').classes('text-lg font-bold mb-4')
                        
                        ui.markdown('''
                        **To add a new page:**
                        
                        1. Create a new method: `create_page4(self)`
                        2. Add it to the pages dict: `'page4': self.create_page4`
                        3. That's it! The menu updates automatically.
                        
                        **Example:**
                        ```python
                        def create_page4(self):
                            with ui.element('div').classes('page-content'):
                                ui.label('New Page Content')
                        ```
                        ''').classes('bg-gray-50 p-4 rounded')
                        
                        ui.label('🎯 Benefits:').classes('font-bold mt-4')
                        benefits = [
                            'Automatic menu generation',
                            'Consistent navigation',
                            'Easy maintenance',
                            'Scalable architecture'
                        ]
                        
                        for benefit in benefits:
                            ui.label(f'• {benefit}').classes('ml-4 text-sm')

    # You can easily add more pages like this:
    # def create_page4(self):
    #     """Create content for Page 4 - Dashboard"""
    #     with ui.element('div').classes('page-content'):
    #         with ui.card().classes('page-card'):
    #             ui.html('<h1>📊 Page 4 - Dashboard</h1>')
    #             ui.label('Your dashboard content goes here...')

    def run_home1(self):
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
    app = FloatingMenuApp1()
    app.run_home1()
    
    # Run the NiceGUI app
    ui.run(
        title='Multi-Page App with Floating Menu',
        favicon='🌟',
        port=8080,
        reload=False
    )