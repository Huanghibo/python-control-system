from pycontrolsys.core.node.base import NetworkedNode

class ControlNode(NetworkedNode):
    node_type = 'control'
    def __init__(self, **kwargs):
        super(ControlNode, self).__init__(**kwargs)
        self.device_nodes = kwargs.get('device_nodes')
        
