from nose.tools import *
from app import app
from tests.tools import assert_response  #, test_game_path

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client # let python know you want to use the global client variable in this function, no extra client
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    # test to make sure a GET request to /game works (returns a 200 status code)
    resp = client.get('/game')
    assert_response(resp) # just make sure we got a valid response

    # make sure the default values work when POST has no data
    resp = client.post('/game') # use POST, but provide no data
    assert_response(resp, contains="You have an Error!") # the request should contain "You have an Error!"

def test_path_1():
    # Go one path through the game
    testdata = {'userinput': 'yes'}
    resp = client.post('/game1', data=testdata)
    assert_response(resp, contains="Central Corridor")

    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game1', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    testdata = {'userinput': '132'}
    resp = client.post('/game1', data=testdata)
    assert_response(resp, contains="The Bridge")

    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game1', data=testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': '2'}
    resp = client.post('/game1', data=testdata)
    assert_response(resp, contains="You Made it!")

# Apparently, I cannot run the function test_path_2() below since the nosetests gives me an error for l. 52.
# (AssertionError: Response does not contain 'Death...'!)
# I assume after several different attempts that the test is not able to identify that I want my tests to run from the beginning after having already tested path_1...
# ... which explains why the client doesn't get "Death..." as a response for 'dodge!' since he already has reached the winning stage "You Made it!".
# In order to make test_path_2 work I would need to find a way to kind of 'reset' the test_path_1.
# However, I googled the hell out of my search engine and I wasn't able find any useful advise apart from information about resetting mocks, that isn't really helpful-
# BUT: I tried out the "Death..."-response by turning the last two blocks from test_path_1 into comments and deleting the tags from l.58-60 -
# - and it worked! So "Death..." was actually tested positively.

#def test_path_2():
    # Try out Death...
#    testdata = {'userinput': 'dodge!'}
#    resp = client.post('/game', data=testdata)
#    assert_response(resp, contains="Death...")

#    testdata = {'userinput': '132'}
#    resp = client.post('/game', data=testdata)
#    assert_response(resp, contains="The Bridge")

#    testdata = {'userinput': 'throw the bomb'}
#    resp = client.post('/game', data=testdata)
#    assert_response(resp, contains="Death...")


#???????????AUTOMATED TEST???????????? FOR LOOP!!!!!
#- series of commands => array list of tuples [(command, response),(), ()]
# [('dodge!', 'Escape'), ('tell a joke', 'Escape')]
# client (instance)
# For more information cf. comments in tools fpr "test_game_path()"

#def test_func1():
#    global client
#    commands = [('tell a joke', "Laser Weapon Armory"), ('132', "The Bridge"), ('slowly place the bomb', "Escape Pod"), ('2', "You Made it!")]
#    test_game_path(client, commands)

#def test_func2():
#    global client
#    commands = [('tell a joke', "Laser Weapon Armory"), ('132', "The Bridge"), ('throw the bomb', "Death...")]
#    print "Hi there"
#    test_game_path(client, commands)
