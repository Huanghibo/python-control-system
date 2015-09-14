
class System(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'default')
        self.id = kwargs.get('id', self.name)
        self.nodes = {'control':{}, 'interface':{}, 'device':{}}
    @property
    def control_nodes(self):
        return self.nodes['control']
    @property
    def interface_nodes(self):
        return self.nodes['interface']
    @property
    def device_nodes(self):
        return self.nodes['device']
    def add_node(self, node=None, cls=None, **kwargs):
        if node is None:
            kwargs['system'] = self
            node = cls(**kwargs)
        if node.id not in self.nodes[node.node_type]:
            self.nodes[node.node_type][node.id] = node
        return node
