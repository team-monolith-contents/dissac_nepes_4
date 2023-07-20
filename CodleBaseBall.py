from ipywidgets import Image
from ipycanvas import Canvas
import ipywidgets as widgets
from IPython.display import display, clear_output

import random

class Baseball():
    def __init__(self, make_answer, strike_ball, judge, add_history):
        self.__canvas = Canvas(width = 700, height = 500)
        self.__inning = 0
        
        player_button = widgets.BoundedIntText(
            min=0,
            max=999,
            step=1,
            description='정답 입력:',
            disabled=False
        )
        
        display(player_button)
    def play:
        for i in range(9):
            self.__inning = i + 1
    
    player = input("정답을 입력해주세요")
    s,b = strike_ball(player, answer)
    history, result = add_history(history, result, player, s, b)
    if judge(s,b) == 1:
        break
    print("지금까지의 기록입니다 : ", history, result)
    print("-"*50)
    
    def show():
        inning_prompt = f"{i} 번째 이닝입니다({i}/9)".format(self.__inning)
        pass
        
    



# class PokerProject4():
#     def __init__(self, **kwargs):
#         self.__deck = Deck()
#         self.__deck.shuffle()
#         self.__hand = self.__deck[:7]
        
#         self.__canvas = Canvas(width = 700, height = 500)
#         self.__canvas.fill_style = "green"
#         self.__canvas.fill_rect(0, 0, self.__canvas.width, self.__canvas.height)
#         self.__canvas.font = "30px serif"
        
#         try: 
#             self.__one_pair = kwargs['one_pair']
#         except:
#             self.__one_pair = None
#         try:
#             self.__two_pair = kwargs['two_pair']
#         except:
#             self.__two_pair = None
#         try:
#             self.__three_of_a_kind = kwargs['three_of_a_kind']
#         except:
#             self.__three_of_a_kind = None
#         try:
#             self.__straight = kwargs['straight']
#         except:
#             self.__straight = None
#         try:    
#             self.__flush = kwargs['flush']
#         except:
#             self.__flush = None
#         try:    
#             self.__full_house = kwargs['full_house']
#         except:
#             self.__full_house = None
#         try:    
#             self.__four_of_a_kind = kwargs['four_of_a_kind']
#         except:
#             self.__four_of_a_kind = None
#         try:    
#             self.__straight_flush = kwargs['straight_flush']
#         except:
#             self.__straight_flush = None
#         try:    
#             self.__royal_straight_flush = kwargs['royal_straight_flush']
#         except:
#             self.__royal_straight_flush = None
        
#         self.__button = widgets.Button(
#             description='play',
#             disabled=False,
#             button_style='',
#             tooltip='play'
#         )
        
#         self.__output = widgets.Output()
#         display(self.__button, self.__canvas, self.__output)
#         self.__button.on_click(self.__play_function_handler)
    
#     def __show_hand(self):
#         with self.__output:
#             for idx, card in enumerate(sorted(self.__hand)):
#                 self.__canvas.draw_image(card.sprite, 50*(idx%7)+150, 200)

#     def __play_function_handler(self, button):
#         with self.__output:
#             self.__canvas.clear()
#             self.__canvas.fill_style = "green"
#             self.__canvas.fill_rect(0, 0, self.__canvas.width, self.__canvas.height)
            
#             # self.__deck.shuffle()
#             # self.__hand = self.__deck[:7]
#             self.__show_hand()
            
#             # one_pair
#             self.__canvas.fill_style = "red" if self.__one_pair and self.__one_pair(self.__hand) else "white"
#             self.__canvas.fill_text("one_pair", 50, 350, max_width=None)
            
#             # two_pair
#             self.__canvas.fill_style = "red" if self.__two_pair and self.__two_pair(self.__hand) else "white"
#             self.__canvas.fill_text("two_pair", 50, 380, max_width=None)
            
#             # three_of_a_kind
#             self.__canvas.fill_style = "red" if self.__three_of_a_kind and self.__three_of_a_kind(self.__hand) else "white"
#             self.__canvas.fill_text("three_of_a_kind", 50, 410, max_width=None)
            
#             # straight
#             self.__canvas.fill_style = "red" if self.__straight and self.__straight(self.__hand) else "white"
#             self.__canvas.fill_text("straight", 50, 440, max_width=None)
            
#             # flush
#             self.__canvas.fill_style = "red" if self.__flush and self.__flush(self.__hand) else "white"
#             self.__canvas.fill_text("flush", 50, 470, max_width=None)
            
#             # full_house
#             self.__canvas.fill_style = "red" if self.__full_house and self.__full_house(self.__hand) else "white"
#             self.__canvas.fill_text("full_house", 400, 350, max_width=None)
            
#             # four_of_a_kind
#             self.__canvas.fill_style = "red" if self.__four_of_a_kind and self.__four_of_a_kind(self.__hand) else "white"
#             self.__canvas.fill_text("four_of_a_kind", 400, 380, max_width=None)
            
#             # straight_flush
#             self.__canvas.fill_style = "red" if self.__straight_flush and self.__straight_flush(self.__hand) else "white"
#             self.__canvas.fill_text("straight_flush", 400, 410, max_width=None)
            
#             # royal_straight_flush
#             self.__canvas.fill_style = "red" if self.__royal_straight_flush and self.__royal_straight_flush(self.__hand) else "white"
#             self.__canvas.fill_text("royal_straight_flush", 400, 440, max_width=None)
    
#     def set_hand(self, hand):
#         self.__hand = hand

# class PokerProject3():
#     def __init__(self, shuffle):
#         self.__shuffle = shuffle
#         self.__deck = Deck()
        
#         self.__button = widgets.Button(
#             description='Shuffle',
#             disabled=False,
#             button_style='',
#             tooltip='Shuffle'
#         )
                
#         self.__canvas = Canvas(width = 700, height = 500)
#         self.__canvas.fill_style = "green"
#         self.__canvas.fill_rect(0, 0, self.__canvas.width, self.__canvas.height)
        
#         self.__output = widgets.Output()
#         display(self.__canvas, self.__button, self.__output)
#         self.__show_deck()
#         self.__button.on_click(self.__shuffle_function_handler)
    
#     def __show_deck(self):
#         with self.__output:
#             for idx, card in enumerate(self.__deck):
#                 self.__canvas.draw_image(card.sprite, 50*(idx%14), 100*(idx//14))

#     def __shuffle_function_handler(self, button):
#         with self.__output:
#             deck = self.__shuffle(self.__deck)
#             self.__show_deck()
        
# class PokerProject2():
#     def __init__(self, card_list):
#         self.__card_list = card_list
        
#         self.__canvas = Canvas(width = 700, height = 500)
#         self.__canvas.fill_style = "green"
#         self.__canvas.fill_rect(0, 0, self.__canvas.width, self.__canvas.height)
        
#         self.__output = widgets.Output()
#         self.__show_all_cards()
#         display(self.__canvas, self.__output)
    
#     def __show_all_cards(self):
#         with self.__output:
#             for idx, card in enumerate(self.__card_list):
#                 self.__canvas.draw_image(card.sprite, 50*(idx%14), 100*(idx//14))


# class PokerProject1():
#     def __init__(self, judge):
#         self.__judge = judge
        
#         self.__canvas = Canvas(width = 700, height = 500)
#         self.__canvas.fill_style = "green"
#         self.__canvas.fill_rect(0, 0, self.__canvas.width, self.__canvas.height)
#         self.__button = widgets.Button(
#             description='Play Game',
#             disabled=False,
#             button_style='',
#             tooltip='Play Game',
#             icon='play' # (FontAwesome names without the `fa-` prefix)
#         )
#         self.__button2 = widgets.Button(
#             description='Judge',
#             disabled=False,
#             button_style='',
#             tooltip='Judge'
#         )
#         self.__output = widgets.Output()
#         display(self.__canvas, self.__button, self.__output, self.__button2)
#         self.__button.on_click(self.__play)
#         self.__button2.on_click(self.__judge_function_handler)
    
#     def __play(self, button):
#         with self.__output:
#             self.__player1 = Card(random.choice(RANKS), random.choice(SUITS))
#             self.__player2 = Card(random.choice(RANKS), random.choice(SUITS))

#             self.__canvas.clear()
#             self.__canvas.fill_style = "green"
#             self.__canvas.fill_rect(0, 0, self.__canvas.width, self.__canvas.height)
            
#             self.__canvas.font = "32px serif"
#             self.__canvas.fill_style = "white"
#             self.__canvas.fill_text("Player1", 200, 150, max_width=None)
#             self.__canvas.fill_text("Player2", 400, 150, max_width=None)
            
#             self.__canvas.draw_image(self.__player1.sprite, 200, 200)
#             self.__canvas.draw_image(self.__player2.sprite, 400, 200)
            
#     def __judge_function_handler(self, button):
#         with self.__output:
#             result = self.__judge(self.__player1, self.__player2)

#             self.__canvas.font = "32px serif"
#             self.__canvas.fill_style = "white"

#             if result == 1:
#                 self.__canvas.fill_text("Player1 WIN!", 300, 400, max_width=None)
#             elif result == 0:
#                 self.__canvas.fill_text("DRAW", 300, 400, max_width=None)
#             elif result == -1:
#                 self.__canvas.fill_text("Player2 WIN!", 300, 400, max_width=None)
#             else:
#                 self.__canvas.fill_text("잘못된 형식입니다", 300, 400, max_width=None)
class PokerProject2():
    def __init__(self, card_list):
        self.__canvas = Canvas(width = 700, height = 500)
        self.__card_list = self.__list_to_card(card_list)
        self.__show_all_cards()

    def __list_to_card(self, card_list):
        retcard = []
        for card in card_list:
            retcard.append(Card(card[0],card[1]))
        return retcard
        
    def __show_all_cards(self):
        for idx, card in enumerate(self.__card_list):
            self.__canvas.draw_image(card.sprite, 50*(idx%14), 100*(idx//14))
        display(self.__canvas)


class PokerProject1():
    def __init__(self, rank, suit):
        self.__canvas = Canvas(width = 700, height = 500)
        self.__card = Card(rank,suit)
        self.__show_all_cards()

    def __show_all_cards(self):
        self.__canvas.draw_image(self.__card.sprite,0,0)
        display(self.__canvas)
               
        
class Deck():
    def __init__(self):
        self.__deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = Card (rank, suit)
                self.__deck.append(card)
                
    def __iter__(self):
        return iter(self.__deck)
    
    def __len__(self):
        return len(self.__deck)
    
    def __getitem__(self, item):
         return self.__deck[item]
    
    def __setitem__(self, key, value):
        self.__deck[key] = value
    
    def shuffle(self):
        random.shuffle(self.__deck)
        
        
class Card():
    def __init__(self, rank, suit):
        if not rank in RANKS : 
            raise ValueError("Wrong rank, rank should be integer of 2 <= rank <=14")
        if not suit in SUITS:
            raise ValueError("Wrong suit, suit must be on of the following : 'C', 'D', 'H' and 'S'")
        self.__rank = rank
        self.__suit = suit

        transition = {'C' : 1,
                        'D' : 2,
                        'H' : 3,
                        'S' : 4}

        card_number = (self.__rank - 2)*4 + transition[self.__suit]
        self.__image_name = f'./Cards/Full/{card_number}.png'
        self.__sprite = Image.from_file(self.__image_name)
    
    @property
    def rank(self):
        return self.__rank
    
    @property
    def suit(self):
        return self.__suit
    
    @property
    def sprite(self):
        return self.__sprite
    
    def __str__(self):
        if self.__rank == 14:
            rank = 'A'
        elif self.__rank == 13:
            rank = 'K'
        elif self.__rank == 12:
            rank = 'Q'
        elif self.__rank == 11:
            rank = 'J'
        else:
            rank = str(rank)
        return self.suit + rank
    
    def __eq__ (self, other):
        return (self.rank == other.rank)

    def __ne__ (self, other):
        return (self.rank != other.rank)

    def __lt__ (self, other):
        return (self.rank < other.rank)

    def __le__ (self, other):
        return (self.rank <= other.rank)

    def __gt__ (self, other):
        return (self.rank > other.rank)

    def __ge__ (self, other):
        return (self.rank >= other.rank)

    