from web.backend.Global import Global
import networkx as nx
import random 
import matplotlib.pyplot as plt
import io
import base64

'''
Clase Location
Autora: Claudia Landeira

Informacion de las localizaciones
'''
class Location:
    
    '''
    Funcion getAllPaged
    Autora: Claudia Landeira

    Devuelve todos las localizacinos disponibles y sus datos paginados
    '''
    def getAllPaged(page):
        return Global.data(f"{Global.getUrlLocation()}?page={page}")
    
    '''
    Funcion get
    Autora: Claudia Landeira

    Devuelve toda la información por id
    '''
    def getById(idLocation):
        return Global.data(f'{Global.getUrlLocation()}{idLocation}')
    
    '''
    Funcion getByList
    Autora: Claudia Landeira

    Devuelve toda la informacion por lista
    '''
    def getByList(lista):
        return Global.data(f'{Global.getUrlLocation()}{lista}')

    '''
    Funcion filter
    Autora: Claudia Landeira

    Devuelve toda la información dando la posiiblidad de filtrar por nombre y/o tipo
    Todos los parametros son optativos
    '''
    def filter(name=None, type=None):
        param = {}

        if name:
            param['name'] = name
        if type:
            param['type'] = type

        filter = '&'.join(f'{key}={value}' for key, value in param.items())

        if filter:
            url = f'{Global.getUrlLocation()}?{filter}'

        return Global.data(url)
    
    '''
    Funcion info
    Autora: Claudia Landeira

    Devuelve la información referente al numero de localizaciones y su paginacion
    '''
    def info(data):
        info = data['info']
        count = Location.count(info)
        pages = Location.pages(info)
        
        return {'count': count, 'pages': pages}
    
    '''
    Funcion count
    Autora: Claudia Landeira

    Devuelve el numero de localizaciones
    '''
    def count(data):
        return data['count']
    
    '''
    Funcion pages
    Autora: Claudia Landeira

    Devuelve el numero de paginas
    '''
    def pages(data):
        return data['pages']
    
    '''
    Funcion results
    Autora: Claudia Landeira

    Devuelve el valor de los resultados de la localizacion
    '''
    def results(data):
        return data['results']
    
    '''
    Funcion id
    Autora: Claudia Landeira

    Devuelve el id de la localizacion
    '''
    def id(data):
        return data['id']
    
    '''
    Funcion name
    Autora: Claudia Landeira

    Devuelve el nombre de la localizacion
    '''
    def name(data):
        return data['name']
    
    '''
    Funcion type
    Autora: Claudia Landeira

    Devuelve el tipo de localizacion
    '''
    def type(data):
        return data['type']
    
    '''
    Funcion dimension
    Autora: Claudia Landeira

    Devuelve la dimension de la localizacion
    '''
    def dimension(data):
        return data['dimension']
    
    '''
    Funcion residents
    Autora: Claudia Landeira

    Devuelve el listado de personajes de esa localizacion
    '''
    def residents(data):
        return data['residents']
    
    '''
    Funcion createGraph
    Autora: Claudia Landeira

    Devuelve un grafo de tipo NetworkX con las localizaciones
    '''
    def createGraph (locations):
        graph = nx.Graph()

        for location in locations:
            graph.add_node(location['name'])

        connections = set()
        max_connections = len(graph.nodes()) * (len(graph.nodes()) - 1) // 2

        for _ in range(max_connections):
            node1 = random.choice(list(graph.nodes()))
            node2 = random.choice(list(graph.nodes()))

            if node1 != node2 and (node1, node2) not in connections and random.random() < 0.2:
                graph.add_edge(node1, node2)
                connections.add((node1, node2))
                connections.add((node2, node1))

                if len(connections) == len(graph.nodes()) - 1:
                    break

        return graph
    
    '''
    Funcion createImage
    Autora: Claudia Landeira

    Devuelve una imagen con el grafo dado por parametros
    '''
    def createImage(graph):
        pos = nx.shell_layout(graph)

        plt.figure(figsize=(14, 7))

        nx.draw_networkx_nodes(graph, pos, node_size=700, node_color="skyblue")
        nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold")
        
        for edge in graph.edges():
            nx.draw_networkx_edges(graph, pos, arrows=True, edgelist=[edge], connectionstyle="arc3,rad=0.3", alpha=0.5)

        plt.axis('off')

        img = io.BytesIO()

        plt.savefig(img, format='png')
        img.seek(0)
        image_base64 = base64.b64encode(img.getvalue()).decode()

        return image_base64
    
    '''
    Funcion nodesLinked
    Autora: Claudia Landeira

    Devuelve una imagen con enlaces asignados
    '''
    def nodesLinked(graph):
        linked = []

        for node in graph.nodes():
            link = f'<a href="/localizacion/{node}">{{ node }}</a>'
            linked.append(link)
        return linked
    