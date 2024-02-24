from Board import Board
from Board import AdjacencyType
from Terrain import Terrain


class TestBoard:
    def test_direct_adj(self):
        aMap = Board()
        assert aMap.get_directly_adj(start=(2, 3)) == {
            aMap.get((2, 2)),
            aMap.get((3, 2)),
            aMap.get((3, 3)),
            aMap.get((3, 4)),
            aMap.get((2, 4)),
            aMap.get((1, 3)),
        }

    def test_filter_with_direct_adj(self):
        aMap = Board()
        my_set = set()
        assert (
            aMap.filter_terrain(
                aMap.get_directly_adj(start=(2, 3)), terrain_filter=Terrain.DESERT
            )
            == my_set
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

    def test_check_adj_with_direct_adj(self):
        aMap = Board()
        assert aMap.check_adjacency((6, 3), (4, 3), 0) is None
        assert aMap.check_adjacency((6, 3), (5, 3), 0) == AdjacencyType.DIRECT

    def test_indirect_adj(self):
        aMap = Board()
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

    def test_filter_with_indirect_adj(self):
        aMap = Board()
        my_set = set()
        assert (
            aMap.filter_terrain(
                aMap.get_indirectly_adj(tile=aMap.get((2, 3))),
                terrain_filter=Terrain.DESERT,
            )
            == my_set
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

    def test_check_adj_with_indirect_adj(self):
        aMap = Board()
        assert aMap.check_adjacency((7, 7), (9, 6), 0) == None
        assert aMap.check_adjacency((7, 7), (9, 6), 1) == AdjacencyType.INDIRECT
        assert aMap.check_adjacency((7, 7), (8, 3), 2) == None
        assert aMap.check_adjacency((7, 7), (8, 3), 3) == AdjacencyType.INDIRECT
        assert aMap.check_adjacency((7, 7), (8, 1), 4) == None
        assert aMap.check_adjacency((7, 7), (8, 1), 5) == AdjacencyType.INDIRECT

    def test_init(self):
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
        assert aMap.get((2, 3))._terrain == Terrain.DESERT
        assert aMap.get_tiles_of_type(Terrain.LAKE) == {
            aMap.get((3, 0)),
            aMap.get((10, 0)),
            aMap.get((1, 3)),
            aMap.get((6, 3)),
            aMap.get((3, 4)),
            aMap.get((12, 4)),
            aMap.get((11, 6)),
            aMap.get((1, 7)),
            aMap.get((6, 7)),
            aMap.get((3, 8)),
            aMap.get((10, 8)),
        }
        assert aMap.get_tiles_of_type(Terrain.DESERT) == {
            aMap.get((4, 0)),
            aMap.get((0, 1)),
            aMap.get((7, 1)),
            aMap.get((11, 1)),
            aMap.get((2, 3)),
            aMap.get((7, 4)),
            aMap.get((4, 5)),
            aMap.get((9, 6)),
            aMap.get((12, 6)),
            aMap.get((0, 7)),
            aMap.get((6, 8)),
        }
        assert aMap.get_tiles_of_type(Terrain.RIVER) == {
            aMap.get((1, 1)),
            aMap.get((2, 1)),
            aMap.get((5, 1)),
            aMap.get((6, 1)),
            aMap.get((9, 1)),
            aMap.get((10, 1)),
            aMap.get((0, 2)),
            aMap.get((1, 2)),
            aMap.get((3, 2)),
            aMap.get((5, 2)),
            aMap.get((7, 2)),
            aMap.get((9, 2)),
            aMap.get((11, 2)),
            aMap.get((12, 2)),
            aMap.get((3, 3)),
            aMap.get((4, 3)),
            aMap.get((7, 3)),
            aMap.get((9, 3)),
            aMap.get((8, 4)),
            aMap.get((9, 4)),
            aMap.get((2, 5)),
            aMap.get((3, 5)),
            aMap.get((6, 5)),
            aMap.get((7, 5)),
            aMap.get((8, 5)),
            aMap.get((0, 6)),
            aMap.get((1, 6)),
            aMap.get((2, 6)),
            aMap.get((4, 6)),
            aMap.get((6, 6)),
            aMap.get((8, 6)),
            aMap.get((3, 7)),
            aMap.get((4, 7)),
            aMap.get((5, 7)),
            aMap.get((8, 7)),
            aMap.get((9, 8)),
        }
