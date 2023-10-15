class BoardTest:
    def test_adj(self):
        from Board import Board
        from Terrain import Terrain
        
        aMap = Board()
        assert aMap.get(2, 3).terrain == Terrain.DESERT
        assert aMap.get(6, 3).terrain == Terrain.LAKE
        assert aMap.get(7, 7).terrain == Terrain.SWAMP
        
        assert aMap.getDirectlyAdj(start = (2, 3)) == [(2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 3)]
        assert aMap.getDirectlyAdj(start = (2, 3), TerainFilter = Terrain.DESERT) == []
        assert aMap.getDirectlyAdj(start = (2, 3), TerainFilter = Terrain.SWAMP) == [(2, 2)]
        assert aMap.getDirectlyAdj(start = (2, 3), TerainFilter = Terrain.LAKE) == [(1, 3), (3, 4)]
        assert aMap.getDirectlyAdj(start = (2, 3), TerainFilter = Terrain.WASTELAND) == [(2, 4)]
        assert aMap.getDirectlyAdj(start = (2, 3), TerainFilter = Terrain.RIVER) == [(3, 2), (3, 3)]
        
        assert aMap.checkAdjacency((6, 3), (4, 3), 0) == "Not"
        assert aMap.checkAdjacency((6, 3), (5, 3), 0) == "Direct"
        
        assert aMap.getIndirectlyAdj(start = (2, 3), shippingLimit = 1) == [(2, 2), (3, 2), (2, 1), (3, 1), (4, 2), (3, 3), (2, 3), (4, 4), (3, 4), (2, 4), (1, 3)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.DESERT) == [(2, 3)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.SWAMP, shippingLimit = 1) == [(2, 2), (4, 4)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.LAKE, shippingLimit = 1) == [(1, 3), (3, 4)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.WASTELAND, shippingLimit = 1) == [(2, 4)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.RIVER, shippingLimit = 1) == [(3, 2), (2, 1), (3, 3), (4, 3)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.FIELD, shippingLimit = 1) == [(3, 1)]
        assert aMap.getIndirectlyAdj(start = (2, 3), TerainFilter = Terrain.MOUNTAIN, shippingLimit = 1) == [(4, 2)]
        
        assert aMap.checkAdjacency((7, 7), (9, 6), 0) == "Not"
        assert aMap.checkAdjacency((7, 7), (9, 6), 1) == "Indirect"
        assert aMap.checkAdjacency((7, 7), (8, 3), 2) == "Not"
        assert aMap.checkAdjacency((7, 7), (8, 3), 3) == "Indirect"
        assert aMap.checkAdjacency((7, 7), (8, 1), 4) == "Not"
        assert aMap.checkAdjacency((7, 7), (8, 1), 5) == "Indirect"
