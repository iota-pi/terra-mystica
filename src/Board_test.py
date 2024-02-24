from Board import Board
from Board import AdjacencyType
from Terrain import Terrain


class TestBoard:
    def test_adj(self):
        aMap = Board()
        assert aMap.get((2, 3)).terrain == Terrain.DESERT
        assert aMap.get((2, 2)).terrain == Terrain.SWAMP
        assert aMap.get((3, 2)).terrain == Terrain.RIVER
        assert aMap.get((3, 3)).terrain == Terrain.RIVER
        assert aMap.get((3, 4)).terrain == Terrain.LAKE
        assert aMap.get((2, 4)).terrain == Terrain.WASTELAND
        assert aMap.get((1, 3)).terrain == Terrain.LAKE
        assert aMap.get((6, 3)).terrain == Terrain.LAKE
        assert aMap.get((7, 7)).terrain == Terrain.SWAMP

        assert aMap.get_directly_adj(start=(2, 3)) == {
            aMap.get((2, 2)),
            aMap.get((3, 2)),
            aMap.get((3, 3)),
            aMap.get((3, 4)),
            aMap.get((2, 4)),
            aMap.get((1, 3)),
        }
        assert (
            len(
                aMap.filter_terrain(
                    aMap.get_directly_adj(start=(2, 3)), terrain_filter=Terrain.DESERT
                )
            )
            == 0
        )
        assert aMap.filter_terrain(
            aMap.get_directly_adj(start=(2, 3)), terrain_filter=Terrain.SWAMP
        ) == {aMap.get((2, 2))}
        assert aMap.filter_terrain(
            aMap.get_directly_adj(start=(2, 3)), terrain_filter=Terrain.LAKE
        ) == {aMap.get((3, 4)), aMap.get((1, 3))}
        assert aMap.filter_terrain(
            aMap.get_directly_adj(start=(2, 3)), terrain_filter=Terrain.WASTELAND
        ) == {aMap.get((2, 4))}
        assert aMap.filter_terrain(
            aMap.get_directly_adj(start=(2, 3)), terrain_filter=Terrain.RIVER
        ) == {aMap.get((3, 2)), aMap.get((3, 3))}

        assert aMap.check_adjacency((6, 3), (4, 3), 0) is None
        assert aMap.check_adjacency((6, 3), (5, 3), 0) == AdjacencyType.DIRECT

        assert aMap.get_indirectly_adj(tile=aMap.get((1, 4))) == aMap.get_directly_adj(
            start=(1, 4)
        )
        assert aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1) == {
            aMap.get((2, 2)),
            aMap.get((3, 2)),
            aMap.get((2, 1)),
            aMap.get((3, 1)),
            aMap.get((4, 2)),
            aMap.get((3, 3)),
            aMap.get((4, 3)),
            aMap.get((4, 4)),
            aMap.get((3, 4)),
            aMap.get((2, 4)),
            aMap.get((1, 3)),
        }
        assert (
            len(
                aMap.filter_terrain(
                    aMap.get_indirectly_adj(tile=aMap.get((2, 3))),
                    terrain_filter=Terrain.DESERT,
                )
            )
            == 0
        )
        assert aMap.filter_terrain(
            aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1),
            terrain_filter=Terrain.SWAMP,
        ) == {aMap.get((2, 2)), aMap.get((4, 4))}
        assert aMap.filter_terrain(
            aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1),
            terrain_filter=Terrain.LAKE,
        ) == {aMap.get((3, 4)), aMap.get((1, 3))}
        assert aMap.filter_terrain(
            aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1),
            terrain_filter=Terrain.WASTELAND,
        ) == {aMap.get((2, 4))}
        assert aMap.filter_terrain(
            aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1),
            terrain_filter=Terrain.RIVER,
        ) == {aMap.get((3, 2)), aMap.get((2, 1)), aMap.get((3, 3)), aMap.get((4, 3))}
        assert aMap.filter_terrain(
            aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1),
            terrain_filter=Terrain.FIELD,
        ) == {aMap.get((3, 1))}
        assert aMap.filter_terrain(
            aMap.get_indirectly_adj(tile=aMap.get((2, 3)), shipping_limit=1),
            terrain_filter=Terrain.MOUNTAIN,
        ) == {aMap.get((4, 2))}

        assert aMap.check_adjacency((7, 7), (9, 6), 0) == None
        assert aMap.check_adjacency((7, 7), (9, 6), 1) == AdjacencyType.INDIRECT
        assert aMap.check_adjacency((7, 7), (8, 3), 2) == None
        assert aMap.check_adjacency((7, 7), (8, 3), 3) == AdjacencyType.INDIRECT
        assert aMap.check_adjacency((7, 7), (8, 1), 4) == None
        assert aMap.check_adjacency((7, 7), (8, 1), 5) == AdjacencyType.INDIRECT

    def test_start(self):
        aMap = Board()
        assert aMap.get((2, 3)).terrain == Terrain.DESERT
        assert aMap.get_tiles_of_type(Terrain.LAKE) == [
            (3, 0),
            (10, 0),
            (1, 3),
            (6, 3),
            (3, 4),
            (12, 4),
            (11, 6),
            (1, 7),
            (6, 7),
            (3, 8),
            (10, 8),
        ]
        assert aMap.get_tiles_of_type(Terrain.DESERT) == [
            (4, 0),
            (0, 1),
            (7, 1),
            (11, 1),
            (2, 3),
            (7, 4),
            (4, 5),
            (9, 6),
            (12, 6),
            (0, 7),
            (6, 8),
        ]
        assert aMap.get_tiles_of_type(Terrain.RIVER) == [
            (1, 1),
            (2, 1),
            (5, 1),
            (6, 1),
            (9, 1),
            (10, 1),
            (0, 2),
            (1, 2),
            (3, 2),
            (5, 2),
            (7, 2),
            (9, 2),
            (11, 2),
            (12, 2),
            (3, 3),
            (4, 3),
            (7, 3),
            (9, 3),
            (8, 4),
            (9, 4),
            (2, 5),
            (3, 5),
            (6, 5),
            (7, 5),
            (8, 5),
            (0, 6),
            (1, 6),
            (2, 6),
            (4, 6),
            (6, 6),
            (8, 6),
            (3, 7),
            (4, 7),
            (5, 7),
            (8, 7),
            (9, 8),
        ]
