# page3.py
from nicegui import ui

def create_page3():
    """Create content for Page 3 - Contact/Settings"""
    with ui.element('div').classes('page-content'):
        with ui.card().classes('page-card'):
            ui.html('<h1 style="color: #e74c3c; margin-bottom: 20px;">📞 Page 3 - Contact & Expansion</h1>')
            
            ui.markdown('''
            ### Contact Information & How to Expand
            
            This page shows how **easy it is to add more pages** to the modular application.
            Each page is now cleanly separated into its own file!
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
                    
                    1. Create `pageX.py` with a `create_pageX()` function
                    2. Import it in `main.py`
                    3. Add to the pages dictionary
                    4. The menu updates automatically!
                    
                    **Benefits:**
                    - Clean separation of concerns
                    - Easy to maintain and debug
                    - Perfect for team collaboration
                    - Scalable architecture
                    ''').classes('bg-gray-50 p-4 rounded')

        # Development tips section
        with ui.card().classes('page-card mt-6'):
            ui.html('<h2 style="color: #e74c3c; margin-bottom: 15px;">💡 Development Tips</h2>')
            
            with ui.row().classes('gap-6'):
                with ui.column().classes('flex-1'):
                    ui.label('🎯 Best Practices').classes('font-bold mb-3')
                    
                    practices = [
                        'Keep page functions focused and simple',
                        'Use consistent CSS classes across pages',
                        'Import only what you need in each file',
                        'Test each page independently'
                    ]
                    
                    for practice in practices:
                        with ui.row().classes('items-center gap-3 mb-2'):
                            ui.icon('star', size='1em').classes('text-yellow-500')
                            ui.label(practice).classes('text-sm')
                
                with ui.column().classes('flex-1'):
                    ui.label('🔧 Common Patterns').classes('font-bold mb-3')
                    
                    patterns = [
                        'Use ui.card() for consistent styling',
                        'Wrap content in page-content div',
                        'Add interactive elements for engagement',
                        'Include proper spacing with classes'
                    ]
                    
                    for pattern in patterns:
                        with ui.row().classes('items-center gap-3 mb-2'):
                            ui.icon('build', size='1em').classes('text-blue-500')
                            ui.label(pattern).classes('text-sm')

        # Footer section
        with ui.card().classes('page-card mt-6'):
            ui.html('<h2 style="color: #e74c3c; margin-bottom: 15px;">🎉 Ready to Expand?</h2>')
            
            ui.markdown('''
            Your modular NiceGUI application is ready for growth! Each page is now in its own file,
            making it easy to:
            
            - **Add new features** without affecting existing pages
            - **Collaborate with teammates** on different sections
            - **Maintain code quality** through separation of concerns
            - **Scale efficiently** as your application grows
            
            Happy coding! 🚀
            ''').classes('text-center bg-gradient-to-r from-red-50 to-pink-50 p-6 rounded-lg')