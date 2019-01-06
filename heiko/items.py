import random
import swagger_client
from string import ascii_letters
import heiko.menu as menu


### ItemsApi Functions

def list_items(auth, client):
    """
    Lists all items in the database to an admin

    :auth: dict
    :returns: bool
    """

    try:
        menu.log(client.items_get())
    except swagger_client.rest.ApiException:
        menu.log("Could not show items from the database.",serv="ERROR")

    return True

def consume_item(auth, client, itemid):
    """
    Sends request to the backend that user took 1 item out of the fridge

    :auth: dict
    :itemid: int
    :returns: bool
    """

    # Lets try to be a little funny
    cheers_msgs = [
        "Have fun!"
        "Well.. just hackspace things."
        "Nice loscher stuff <3"
        "Beer mh? How are your projects going?"
    ]

    try:
        client.items_item_id_consume_patch(itemid)
        menu.log(random.choice(cheers_msgs) + " Prost!", serv="SUCCESS")
        return True
    except swagger_client.rest.ApiException:
        menu.log("Not enough credits, dude.", serv="ERROR")
        return False
    except:
        menu.log("Something went wrong, contact developer!")
        return False
