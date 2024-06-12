
class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.lsdb = {}
        self.links = []

    def generate_lsa(self):
        return {"router_id": self.router_id, "links": self.links}

    def broadcast_lsa(self, lsa, neighbors):
        for neighbor in neighbors:
            neighbor.receive_lsa(lsa)

    def receive_lsa(self, lsa):
        self.lsdb[lsa["router_id"]] = lsa

    def update(self, message):
        pass
