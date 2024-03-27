import uuid

# Step 1: Generate Provider
class Provider:
    def __init__(self):
        self.id = str(uuid.uuid4())

    def get(self):
        return self.id
    
    def check(self):
        return True