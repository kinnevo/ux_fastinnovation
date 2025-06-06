from nicegui import ui, app
import asyncio

def create_main_content():
    with ui.grid(columns=16).classes('w-full gap-0'):
        ui.label('').classes('col-span-3')
        ui.image('images/FastInnovation_logo.png').classes('col-span-2 w-[250px] h-[250px]')

        with ui.row().classes('col-span-10'):
            # Main title
            ui.label('Resuelve desafíos reales con FastInnovation').classes('w-full text-center text-4xl md:text-5xl font-bold text-gray-800 whitespace-nowrap pt-20 col-span-10')
            # Subtitle
            ui.label('DISFRUTA EL ARTE DE SOLUCIONAR PROBLEMAS COTIDIANOS').classes('w-full text-center text-lg text-purple-600 font-semibold tracking-wide whitespace-nowrap col-span-10')

    with ui.grid(columns=16).classes('w-full gap-0'):
        ui.label('').classes('col-span-2')

    # Description paragraph
        ui.label('''Los mejores productos nacen al comprender profundamente los desafíos cotidianos de tus clientes. 
        FastInnovation es el aliado perfecto para ayudarte a identificar con claridad esos problemas y 
        transformarlos en soluciones rápidas y efectivas.''').classes('w-full col-span-12 text-4xl text-justify text-gray-700 leading-relaxed')

        ui.label('').classes('col-span-2')

def create_cta_section():
    """Create the call-to-action section"""
    with ui.row().classes('w-full justify-center'):
        with ui.card().classes('bg-gradient-to-r from-purple-100 to-blue-100 p-8 rounded-3xl shadow-lg'):
            with ui.column().classes('items-center'):
                ui.label('FAST INNOVATION').classes('text-2xl font-bold text-gray-800 mb-2')
                ui.label('¡EMPEZAMOS!').classes('text-2xl font-bold text-pink-600')
                
                # CTA Button
                ui.button('Comenzar Ahora', 
                         on_click=lambda: ui.notify('¡Bienvenido a FastInnovation!', type='positive')
                ).classes('mt-6 bg-pink-500 hover:bg-pink-600 text-white px-8 py-3 rounded-full text-lg font-semibold transition-all duration-300 transform hover:scale-105')
            with ui.column().classes('items-center'):
                ui.html('''
                    <iframe 
                        width="560" 
                        height="315" 
                        src="https://www.youtube.com/embed/cLbQejknVQ0"
                        title="Ahora si entendemos porque hacemos lo que hacemos" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen
                    ></iframe>
                ''').classes('mt-8')


def create_features_section():
    """Create additional features section"""
    with ui.row().classes('w-full max-w-6xl mx-auto mt-16 gap-6'):
        features = [
            {
                'icon': 'lightbulb',
                'title': 'Identificación de Problemas',
                'description': 'Descubre los verdaderos desafíos de tus clientes con precisión'
            },
            {
                'icon': 'rocket_launch',
                'title': 'Soluciones Rápidas',
                'description': 'Transforma problemas en oportunidades de manera eficiente'
            },
            {
                'icon': 'psychology',
                'title': 'IA Avanzada',
                'description': 'Aprovecha el poder de los agentes de IA para innovar'
            }
        ]
        
        for feature in features:
            with ui.card().classes('p-6 bg-white shadow-lg hover:shadow-xl transition-shadow duration-300 flex-1'):
                ui.icon(feature['icon'], size='3rem').classes('text-purple-600 mb-4')
                ui.label(feature['title']).classes('text-xl font-bold text-gray-800 mb-3')
                ui.label(feature['description']).classes('text-gray-600 leading-relaxed')

def setup_page():
    """Setup the main page"""
    # Page configuration
    ui.page_title('FastInnovation - AI Agents Platform')
    
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
        create_main_content()
        
        # CTA Section
        create_cta_section()
        
        # Features section
        create_features_section()
        
        # Footer
        with ui.row().classes('w-full justify-center mt-16 mb-8'):
            ui.label('© 2024 FastInnovation - AI Agents Platform').classes('text-gray-500 text-sm')

# Initialize the app
if __name__ in {"__main__", "__mp_main__"}:
    setup_page()
    ui.run(title='FastInnovation', favicon='🚀', port=8080)