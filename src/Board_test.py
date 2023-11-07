class TestBoard:
    def test_adj(self):
        from Board import Board
        from Terrain import Terrain

        aMap = Board()
        assert aMap.get(2, 3).terrain == Terrain.DESERT
        assert aMap.get(6, 3).terrain == Terrain.LAKE
        assert aMap.get(7, 7).terrain == Terrain.SWAMP

        assert aMap.get_directly_adj(start=(2, 3)) == [
            (2, 2),
            (3, 2),
            (3, 3),
            (3, 4),
            (2, 4),
            (1, 3),
        ]
        assert aMap.get_directly_adj(start=(2, 3), terain_filter=Terrain.DESERT) == []
        assert aMap.get_directly_adj(start=(2, 3), terain_filter=Terrain.SWAMP) == [(2, 2)]
        assert aMap.get_directly_adj(start=(2, 3), terain_filter=Terrain.LAKE) == [
            (1, 3),
            (3, 4),
        ]
        assert aMap.get_directly_adj(start=(2, 3), terain_filter=Terrain.WASTELAND) == [
            (2, 4)
        ]
        assert aMap.get_directly_adj(start=(2, 3), terain_filter=Terrain.RIVER) == [
            (3, 2),
            (3, 3),
        ]

        assert aMap.check_adjacency((6, 3), (4, 3), 0) == "Not"
        assert aMap.check_adjacency((6, 3), (5, 3), 0) == "Direct"

        assert aMap.ge_indirectly_adj(start=(2, 3), shipping_limit=1) == [
            (2, 2),
            (3, 2),
            (2, 1),
            (3, 1),
            (4, 2),
            (3, 3),
            (2, 3),
            (4, 4),
            (3, 4),
            (2, 4),
            (1, 3),
        ]
        assert aMap.ge_indirectly_adj(start=(2, 3), terain_filter=Terrain.DESERT) == [
            (2, 3)
        ]
        assert aMap.ge_indirectly_adj(
            start=(2, 3), terain_filter=Terrain.SWAMP, shipping_limit=1
        ) == [(2, 2), (4, 4)]
        assert aMap.ge_indirectly_adj(
            start=(2, 3), terain_filter=Terrain.LAKE, shipping_limit=1
        ) == [(1, 3), (3, 4)]
        assert aMap.ge_indirectly_adj(
            start=(2, 3), terain_filter=Terrain.WASTELAND, shipping_limit=1
        ) == [(2, 4)]
        assert aMap.ge_indirectly_adj(
            start=(2, 3), terain_filter=Terrain.RIVER, shipping_limit=1
        ) == [(3, 2), (2, 1), (3, 3), (4, 3)]
        assert aMap.ge_indirectly_adj(
            start=(2, 3), terain_filter=Terrain.FIELD, shipping_limit=1
        ) == [(3, 1)]
        assert aMap.ge_indirectly_adj(
            start=(2, 3), terain_filter=Terrain.MOUNTAIN, shipping_limit=1
        ) == [(4, 2)]

        assert aMap.check_adjacency((7, 7), (9, 6), 0) == "Not"
        assert aMap.check_adjacency((7, 7), (9, 6), 1) == "Indirect"
        assert aMap.check_adjacency((7, 7), (8, 3), 2) == "Not"
        assert aMap.check_adjacency((7, 7), (8, 3), 3) == "Indirect"
        assert aMap.check_adjacency((7, 7), (8, 1), 4) == "Not"
        assert aMap.check_adjacency((7, 7), (8, 1), 5) == "Indirect"
