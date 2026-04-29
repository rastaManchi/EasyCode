status = 'prod'

if status == 'prod':
    from .module_prod import *
else:
    from .module import *