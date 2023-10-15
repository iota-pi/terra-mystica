class TestTile:
    def test_building(self):
        from Tile import Tile
        from Terrain import Terrain
        from Building import Building
        
        spot = Tile(Terrain.MOUNTAIN)
        assert spot.can_build(Building.DWELLING)
        assert not spot.can_build(Building.TRADING_HOUSE)
        spot.build(Building.DWELLING)
        assert spot.can_build(Building.TRADING_HOUSE)
        assert not spot.can_build(Building.DWELLING)
        assert not spot.can_build(Building.SANCTUARY)
        spot.build(Building.TRADING_HOUSE)
        assert spot.can_build(Building.TEMPLE)
        assert spot.can_build(Building.STRONGHOLD)
        assert not spot.can_build(Building.DWELLING)
        spot.build(Building.TEMPLE)
        assert spot.can_build(Building.SANCTUARY)
        assert not spot.can_build(Building.STRONGHOLD)
        spot.build(Building.SANCTUARY)
        assert not spot.can_build(Building.DWELLING)
        assert not spot.can_build(Building.TRADING_HOUSE)
        assert not spot.can_build(Building.TEMPLE)
        assert not spot.can_build(Building.STRONGHOLD)
        assert not spot.can_build(Building.SANCTUARY)
        