
class Node(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.system = kwargs.get('system')
        self.node_address = '/'.join(self.system.id, self.node_type, self.id)
    @property
    def node_type(self):
        nt = getattr(self, '_node_type', None)
        if nt is None:
            nt = self._node_type = self.__class__.__name__.lower()
        return nt
    
class NetworkedNode(Node):
    def __init__(self, **kwargs):
        super(NetworkedNode, self).__init__(**kwargs)
        self.host_addresses = kwargs.get('host_addresses')
