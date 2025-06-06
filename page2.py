# page2.py
from nicegui import ui

def create_page2():
    """Create content for Page 2 - Features/About"""
    with ui.element('div').classes('page-content'):
        with ui.card().classes('page-card'):
            ui.html('<h1 style="color: #764ba2; margin-bottom: 20px;">⚡ Page 2 - Features</h1>')
            
            ui.markdown('''
            ### Application Features & Technical Details
            
            This page demonstrates the **features and capabilities** of our floating menu system.
            Each page is now in its own separate file for better organization!
            ''')
            
            # Interactive elements
            with ui.row().classes('gap-6 mt-6'):
                with ui.column().classes('flex-1'):
                    ui.label('🛠️ Technical Stack').classes('text-lg font-bold mb-3')
                    
                    tech_items = [
                        ('NiceGUI', 'Modern Python web framework'),
                        ('Modular Design', 'Each page in separate files'),
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

        # File structure section
        with ui.card().classes('page-card mt-6'):
            ui.html('<h2 style="color: #764ba2; margin-bottom: 15px;">📁 File Structure</h2>')
            
            ui.markdown('''
            The application is now organized into separate files:
            
            ```
            project/
            ├── main.py      # Main application and floating menu
            ├── page1.py     # Home page content
            ├── page2.py     # Features page content
            └── page3.py     # Contact page content
            ```
            
            **Benefits of this structure:**
            - **Maintainability**: Each page can be edited independently
            - **Scalability**: Easy to add new pages without touching existing code
            - **Collaboration**: Different developers can work on different pages
            - **Reusability**: Page functions can be imported and reused
            ''').classes('bg-gray-50 p-4 rounded')

        # Code example section
        with ui.card().classes('page-card mt-6'):
            ui.html('<h2 style="color: #764ba2; margin-bottom: 15px;">💻 Code Example</h2>')
            
            ui.markdown('''
            **Adding a new page is simple:**
            
            1. Create `page4.py`:
            ```python
            # page4.py
            from nicegui import ui
            
            def create_page4():
                with ui.element('div').classes('page-content'):
                    with ui.card().classes('page-card'):
                        ui.label('Page 4 Content')
            ```
            
            2. Import in `main.py`:
            ```python
            from page4 import create_page4
            
            # Add to pages dictionary
            'page4': create_page4
            ```
            
            That's it! The floating menu automatically includes the new page.
            ''').classes('bg-blue-50 p-4 rounded')