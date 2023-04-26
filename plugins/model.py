import config
import wheatly.utils as utils

class Model:
    def __init__(self):
        self.name = 'model'
        self.tokens = config.lexicon[self.name]['tokens']
        self.actions = config.lexicon[self.name]['actions']
        self.modifiers = config.lexicon[self.name]['modifiers']

    def action_get(self, context, logger, args={}, modifiers=[]):
        # perform get actions for this object
        print('get!')
        # return modified context and success or fail
        return context, True

    def action_delete(self, context, logger, args={}, modifiers=[]):
        # perform delete actions for this object 
        print('delete!')
        # return modified context and success or fail
        return context, True

    def __str__(self):
        return f'{self.name}()'

    def __repr__(self):
        return f'{self.name}()'
