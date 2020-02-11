
#########################################
##### Name: Boya Li #####################
##### Uniqname: liboya ##################
#########################################

import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        c1=cards.Card(rank=12)
        self.assertEqual(c1.rank_name, "Queen")
    
    def test_2_Clubs(self):
        c2=cards.Card(1)
        self.assertEqual(c2.suit_name, "Clubs")

    def test_3_KingofSpades(self):
        c3=cards.Card(3,13)
        self.assertEqual(c3.__str__(), "King of Spades")

    def test_4_52cards(self):
        d1=cards.Deck().cards
        self.assertEqual(len(d1), 52)
    
    def test_5_dealcardreturn(self):
        d2=cards.Deck().deal_card()
        self.assertIsInstance(d2, cards.Card)

    def test_6_onelesscard(self):
        d3=cards.Deck()
        len_original=len(d3.cards)
        d3.deal_card()
        len_afterwards=len(d3.cards)
        self.assertEqual(len_original-len_afterwards, 1)

    def test_7_replacecard(self):
        d4=cards.Deck()
        len_original=len(d4.cards)
        d5=d4.deal_card()
        d4.replace_card(d5)
        len_afterwards=len(d4.cards)
        self.assertEqual(len_original,len_afterwards)
    
    def test_8_silentignore(self):
        d6=cards.Deck()
        d7=d6.deal_card()
        len_original=len(d6.cards)
        for instance in d6.cards:
            if instance != d7:
                d8=instance
        results=d6.replace_card(d8)
        len_afterwards=len(d6.cards)
        self.assertEqual(results,None)
        self.assertEqual(len_original,len_afterwards)














############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
