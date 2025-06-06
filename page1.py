# page1.py
from nicegui import ui

def create_page1():
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

        # Additional content section
        with ui.card().classes('page-card mt-6'):
            ui.html('<h2 style="color: #667eea; margin-bottom: 15px;">📋 Quick Overview</h2>')
            
            overview_items = [
                ("Modular Design", "Each page is in its own file for easy maintenance"),
                ("Clean Architecture", "Separation of concerns with dedicated modules"),
                ("Scalable Structure", "Add new pages by creating new files"),
                ("Reusable Components", "Common styles and elements across pages")
            ]
            
            for title, description in overview_items:
                with ui.row().classes('items-center gap-3 mb-3'):
                    ui.icon('check_circle', size='1.5em').classes('text-green-500')
                    with ui.column().classes('gap-1'):
                        ui.label(title).classes('font-semibold text-gray-800')
                        ui.label(description).classes('text-sm text-gray-600')