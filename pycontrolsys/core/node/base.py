
class Node(object):
    node_type = None
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.system = kwargs.get('system')
        self.node_address = '/'.join(self.system.id, self.node_type, self.id)
        self.system.add_node(node=self)
    
    
class NetworkedNode(Node):
    def __init__(self, **kwargs):
        super(NetworkedNode, self).__init__(**kwargs)
        self.host_addresses = kwargs.get('host_addresses')
