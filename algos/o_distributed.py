import pykka


class SpanningTreeSimpleActor(pykka.ThreadingActor):
    """
        ask: {type='search', parent=<actor_ref>}, return: [<from_ref>, <to_ref>]
        tell: {type='add_child', child=<actor_ref>}
    """

    def __init__(self, id):
        super(SpanningTreeSimpleActor, self).__init__()
        self.id = id
        self._output_refs = []
        self.parent = None

    def on_receive(self, message):
        if message['type'] == 'add_child':
            self._output_refs.append(message['child'])
        elif message['type'] == 'search':
            if self.parent is None:
                self.parent = message['parent']
                futures = []
                for output_ref in self._output_refs:
                    futures.append(output_ref.ask(dict(type='search', parent=self), block=False))

                returned = reduce(lambda x, y: x + y, filter(lambda x: x is not None, map(lambda x: x.get(), futures)),
                                  [])
                returned += [(self.parent.id if self.parent else None, self.id)]

                return returned
            else:
                return None
