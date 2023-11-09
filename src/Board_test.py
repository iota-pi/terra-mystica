from Board import Board
from Terrain import Terrain


class TestBoard:
    def test_adj(self):
        aMap = Board()
        assert aMap.get((2, 3))._terrain == Terrain.DESERT
        assert aMap.get((2, 2))._terrain == Terrain.SWAMP
        assert aMap.get((3, 2))._terrain == Terrain.RIVER
        assert aMap.get((3, 3))._terrain == Terrain.RIVER
        assert aMap.get((3, 4))._terrain == Terrain.LAKE
        assert aMap.get((2, 4))._terrain == Terrain.WASTELAND
        assert aMap.get((1, 3))._terrain == Terrain.LAKE
        assert aMap.get((6, 3))._terrain == Terrain.LAKE
        assert aMap.get((7, 7))._terrain == Terrain.SWAMP

        assert aMap.get_directly_adj(start=(2, 3)) == [
            (2, 2),
            (3, 2),
            (3, 3),
            (3, 4),
            (2, 4),
            (1, 3),
        ]
        assert aMap.get_directly_adj(start=(2, 3), terrain_filter=Terrain.DESERT) == []
        assert aMap.get_directly_adj(start=(2, 3), terrain_filter=Terrain.SWAMP) == [
            (2, 2)
        ]
        assert aMap.get_directly_adj(start=(2, 3), terrain_filter=Terrain.LAKE) == [
            (3, 4),
            (1, 3),
        ]
        assert aMap.get_directly_adj(
            start=(2, 3), terrain_filter=Terrain.WASTELAND
        ) == [(2, 4)]
        assert aMap.get_directly_adj(start=(2, 3), terrain_filter=Terrain.RIVER) == [
            (3, 2),
            (3, 3),
        ]

        assert aMap.check_adjacency((6, 3), (4, 3), 0) == "Not"
        assert aMap.check_adjacency((6, 3), (5, 3), 0) == "Direct"

        assert aMap.get_indirectly_adj(start=(1, 4)) == aMap.get_directly_adj(
            start=(1, 4)
        )
        assert aMap.get_indirectly_adj(start=(2, 3), shipping_limit=1) == [
            (2, 2),
            (3, 2),
            (2, 1),
            (3, 1),
            (4, 2),
            (3, 3),
            (4, 3),
            (4, 4),
            (3, 4),
            (2, 4),
            (1, 3),
        ]
        assert (
            aMap.get_indirectly_adj(start=(2, 3), terrain_filter=Terrain.DESERT) == []
        )
        assert aMap.get_indirectly_adj(
            start=(2, 3), terrain_filter=Terrain.SWAMP, shipping_limit=1
        ) == [(2, 2), (4, 4)]
        assert aMap.get_indirectly_adj(
            start=(2, 3), terrain_filter=Terrain.LAKE, shipping_limit=1
        ) == [(3, 4), (1, 3)]
        assert aMap.get_indirectly_adj(
            start=(2, 3), terrain_filter=Terrain.WASTELAND, shipping_limit=1
        ) == [(2, 4)]
        assert aMap.get_indirectly_adj(
            start=(2, 3), terrain_filter=Terrain.RIVER, shipping_limit=1
        ) == [(3, 2), (2, 1), (3, 3), (4, 3)]
        assert aMap.get_indirectly_adj(
            start=(2, 3), terrain_filter=Terrain.FIELD, shipping_limit=1
        ) == [(3, 1)]
        assert aMap.get_indirectly_adj(
            start=(2, 3), terrain_filter=Terrain.MOUNTAIN, shipping_limit=1
        ) == [(4, 2)]

        assert aMap.check_adjacency((7, 7), (9, 6), 0) == "Not"
        assert aMap.check_adjacency((7, 7), (9, 6), 1) == "Indirect"
        assert aMap.check_adjacency((7, 7), (8, 3), 2) == "Not"
        assert aMap.check_adjacency((7, 7), (8, 3), 3) == "Indirect"
        assert aMap.check_adjacency((7, 7), (8, 1), 4) == "Not"
        assert aMap.check_adjacency((7, 7), (8, 1), 5) == "Indirect"
