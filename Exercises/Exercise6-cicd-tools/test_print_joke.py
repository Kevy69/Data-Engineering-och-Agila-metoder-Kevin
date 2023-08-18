from print_joke import get_random_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert type(reaction) == str


def test_get_random_reaction_repeats():    
    reaction1 = get_random_reaction()
    reaction2 = reaction1
    tries = 0
    
    while reaction1 == reaction2:
        reaction1 = get_random_reaction()
        
        if tries >= 100:
            raise Exception("FUCK")
        
        tries += 1
        



# Come up with a test of your own and implement it here.
def test_print_random_joke_and_reaction_type():
    reaction = get_random_reaction()
    assert type(reaction) == str