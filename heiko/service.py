from tabulate import tabulate

from heiko.utils import log

# ServiceApi Functions


def show_service_stats(auth, client):
    """
    Shows service stats
    :auth: dict
    :client: service_client object
    :returns: bool
    """

    items = client.service_stats_get().to_dict()["items"]
    users = client.service_stats_get().to_dict()["users"]

    log("Number of Items: %s" % items["count"])
    it = []
    for x in items["cost"].keys():
        it.append([x, float(items["cost"][x]) / 100])

    log(tabulate(it, headers=["Measurement", "Cost (EUR)"], tablefmt="presto", floatfmt=".2f"))
    log("")

    log("Number of Users: %s" % users["count"])
    ut = []
    for x in users["credits"].keys():
        ut.append([x, float(users["credits"][x]) / 100])

    log(tabulate(ut, headers=["Measurement", "Credits (EUR)"], tablefmt="presto", floatfmt=".2f"))
    log("")
    return True
