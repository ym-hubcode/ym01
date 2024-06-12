
from router import Router

class Network:
    def __init__(self):
        self.topology = {}

    def add_router(self, router_id, position):
        router = Router(router_id)
        self.topology[router_id] = {"router": router, "position": position, "links": []}

    def add_link(self, router1_id, router2_id):
        self.topology[router1_id]["links"].append(router2_id)
        self.topology[router2_id]["links"].append(router1_id)

    def remove_router(self, router_id):
        for neighbor in self.topology[router_id]["links"]:
            self.topology[neighbor]["links"].remove(router_id)
        del self.topology[router_id]

    def remove_link(self, router1_id, router2_id):
        self.topology[router1_id]["links"].remove(router2_id)
        self.topology[router2_id]["links"].remove(router1_id)
