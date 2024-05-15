class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):

    nodes_to_visit = [self.root]

    while nodes_to_visit:
      current = nodes_to_visit.pop(0)
      if current['id'] == id:
        return current
      else:
        nodes_to_visit = current['children'] + nodes_to_visit
    
    return None