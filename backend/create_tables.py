from geral.config import *
from models.car import *
from models.customer import *
from models.employee import *
from models.motorcycle import *
from models.person import *
from models.sales import *
from models.vehicle import *


if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()