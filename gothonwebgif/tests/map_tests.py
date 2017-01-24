from nose.tools import *
from map import *

def test_gothon_game_map():
    assert_equal(gothon.go('yes'), central_corridor)
    assert_equal(gothon.go('begin'), central_corridor)
    assert_equal(gothon.go('ready'), central_corridor)
    assert_equal(gothon.go('*'), gothon)    

    assert_equal(central_corridor.go('shoot!'), generic_death)
    assert_equal(central_corridor.go('dodge!'), generic_death)
    room = central_corridor.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    assert_equal(central_corridor.go('*'), central_corridor)

    assert_equal(laser_weapon_armory.go('132'), the_bridge)
    assert_equal(laser_weapon_armory.go('*'), generic_death)

    assert_equal(the_bridge.go('throw the bomb'), generic_death)
    assert_equal(the_bridge.go('slowly place the bomb'), escape_pod)
    assert_equal(the_bridge.go('*'), the_bridge)

    assert_equal(escape_pod.go('2'), the_end_winner)
    assert_equal(escape_pod.go('*'), the_end_loser)
