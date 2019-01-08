import random
import swagger_client

from heiko.utils import log


### ServiceApi Functions

def show_service_stats(auth, client):
    """
    Shows service stats
    :auth: dict
    :client: service_client object
    :returns: bool
    """

    log(client.service_stats_get().to_dict())
    return True

