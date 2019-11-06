# -*- coding: utf-8 -*-

import random
import swagger_client
from tabulate import tabulate

from heiko.utils import log, yes_or_no


# ItemsApi Functions

def show_item(auth, client, itemid):
    """
    Shows detail of a single item
    :auth: dict
    :client: item_client object
    :returns: bool
    """

    log(client.items_item_id_get(itemid).to_dict())
    return True


def delete_item(auth, client):
    """
    Deletes an item from the backend
    :auth: dict
    :client: item_client object
    :returns: bool
    """

    itemid = input("What item (ID)?: ")

    item_name = client.items_item_id_get(itemid).to_dict()["name"]

    really_delete = yes_or_no("Do you really want to delete %s?" % item_name)

    if really_delete is False:
        log("Aborted")
        return False

    try:
        client.items_item_id_delete(itemid)
        log("Item with id %s was deleted" % itemid, serv="SUCCESS")
        return True
    except:
        log("Could not delete item with id %s" % itemid, serv="ERROR")
        return False


def list_items_stats(auth, client):
    """
    Lists stats for all items in the database

    :auth: dict
    :returns: bool
    """

    try:
        items = client.items_stats_get()
    except swagger_client.rest.ApiException:
        log("Could not show items from the database.", serv="ERROR")

    it = []
    revenue = 0.0
    for i in items:
        d = i.to_dict()
        it.append([d["id"], float(d["cost"]) / 100, d["name"], d["consumed"]])
        revenue += float(d["cost"]) / 100 * float(d["consumed"])

    log(tabulate(it, headers=["ID", "Cost (EUR)", "Drink", "Consumptions"], floatfmt=".2f", tablefmt="presto"))
    log("total revenue (EUR): %.2f" % revenue)

    return True


def consume_item(auth, client, itemid):
    """
    Sends request to the backend that user took 1 item out of the fridge

    :auth: dict
    :itemid: int
    :returns: bool
    """

    # Lets try to be a little funny
    prost_msgs = [
        "Well, drink responsible",
        "Gesondheid (Cheers in Afrikaans)",
        "Gan bay (Cheers in Mandarin)",
        "Na zdravi (Cheers in Czech)",
        "Proost (Cheers in Dutch)",
        "Ah la vo-tre sahn-tay (Cheers in French)",
        "Zum Wohl! (Cheers in German)",
        "Yamas (Cheers in Greek)",
        "Slawn-cha (Cheers in Irish Gaelic)",
        "Salute (Cheers in Italian)",
        "Kanpai (Cheers in Japanese)",
        "Gun bae (Cheers in Korean)",
        "Na zdrowie (Cheers in Polish)",
        "Happy hacking!",
        "Well.. just hackspace things.",
    ]

    try:
        client.items_item_id_consume_patch(itemid)

        # TODO: Temp hack to display correct credits in banner
        cost = float(client.items_item_id_get(itemid).to_dict()["cost"])
        auth["user"]["credits"] = auth["user"]["credits"] - cost

        log(random.choice(prost_msgs), serv="SUCCESS")
        log("Cost: %.2f Euro" % (cost / 100), serv="SUCCESS")

        return True

    except swagger_client.rest.ApiException:
        log("Not enough credits, dude.", serv="ERROR")
        return False
    except:
        log("Something went wrong, contact developer!", serv="ERROR")
        return False


def create_item(auth, client):
    """
    Asks admin for details and creates new item in the backend

    :auth: dict
    :returns: bool
    """

    name = input("Name of Drink: ")

    # TODO: Remove this? MaaS does not seem to mind non-alphanumerical charaters...
    if name.isalnum() is False:
        log("Item name not valid. Please be alphanumerical.", serv="ERROR")
        return False

    cost = float(input("Price in EUR (i.e. 1 or 1.20): ")) * 100

    if cost < 0:
        log("Negative price is not allowed ;)", serv="ERROR")
        return False

    try:
        client.items_post(name, int(cost))
        log("Successfully added new item with name %.2f and cost %.2f" % (name, float(cost) / 100), serv="SUCCESS")
    except swagger_client.rest.ApiException as api_expception:
        log("Item could not be created in the backend: " + api_expception.body, serv="ERROR")
        return False

    return True


def update_item(auth, client):
    """
    Adjust the name/price of an item

    :auth: dict
    :returns: bool
    """

    item_id = input("ID of item: ")

    if item_id.isalnum() is False:
        return False

    # Ask for new Cost
    try:
        new_cost = float(input("New price in EUR (i.e. 1 or 1.20): ")) * 100
    except ValueError:
        return False

    if new_cost < 0:
        log("Negative price is not allowed ;)", serv="ERROR")
        return False

    # Ask for new Name
    # TODO as not needed

    # get current item name
    current_item = client.items_item_id_get(item_id).to_dict()
    current_cost = current_item["cost"]
    current_name = current_item["name"]

    try:
        client.items_item_id_patch(item_id, name=current_name, cost=int(new_cost))
        log("Successfully modified price of %s from %s to %s" % (current_name, float(current_cost) / 100, float(new_cost) / 100), serv="SUCCESS")
    except swagger_client.rest.ApiException as api_expception:
        log("Item could not be updated in the backend: " + api_expception.body, serv="ERROR")
        return False

    return True
