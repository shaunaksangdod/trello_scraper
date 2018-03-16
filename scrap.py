# Board ID(TEST) : 5a9b2a4762eeeac937bb458f
# Key : cb369b88d7602522fbafc26315f80ae5
# Secret (OAUTH) : c2992c0cfd8dcca7edbc9c8d9a5f4d3be345a970372f733afe912017e5c9b4af
# Token : d1ec5556b81731e510220dde2bf5c9f84b99074c6a2cda47eb9443fdb66c1ff7
from trollop import TrelloConnection
import requests
k = []
url = "https://api.trello.com/1/"
def read_config():

    with open('keys.txt', 'r') as keys:
        for line in keys:
            k.append(line.split('=')[1].rstrip().lstrip())

def main():
    # Establish connection
    conn = TrelloConnection(k[0], k[1])

    board = conn.get_board(k[2])
    #---#boardContents = requests.get("https://api.trello.com/1/" + "boards/" + k[2])
    #---#print boardContents
    for list in board.lists:
        print list['name'], "::"
        print "id: " , list['id']
        l = conn.get_list(list['id'])
        for card in l.cards:
            card = conn.get_card(card['id'])
            #---# print card._data #All card data
            card_actions = requests.get("https://api.trello.com/1/" + "cards/" + card['id'] + "/actions",\
                                        params={"key":k[0],"token":k[1],"filter":"commentCard","fields":"data"})
            actions_json = card_actions.json()
            if(len(actions_json) != 0):
                print actions_json[0]['data']['text']
if __name__ == '__main__':
    read_config()

    main()
